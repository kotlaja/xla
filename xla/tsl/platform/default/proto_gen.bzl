"""TODO: kotlaja - Write module docstring."""

# TODO: This rule is not available anymore in higher protobuf versions. Clean up this rule once
# migration is done.

def _GetPath(ctx, path):
    if ctx.label.workspace_root:
        return ctx.label.workspace_root + "/" + path
    else:
        return path

def _IsNewExternal(ctx):
    # Bazel 0.4.4 and older have genfiles paths that look like:
    #   bazel-out/local-fastbuild/genfiles/external/repo/foo
    # After the exec root rearrangement, they look like:
    #   ../repo/bazel-out/local-fastbuild/genfiles/foo
    return ctx.label.workspace_root.startswith("../")

def _GenDir(ctx):
    if _IsNewExternal(ctx):
        # We are using the fact that Bazel 0.4.4+ provides repository-relative paths
        # for ctx.genfiles_dir.
        return ctx.genfiles_dir.path + (
            "/" + ctx.attr.includes[0] if ctx.attr.includes and ctx.attr.includes[0] else ""
        )

    # This means that we're either in the old version OR the new version in the local repo.
    # Either way, appending the source path to the genfiles dir works.
    return ctx.var["GENDIR"] + "/" + _SourceDir(ctx)

def _SourceDir(ctx):
    if not ctx.attr.includes:
        return ctx.label.workspace_root
    if not ctx.attr.includes[0]:
        return _GetPath(ctx, ctx.label.package)
    if not ctx.label.package:
        return _GetPath(ctx, ctx.attr.includes[0])
    return _GetPath(ctx, ctx.label.package + "/" + ctx.attr.includes[0])

def _CcHdrs(srcs, use_grpc_plugin = False):
    ret = [s[:-len(".proto")] + ".pb.h" for s in srcs]
    if use_grpc_plugin:
        ret += [s[:-len(".proto")] + ".grpc.pb.h" for s in srcs]
    return ret

def _CcSrcs(srcs, use_grpc_plugin = False):
    ret = [s[:-len(".proto")] + ".pb.cc" for s in srcs]
    if use_grpc_plugin:
        ret += [s[:-len(".proto")] + ".grpc.pb.cc" for s in srcs]
    return ret

def _CcOuts(srcs, use_grpc_plugin = False):
    return _CcHdrs(srcs, use_grpc_plugin) + _CcSrcs(srcs, use_grpc_plugin)

def _PyOuts(srcs, use_grpc_plugin = False):
    ret = [s[:-len(".proto")] + "_pb2.py" for s in srcs]
    if use_grpc_plugin:
        ret += [s[:-len(".proto")] + "_pb2_grpc.py" for s in srcs]
    return ret

