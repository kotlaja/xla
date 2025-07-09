load("@rules_python//python/private/pypi:whl_library.bzl", "whl_library")
# -- load statements -- #

def _extension_for_whl_library_impl(ctx):
  whl_library(
    name = "pypi_lit",
    group_deps = [  ],
    repo = "pypi",
    repo_prefix = "pypi_",
    requirement = "lit==17.0.6     --hash=sha256:dfa9af9b55fc4509a56be7bf2346f079d7f4a242d583b9f2e0b078fd0abae31b",
    download_only = False,
    enable_implicit_namespace_pkgs = False,
    environment = {  },
    envsubst = [  ],
    extra_pip_args = [  ],
    isolated = True,
    pip_data_exclude = [  ],
    python_interpreter = "python3",
    python_interpreter_target = "@@python_x86_64-unknown-linux-gnu//:bin/python3",
    quiet = True,
    timeout = 600,
  )
# -- repo definitions -- #

extension_for_whl_library = module_extension(implementation = _extension_for_whl_library_impl)
