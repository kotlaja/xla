#load("@tsl//third_party:repo.bzl", "tf_http_archive", "tf_mirror_urls")
load("//third_party:repo.bzl", "tf_http_archive", "tf_mirror_urls")
load("//third_party/stablehlo:workspace.bzl", stablehlo = "repo")
load("//third_party/triton:workspace.bzl", triton = "repo")
load("//third_party/absl:workspace.bzl", absl = "repo")
load("//third_party/eigen3:workspace.bzl", eigen = "repo")
load("//third_party/gloo:workspace.bzl", gloo = "repo")
load("//third_party/farmhash:workspace.bzl", farmhash_archive = "repo")
load("//third_party/hwloc:workspace.bzl", hwloc = "repo")
load("//third_party/shardy:workspace.bzl", shardy = "repo")
load("//third_party/mpitrampoline:workspace.bzl", mpitrampoline = "repo")
load("//third_party/nanobind:workspace.bzl", nanobind = "repo")
load("//third_party/robin_map:workspace.bzl", robin_map = "repo")
load("//third_party/dlpack:workspace.bzl", dlpack = "repo")
load("//third_party/ducc:workspace.bzl", ducc = "repo")
load("//third_party/implib_so:workspace.bzl", implib_so = "repo")
load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")
load("@bazel_tools//tools/build_defs/repo:utils.bzl", "maybe")
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
      # Use the commit on 2025/6/09:
      # https://github.com/google/googletest/commit/28e9d1f26771c6517c3b4be10254887673c94018
      sha256 = "f253ca1a07262f8efde8328e4b2c68979e40ddfcfc001f70d1d5f612c7de2974",
      strip_prefix = "googletest-28e9d1f26771c6517c3b4be10254887673c94018",
      # Patch googletest to:
      #   - avoid dependencies on @fuchsia_sdk,
      #   - refer to re2 as @com_googlesource_code_re2,
      #   - refer to abseil as @com_google_absl.
      #
      # To update the patch, run:
      # $ cd ~
      # $ mkdir -p github
      # $ cd github
      # $ git clone https://github.com/google/googletest.git
      # $ cd googletest
      # $ git checkout 28e9d1f26771c6517c3b4be10254887673c94018
      # ... make local changes to googletest ...
      # $ git diff > <client-root>/third_party/tensorflow/third_party/googletest/googletest.patch
      #
      # The patch path is relative to third_party/xla.
      patch_file = ["//third_party/googletest:googletest.patch"],
      urls = tf_mirror_urls("https://github.com/google/googletest/archive/28e9d1f26771c6517c3b4be10254887673c940189.zip"),
  )

  tf_http_archive(
      name = "com_googlesource_code_re2",
      sha256 = "ef516fb84824a597c4d5d0d6d330daedb18363b5a99eda87d027e6bdd9cba299",
      strip_prefix = "re2-03da4fc0857c285e3a26782f6bc8931c4c950df4",
      system_build_file = "//third_party/systemlibs:re2.BUILD",
      urls = tf_mirror_urls("https://github.com/google/re2/archive/03da4fc0857c285e3a26782f6bc8931c4c950df4.tar.gz"),
  )
  
  tf_http_archive(
      name = "onednn",
      build_file = "//third_party/mkl_dnn:mkldnn_v1.BUILD",
      patch_file = ["//third_party/mkl_dnn:setting_init.patch"],
      sha256 = "071f289dc961b43a3b7c8cbe8a305290a7c5d308ec4b2f586397749abdc88296",
      strip_prefix = "oneDNN-3.7.3",
      urls = tf_mirror_urls("https://github.com/oneapi-src/oneDNN/archive/refs/tags/v3.7.3.tar.gz"),
  )

  # Intel openMP that is part of LLVM sources.
  tf_http_archive(
      name = "llvm_openmp",
      build_file = "//third_party/llvm_openmp:BUILD.bazel",
      patch_file = ["//third_party/llvm_openmp:openmp_switch_default_patch.patch"],
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
      system_build_file = "//third_party/systemlibs:jsoncpp.BUILD",
      urls = tf_mirror_urls("https://github.com/open-source-parsers/jsoncpp/archive/1.9.5.tar.gz"),
  )

  # TODO: Move it to a module when it becomes available in BCR.
  tf_http_archive(
      name = "pybind11",
      urls = tf_mirror_urls("https://github.com/pybind/pybind11/archive/v2.13.4.tar.gz"),
      sha256 = "efc901aa0aab439a3fea6efeaf930b5a349fb06394bf845c64ce15a9cf8f0240",
      strip_prefix = "pybind11-2.13.4",
      build_file = "//third_party:pybind11.BUILD",
      system_build_file = "//third_party/systemlibs:pybind11.BUILD",
  )


  tf_http_archive(
      name = "pthreadpool",
      sha256 = "cb668c32d6e05099492cc7ea19168e2dad0d1dcc4cbaa0e34fd4b38d39f0e03e",
      strip_prefix = "pthreadpool-f94ab76fe99754960035d520dce28e15b647e8cf",
      urls = tf_mirror_urls("https://github.com/Maratyszcza/pthreadpool/archive/f94ab76fe99754960035d520dce28e15b647e8cf.zip"),
  )

  tf_http_archive(
    name = "com_github_nelhage_rules_boost",
    sha256 = "feb4b1294684c79df7c1e08f1aec5da0da52021e33db59c88edbe86b4d1a017a",
    urls = [
      "https://storage.googleapis.com/mirror.tensorflow.org/github.com/nelhage/rules_boost/archive/5160325dbdc8c9e499f9d9917d913f35f1785d52.zip",
      "https://github.com/nelhage/rules_boost/archive/5160325dbdc8c9e499f9d9917d913f35f1785d52.zip"
    ],
    strip_prefix = "rules_boost-5160325dbdc8c9e499f9d9917d913f35f1785d52",
  )

  maybe(
      http_archive,
      name = "boost",
      build_file = "@com_github_nelhage_rules_boost//:boost.BUILD",
      patch_cmds = ["rm -f doc/pdf/BUILD"],
      patch_cmds_win = ["Remove-Item -Force doc/pdf/BUILD"],
      url = "https://github.com/boostorg/boost/releases/download/boost-1.84.0/boost-1.84.0.tar.gz",
      sha256 = "4d27e9efed0f6f152dc28db6430b9d3dfb40c0345da7342eaa5a987dde57bd95",
      strip_prefix = "boost-1.84.0",
  )

  # Can be added as bazel_dep(name = "bzip2", version = "1.0.8", repo_name = "org_bzip_bzip2")
  # Issue is build_file
  maybe(
      http_archive,
      name = "org_bzip_bzip2",
      build_file = "@com_github_nelhage_rules_boost//:bzip2.BUILD",
      sha256 = "ab5a03176ee106d3f0fa90e381da478ddae405918153cca248e682cd0c4a2269",
      strip_prefix = "bzip2-1.0.8",
      urls = [
          "https://mirror.bazel.build/sourceware.org/pub/bzip2/bzip2-1.0.8.tar.gz",
          "https://sourceware.org/pub/bzip2/bzip2-1.0.8.tar.gz",
      ],
  )

  http_archive(
    name = "org_lzma_lzma",
    url = "https://src.fedoraproject.org/lookaside/extras/xz/xz-5.4.6.tar.gz/sha512/b08a61d8d478d3b4675cb1ddacdbbd98dc6941a55bcdd81a28679e54e9367d3a595fa123ac97874a17da571c1b712e2a3e901c2737099a9d268616a1ba3de497/xz-5.4.6.tar.gz",
    sha256 = "aeba3e03bf8140ddedf62a0a367158340520f6b384f75ca6045ccc6c0d43fd5c",
    strip_prefix = "xz-5.4.6",
    build_file = "@com_github_nelhage_rules_boost//:lzma.BUILD",
  )

  # Higher version of org_lzma_lzma
  # http_archive(
  #   name = "org_lzma_lzma",
  #   url = "https://src.fedoraproject.org/lookaside/extras/xz/xz-5.6.1.tar.gz/sha512/8af100eb83288f032e4813be2bf8de7d733c8761f77f078776c1391709241ad8fe3192d107664786e2543677915c5eeb3fe7add5c53b48b50c10a9de7c9f4fda/xz-5.6.1.tar.gz",
  #   sha256 = "2398f4a8e53345325f44bdd9f0cc7401bd9025d736c6d43b372f4dea77bf75b8",
  #   strip_prefix = "xz-5.6.1",
  #   build_file = "@com_github_nelhage_rules_boost//:lzma.BUILD",
  # )
# -- repo definitions -- #

extension_for_tf_http_archive = module_extension(implementation = _extension_for_tf_http_archive_impl)
