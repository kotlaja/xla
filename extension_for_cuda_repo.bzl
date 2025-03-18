load("@tsl//third_party/gpus/cuda/hermetic:cuda_redist_init_repositories.bzl", "cuda_repo")
# -- load statements -- #

def _extension_for_cuda_repo_impl(ctx):
  CUDA_REPOS = [
    "cuda_cccl",
    "cuda_cublas",
    "cuda_cudart",
    "cuda_cupti",
    "cuda_nvjitlink",
    "cuda_nvml",
    "cuda_nvcc",
    "cuda_curand",
    "cuda_cusparse",
    "cuda_cufft",
    "cuda_cusolver",
    "cuda_nvtx"
  ]
  for repo in CUDA_REPOS:
    cuda_repo(
      name = repo,
      url_dict = {  },
      versions = [
        "12,11"
      ],
      build_templates = [
        "@tsl//third_party/gpus/cuda/hermetic:"+repo+".BUILD.tpl"
      ],
      cuda_redist_path_prefix = "https://developer.download.nvidia.com/compute/cuda/redist/",
    )
# -- repo definitions -- #

extension_for_cuda_repo = module_extension(implementation = _extension_for_cuda_repo_impl)
