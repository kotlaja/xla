load("//third_party/tensorrt:tensorrt_configure.bzl", "tensorrt_configure")
# -- load statements -- #

def _extension_for_tensorrt_configure_impl(ctx):
  tensorrt_configure(
    name = "local_config_tensorrt",
  )
# -- repo definitions -- #

extension_for_tensorrt_configure = module_extension(implementation = _extension_for_tensorrt_configure_impl)
