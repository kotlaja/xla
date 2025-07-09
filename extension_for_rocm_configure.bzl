load("//third_party/gpus:rocm_configure.bzl", "rocm_configure")
# -- load statements -- #

def _extension_for_rocm_configure_impl(ctx):
  rocm_configure(
    name = "local_config_rocm",
  )
# -- repo definitions -- #

extension_for_rocm_configure = module_extension(implementation = _extension_for_rocm_configure_impl)
