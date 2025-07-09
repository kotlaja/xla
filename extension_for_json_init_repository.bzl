load("@rules_ml_toolchain//third_party/gpus:nvidia_common_rules.bzl", "json_init_repository")
# -- load statements -- #

def _extension_for_json_init_repository_impl(ctx):
  json_init_repository(
    name = "nvshmem_redist_json",
    toolkit_name = "NVSHMEM",
    json_dict = {
      "3.2.5": [
          "https://developer.download.nvidia.com/compute/nvshmem/redist/redistrib_3.2.5.json",
          "6945425d3bfd24de23c045996f93ec720c010379bfd6f0860ac5f2716659442d"
      ]
    },
    mirrored_tars_json_dict = {
      "3.2.5": [
          "https://storage.googleapis.com/mirror.tensorflow.org/developer.download.nvidia.com/compute/nvshmem/redist/redistrib_3.2.5_tar.json",
          "641f7ca7048e4acfb466ce8be722f4828b2fa6b8671c28f6e8c230344484fd1c"
      ]
    },
    redist_version_env_vars = [
      "HERMETIC_NVSHMEM_VERSION"
    ],
    local_path_env_var = "LOCAL_NVSHMEM_PATH",
    use_tar_file_env_var = "USE_NVSHMEM_TAR_ARCHIVE_FILES",
  )
  json_init_repository(
    name = "nvshmem_redist_json",
    toolkit_name = "NVSHMEM",
    json_dict = {
      "3.2.5": [
          "https://developer.download.nvidia.com/compute/nvshmem/redist/redistrib_3.2.5.json",
          "6945425d3bfd24de23c045996f93ec720c010379bfd6f0860ac5f2716659442d"
      ]
    },
    mirrored_tars_json_dict = {
      "3.2.5": [
          "https://storage.googleapis.com/mirror.tensorflow.org/developer.download.nvidia.com/compute/nvshmem/redist/redistrib_3.2.5_tar.json",
          "641f7ca7048e4acfb466ce8be722f4828b2fa6b8671c28f6e8c230344484fd1c"
      ]
    },
    redist_version_env_vars = [
      "HERMETIC_NVSHMEM_VERSION"
    ],
    local_path_env_var = "LOCAL_NVSHMEM_PATH",
    use_tar_file_env_var = "USE_NVSHMEM_TAR_ARCHIVE_FILES",
  )
# -- repo definitions -- #

extension_for_json_init_repository = module_extension(implementation = _extension_for_json_init_repository_impl)
