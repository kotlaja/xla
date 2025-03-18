load("//third_party/llvm:setup.bzl", "llvm_setup")
# -- load statements -- #

def _extension_for_llvm_project_impl(ctx):
  llvm_setup(name = "llvm-project")

extension_for_llvm_project = module_extension(implementation = _extension_for_llvm_project_impl)