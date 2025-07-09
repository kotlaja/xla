load("@rules_ml_toolchain//third_party/nvshmem/hermetic:nvshmem_configure.bzl", "nvshmem_configure")
load(
    "@nvshmem_redist_json//:distributions.bzl",
    "NVSHMEM_REDISTRIBUTIONS",
)
load(
    "@rules_ml_toolchain//third_party/nvshmem/hermetic:nvshmem_redist_init_repository.bzl",
    "nvshmem_redist_init_repository",
)
# -- load statements -- #

def _extension_for_nvshmem_configure_impl(ctx):
    nvshmem_configure(
      name = "local_config_nvshmem",
    )
    nvshmem_redist_init_repository(
        nvshmem_redistributions = NVSHMEM_REDISTRIBUTIONS,
    )

# -- repo definitions -- #

extension_for_nvshmem_configure = module_extension(implementation = _extension_for_nvshmem_configure_impl)
