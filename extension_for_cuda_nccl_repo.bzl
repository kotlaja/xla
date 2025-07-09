load(
    "@rules_ml_toolchain//third_party/nccl/hermetic:nccl_redist_init_repository.bzl",
    "nccl_redist_init_repository",
)

def _extension_for_cuda_nccl_repo_impl(ctx):
    nccl_redist_init_repository()
# -- repo definitions -- #

extension_for_cuda_nccl_repo = module_extension(implementation = _extension_for_cuda_nccl_repo_impl)
