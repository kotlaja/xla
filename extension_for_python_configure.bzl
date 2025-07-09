load("//third_party/py:python_configure.bzl", "python_configure")
# -- load statements -- #

def _extension_for_python_configure_impl(ctx):
  python_configure(
    name = "local_config_python",
  )
# -- repo definitions -- #

extension_for_python_configure = module_extension(implementation = _extension_for_python_configure_impl)