def _proto_gen_impl(ctx):
    """General implementation for generating protos"""
    srcs = ctx.files.srcs
    deps = depset(direct = ctx.files.srcs)
    source_dir = _SourceDir(ctx)
    gen_dir = _GenDir(ctx).rstrip("/")
    if source_dir:
        has_sources = any([src.is_source for src in srcs])
        has_generated = any([not src.is_source for src in srcs])
        import_flags = []
        if has_sources:
            import_flags += ["-I" + source_dir]
        if has_generated:
            import_flags += ["-I" + gen_dir]
        import_flags = depset(direct = import_flags)
    else:
        import_flags = depset(direct = ["-I."])

    for dep in ctx.attr.deps:
        if type(dep.proto.import_flags) == "list":
            import_flags = depset(transitive = [import_flags], direct = dep.proto.import_flags)
        else:
            import_flags = depset(transitive = [import_flags, dep.proto.import_flags])
        if type(dep.proto.deps) == "list":
            deps = depset(transitive = [deps], direct = dep.proto.deps)
        else:
            deps = depset(transitive = [deps, dep.proto.deps])

    if not ctx.attr.gen_cc and not ctx.attr.gen_py and not ctx.executable.plugin:
        return struct(
            proto = struct(
                srcs = srcs,
                import_flags = import_flags,
                deps = deps,
            ),
        )

    for src in srcs:
        args = []

        in_gen_dir = src.root.path == gen_dir
        if in_gen_dir:
            import_flags_real = []
            for f in import_flags.to_list():
                path = f.replace("-I", "")
                import_flags_real.append("-I$(realpath -s %s)" % path)

        outs = []
        use_grpc_plugin = (ctx.attr.plugin_language == "grpc" and ctx.attr.plugin)
        path_tpl = "$(realpath %s)" if in_gen_dir else "%s"
        if ctx.attr.gen_cc:
            args += [("--cpp_out=" + path_tpl) % gen_dir]
            outs.extend(_CcOuts([src.basename], use_grpc_plugin = use_grpc_plugin))
        if ctx.attr.gen_py:
            args += [("--python_out=" + path_tpl) % gen_dir]
            outs.extend(_PyOuts([src.basename], use_grpc_plugin = use_grpc_plugin))

        outs = [ctx.actions.declare_file(out, sibling = src) for out in outs]
        inputs = [src] + deps.to_list()
        tools = [ctx.executable.protoc]
        if ctx.executable.plugin:
            plugin = ctx.executable.plugin
            lang = ctx.attr.plugin_language
            if not lang and plugin.basename.startswith("protoc-gen-"):
                lang = plugin.basename[len("protoc-gen-"):]
            if not lang:
                fail("cannot infer the target language of plugin", "plugin_language")

            outdir = "." if in_gen_dir else gen_dir

            if ctx.attr.plugin_options:
                outdir = ",".join(ctx.attr.plugin_options) + ":" + outdir
            args += [("--plugin=protoc-gen-%s=" + path_tpl) % (lang, plugin.path)]
            args += ["--%s_out=%s" % (lang, outdir)]
            tools.append(plugin)

        if not in_gen_dir:
            ctx.actions.run(
                inputs = inputs,
                tools = tools,
                outputs = outs,
                arguments = args + import_flags.to_list() + [src.path],
                executable = ctx.executable.protoc,
                mnemonic = "ProtoCompile",
                use_default_shell_env = True,
            )
        else:
            for out in outs:
                orig_command = " ".join(
                    ["$(realpath %s)" % ctx.executable.protoc.path] + args +
                    import_flags_real + ["-I.", src.basename],
                )
                command = ";".join([
                    'CMD="%s"' % orig_command,
                    "cd %s" % src.dirname,
                    "${CMD}",
                    "cd -",
                ])
                generated_out = "/".join([gen_dir, out.basename])
                if generated_out != out.path:
                    command += ";mv %s %s" % (generated_out, out.path)
                ctx.actions.run_shell(
                    inputs = inputs,
                    outputs = [out],
                    command = command,
                    mnemonic = "ProtoCompile",
                    tools = tools,
                    use_default_shell_env = True,
                )

    return struct(
        proto = struct(
            srcs = srcs,
            import_flags = import_flags,
            deps = deps,
        ),
    )

"""Generates codes from Protocol Buffers definitions.

This rule helps you to implement Skylark macros specific to the target
language. You should prefer more specific `cc_proto_library `,
`py_proto_library` and others unless you are adding such wrapper macros.

Args:
  srcs: Protocol Buffers definition files (.proto) to run the protocol compiler
    against.
  deps: a list of dependency labels; must be other proto libraries.
  includes: a list of include paths to .proto files.
  protoc: the label of the protocol compiler to generate the sources.
  plugin: the label of the protocol compiler plugin to be passed to the protocol
    compiler.
  plugin_language: the language of the generated sources
  plugin_options: a list of options to be passed to the plugin
  gen_cc: generates C++ sources in addition to the ones from the plugin.
  gen_py: generates Python sources in addition to the ones from the plugin.
  outs: a list of labels of the expected outputs from the protocol compiler.
"""
proto_gen = rule(
    attrs = {
        "srcs": attr.label_list(allow_files = True),
        "deps": attr.label_list(providers = ["proto"]),
        "includes": attr.string_list(),
        "protoc": attr.label(
            cfg = "exec",
            executable = True,
            allow_single_file = True,
            mandatory = True,
        ),
        "plugin": attr.label(
            cfg = "exec",
            allow_files = True,
            executable = True,
        ),
        "plugin_language": attr.string(),
        "plugin_options": attr.string_list(),
        "gen_cc": attr.bool(),
        "gen_py": attr.bool(),
        "outs": attr.output_list(),
    },
    output_to_genfiles = True,
    implementation = _proto_gen_impl,
)
