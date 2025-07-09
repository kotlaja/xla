# load("//third_party/gpus/cuda/hermetic:cuda_redist_init_repositories.bzl", "cuda_repo")
# -- load statements -- #

load(
    "@rules_ml_toolchain//third_party/gpus/cuda/hermetic:cuda_redist_init_repositories.bzl",
    "cuda_redist_init_repositories",
    "cudnn_redist_init_repository",
)
load(
    "@cuda_redist_json//:distributions.bzl",
    "CUDA_REDISTRIBUTIONS",
    "CUDNN_REDISTRIBUTIONS",
)
# load(
#     "@rules_ml_toolchain//third_party/gpus/cuda/hermetic:cuda_configure.bzl",
#     "cuda_configure",
# )
# load(
#     "@rules_ml_toolchain//third_party/nccl/hermetic:nccl_configure.bzl",
#     "nccl_configure",
# )




def _extension_for_cuda_repo_impl(ctx):
  cuda_redist_init_repositories(
      cuda_redistributions = CUDA_REDISTRIBUTIONS,
  )
  cudnn_redist_init_repository(
      cudnn_redistributions = CUDNN_REDISTRIBUTIONS,
  )

  # nccl_configure(name = "local_config_nccl")

  # cuda_configure(name = "local_config_cuda")

  # CUDA_REPOS = [
  #   "cuda_cccl",
  #   "cuda_cublas",
  #   "cuda_cudart",
  #   "cuda_cupti",
  #   "cuda_nvjitlink",
  #   "cuda_nvml",
  #   "cuda_nvcc",
  #   "cuda_curand",
  #   "cuda_cusparse",
  #   "cuda_cufft",
  #   "cuda_cusolver",
  #   "cuda_nvtx"
  # ]
  # for repo in CUDA_REPOS:
  #   cuda_repo(
  #     name = repo,
  #     url_dict = {  },
  #     versions = [
  #       "12,11"
  #     ],
  #     build_templates = [
  #       "@tsl//third_party/gpus/cuda/hermetic:"+repo+".BUILD.tpl"
  #     ],
  #     cuda_redist_path_prefix = "https://developer.download.nvidia.com/compute/cuda/redist/",
  #   )
# -- repo definitions -- #

extension_for_cuda_repo = module_extension(implementation = _extension_for_cuda_repo_impl)
