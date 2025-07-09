load("//third_party/gpus/cuda/hermetic:cuda_configure.bzl", "cuda_configure")
# load(
#     "//third_party/nccl/hermetic:nccl_configure.bzl",
#     "nccl_configure",
# )
# load("@rules_ml_toolchain//third_party/gpus/cuda/hermetic:cuda_configure.bzl", "cuda_configure")
# -- load statements -- #

def _extension_for_cuda_configure_impl(ctx):
  cuda_configure(
    name = "local_config_cuda",
  )
# -- repo definitions -- #

extension_for_cuda_configure = module_extension(implementation = _extension_for_cuda_configure_impl)
