load(
    "//third_party/nccl/hermetic:nccl_configure.bzl",
    "nccl_configure",
)
# load("@rules_ml_toolchain//third_party/nccl/hermetic:nccl_configure.bzl", "nccl_configure")
# -- load statements -- #

def _extension_for_nccl_configure_impl(ctx):
  nccl_configure(
    name = "local_config_nccl",
  )
# -- repo definitions -- #

extension_for_nccl_configure = module_extension(implementation = _extension_for_nccl_configure_impl)
