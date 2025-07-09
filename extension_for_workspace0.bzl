"""TensorFlow workspace initialization. Consult the WORKSPACE on how to use it."""

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

def _extension_for_workspace0_impl(ctx):
    # Toolchains for ML projects hermetic builds.
    # Details: https://github.com/google-ml-infra/rules_ml_toolchain
    http_archive(
        name = "rules_ml_toolchain",
        sha256 = "c85a3ae3da6af08dcc5065387e8d9b033913407c8fa5b074881fce516b482f69",
        strip_prefix = "rules_ml_toolchain-f1e2b169441df00c8b1e9b08371d9ec8e0517ce6",
        urls = [
            "https://github.com/google-ml-infra/rules_ml_toolchain/archive/f1e2b169441df00c8b1e9b08371d9ec8e0517ce6.tar.gz",
        ],
    )

extension_for_workspace0 = module_extension(implementation = _extension_for_workspace0_impl)