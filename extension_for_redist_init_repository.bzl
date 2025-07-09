load(
    "@rules_ml_toolchain//third_party/nvshmem/hermetic:nvshmem_json_init_repository.bzl",
    "nvshmem_json_init_repository",
)
# -- load statements -- #

def _extension_for_redist_init_repository_impl(ctx):
    nvshmem_json_init_repository()
# -- repo definitions -- #

extension_for_redist_init_repository = module_extension(implementation = _extension_for_redist_init_repository_impl)
