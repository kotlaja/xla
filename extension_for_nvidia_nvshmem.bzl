load("//third_party:repo.bzl", "tf_http_archive", "tf_mirror_urls")
load(
    "@nvshmem_redist_json//:distributions.bzl",
    "NVSHMEM_REDISTRIBUTIONS",
)
load(
    "@rules_ml_toolchain//third_party/nvshmem/hermetic:nvshmem_redist_init_repository.bzl",
    "nvshmem_redist_init_repository",
)
# -- load statements -- #

def _extension_for_nvidia_nvshmem_impl(ctx):
    nvshmem_redist_init_repository(
        nvshmem_redistributions = NVSHMEM_REDISTRIBUTIONS,
    )
    tf_http_archive(
        name = "nvshmem",
        strip_prefix = "nvshmem_src",
        sha256 = "2146ff231d9aadd2b11f324c142582f89e3804775877735dc507b4dfd70c788b",
        urls = tf_mirror_urls("https://developer.download.nvidia.com/compute/redist/nvshmem/3.1.7/source/nvshmem_src_3.1.7-1.txz"),
        build_file = "//third_party/nvshmem:nvshmem.BUILD",
        patch_file = ["//third_party/nvshmem:archive.patch"],
        type = "tar",
    )

# -- repo definitions -- #

extension_for_nvidia_nvshmem = module_extension(implementation = _extension_for_nvidia_nvshmem_impl)
