
load(
    "@rules_ml_toolchain//third_party/nvshmem/hermetic:nvshmem_json_init_repository.bzl",
    "nvshmem_json_init_repository",
)
# -- load statements -- #

def _extension_for_nvshmem_redist_json_impl(ctx):
    nvshmem_json_init_repository()

# -- repo definitions -- #

extension_for_nvshmem_redist_json = module_extension(implementation = _extension_for_nvshmem_redist_json_impl)
