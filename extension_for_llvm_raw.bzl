load("//third_party/llvm:workspace.bzl", llvm = "repo")
# -- load statements -- #

def _extension_for_llvm_raw_impl(ctx):
  # Load the raw llvm-project.  llvm does not have build rules set up by default,
  # but provides a script for setting up build rules via overlays.
  llvm("llvm-raw")


extension_for_llvm_raw = module_extension(implementation = _extension_for_llvm_raw_impl)