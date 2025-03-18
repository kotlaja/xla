load("@tsl//third_party/gpus/cuda/hermetic:cuda_configure.bzl", "cuda_configure")
load(
    "@tsl//third_party/nccl/hermetic:nccl_configure.bzl",
    "nccl_configure",
)
# -- load statements -- #

def _extension_for_cuda_configure_impl(ctx):
  cuda_configure(
    name = "local_config_cuda",
  )
  nccl_configure(name = "local_config_nccl")
# -- repo definitions -- #

extension_for_cuda_configure = module_extension(implementation = _extension_for_cuda_configure_impl)
