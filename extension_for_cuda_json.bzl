load(
    "@rules_ml_toolchain//third_party/gpus/cuda/hermetic:cuda_json_init_repository.bzl",
    "cuda_json_init_repository",
)

def _extension_for_cuda_json_impl(ctx):
    cuda_json_init_repository()

extension_for_cuda_json = module_extension(implementation = _extension_for_cuda_json_impl)
