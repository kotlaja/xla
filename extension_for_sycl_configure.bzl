load("//third_party/gpus:sycl_configure.bzl", "sycl_configure")
# -- load statements -- #

def _extension_for_sycl_configure_impl(ctx):
  sycl_configure(
    name = "local_config_sycl",
  )
# -- repo definitions -- #

extension_for_sycl_configure = module_extension(implementation = _extension_for_sycl_configure_impl)
