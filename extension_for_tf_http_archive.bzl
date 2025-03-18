#load("@tsl//third_party:repo.bzl", "tf_http_archive", "tf_mirror_urls")
load("//third_party:repo.bzl", "tf_http_archive", "tf_mirror_urls")
load("//third_party/stablehlo:workspace.bzl", stablehlo = "repo")
load("//third_party/triton:workspace.bzl", triton = "repo")
load("//third_party/tsl/third_party/absl:workspace.bzl", absl = "repo")
load("//third_party/tsl/third_party/eigen3:workspace.bzl", eigen = "repo")
load("//third_party/gloo:workspace.bzl", gloo = "repo")
load("//third_party/tsl/third_party/farmhash:workspace.bzl", farmhash_archive = "repo")
load("@tsl//third_party/hwloc:workspace.bzl", hwloc = "repo")
load("//third_party/shardy:workspace.bzl", shardy = "repo")
load("//third_party/mpitrampoline:workspace.bzl", mpitrampoline = "repo")
load("//third_party/nanobind:workspace.bzl", nanobind = "repo")
load("//third_party/robin_map:workspace.bzl", robin_map = "repo")
load("//third_party/dlpack:workspace.bzl", dlpack = "repo")
load("@tsl//third_party/ducc:workspace.bzl", ducc = "repo")
load("@tsl//third_party/implib_so:workspace.bzl", implib_so = "repo")
# -- load statements -- #

def _extension_for_tf_http_archive_impl(ctx):

  stablehlo()
  triton()
  absl()
  eigen()
  gloo()
  farmhash_archive()
  hwloc()
  shardy()
  mpitrampoline()
  nanobind()
  robin_map()
  dlpack()
  ducc()
  implib_so()

  tf_http_archive(
    name = "ml_dtypes_py",
    sha256 = "f6e5880666661351e6cd084ac4178ddc4dabcde7e9a73722981c0d1500cf5937",
    urls = [
      "https://storage.googleapis.com/mirror.tensorflow.org/github.com/jax-ml/ml_dtypes/archive/00d98cd92ade342fef589c0470379abb27baebe9/ml_dtypes-00d98cd92ade342fef589c0470379abb27baebe9.tar.gz",
      "https://github.com/jax-ml/ml_dtypes/archive/00d98cd92ade342fef589c0470379abb27baebe9/ml_dtypes-00d98cd92ade342fef589c0470379abb27baebe9.tar.gz"
    ],
    strip_prefix = "ml_dtypes-00d98cd92ade342fef589c0470379abb27baebe9",
    build_file = "//third_party/py/ml_dtypes:ml_dtypes_py.BUILD",
    link_files = {
      "//third_party/py/ml_dtypes:ml_dtypes.BUILD": "ml_dtypes/BUILD.bazel"
    },
  )

  tf_http_archive(
      name = "com_google_googletest",
      sha256 = "81964fe578e9bd7c94dfdb09c8e4d6e6759e19967e397dbea48d1c10e45d0df2",
      strip_prefix = "googletest-release-1.12.1",
      urls = tf_mirror_urls("https://github.com/google/googletest/archive/refs/tags/release-1.12.1.tar.gz"),
  )

  tf_http_archive(
      name = "com_googlesource_code_re2",
      sha256 = "ef516fb84824a597c4d5d0d6d330daedb18363b5a99eda87d027e6bdd9cba299",
      strip_prefix = "re2-03da4fc0857c285e3a26782f6bc8931c4c950df4",
      system_build_file = "@tsl//third_party/systemlibs:re2.BUILD",
      urls = tf_mirror_urls("https://github.com/google/re2/archive/03da4fc0857c285e3a26782f6bc8931c4c950df4.tar.gz"),
  )
  
  tf_http_archive(
      name = "onednn",
      build_file = "@tsl//third_party/mkl_dnn:mkldnn_v1.BUILD",
      sha256 = "8356aa9befde4d4ff93f1b016ac4310730b2de0cc0b8c6c7ce306690bc0d7b43",
      strip_prefix = "oneDNN-3.5",
      urls = tf_mirror_urls("https://github.com/oneapi-src/oneDNN/archive/refs/tags/v3.5.tar.gz"),
  )

  tf_http_archive(
        name = "llvm_openmp",
        build_file = "@tsl//third_party/llvm_openmp:BUILD",
        patch_file = ["@tsl//third_party/llvm_openmp:openmp_switch_default_patch.patch"],
        sha256 = "d19f728c8e04fb1e94566c8d76aef50ec926cd2f95ef3bf1e0a5de4909b28b44",
        strip_prefix = "openmp-10.0.1.src",
        urls = tf_mirror_urls("https://github.com/llvm/llvm-project/releases/download/llvmorg-10.0.1/openmp-10.0.1.src.tar.xz"),
  )

  # LINT.IfChange
  tf_http_archive(
      name = "XNNPACK",
      sha256 = "face04056299ca22e2dbbf122a27aef289443dc7b1ad7e33a52714d6acc084eb",
      strip_prefix = "XNNPACK-e55b3998cadb320188759aaada27328cbacc3253",
      urls = tf_mirror_urls("https://github.com/google/XNNPACK/archive/e55b3998cadb320188759aaada27328cbacc3253.zip"),
  )
  # LINT.ThenChange(//tensorflow/lite/tools/cmake/modules/xnnpack.cmake)

  tf_http_archive(
      name = "jsoncpp_git",
      sha256 = "f409856e5920c18d0c2fb85276e24ee607d2a09b5e7d5f0a371368903c275da2",
      strip_prefix = "jsoncpp-1.9.5",
      system_build_file = "@tsl//third_party/systemlibs:jsoncpp.BUILD",
      urls = tf_mirror_urls("https://github.com/open-source-parsers/jsoncpp/archive/1.9.5.tar.gz"),
  )

  # TODO: Move it to a module when it becomes available in BCR.
  tf_http_archive(
      name = "pybind11",
      urls = tf_mirror_urls("https://github.com/pybind/pybind11/archive/v2.13.4.tar.gz"),
      sha256 = "efc901aa0aab439a3fea6efeaf930b5a349fb06394bf845c64ce15a9cf8f0240",
      strip_prefix = "pybind11-2.13.4",
      build_file = "@tsl//third_party:pybind11.BUILD",
      system_build_file = "@tsl//third_party/systemlibs:pybind11.BUILD",
  )


  tf_http_archive(
      name = "pthreadpool",
      sha256 = "cb668c32d6e05099492cc7ea19168e2dad0d1dcc4cbaa0e34fd4b38d39f0e03e",
      strip_prefix = "pthreadpool-f94ab76fe99754960035d520dce28e15b647e8cf",
      urls = tf_mirror_urls("https://github.com/Maratyszcza/pthreadpool/archive/f94ab76fe99754960035d520dce28e15b647e8cf.zip"),
  )

# -- repo definitions -- #

extension_for_tf_http_archive = module_extension(implementation = _extension_for_tf_http_archive_impl)
