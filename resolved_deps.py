resolved = [
     {
          "original_rule_class": "local_repository",
          "original_attributes": {
               "name": "bazel_tools",
               "path": "/usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/install/bd3f2062f72dd67fde166eda94178459/embedded_tools"
          },
          "native": "local_repository(name = \"bazel_tools\", path = __embedded_dir__ + \"/\" + \"embedded_tools\")"
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository rules_python instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:14:18: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/third_party/py/python_init_rules.bzl:6:17: in python_init_rules\nRepository rule http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/http.bzl:387:31: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_python",
               "generator_name": "rules_python",
               "generator_function": "python_init_rules",
               "generator_location": None,
               "url": "https://github.com/bazelbuild/rules_python/releases/download/0.39.0/rules_python-0.39.0.tar.gz",
               "sha256": "62ddebb766b4d6ddf1712f753dac5740bea072646f630eb9982caa09ad8a7687",
               "strip_prefix": "rules_python-0.39.0",
               "patches": [
                    "//third_party/py:rules_python.patch"
               ],
               "patch_args": [
                    "-p1"
               ]
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://github.com/bazelbuild/rules_python/releases/download/0.39.0/rules_python-0.39.0.tar.gz",
                         "urls": [],
                         "sha256": "62ddebb766b4d6ddf1712f753dac5740bea072646f630eb9982caa09ad8a7687",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "rules_python-0.39.0",
                         "add_prefix": "",
                         "type": "",
                         "patches": [
                              "//third_party/py:rules_python.patch"
                         ],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p1"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "rules_python"
                    },
                    "output_tree_hash": "4314f4c1dbea0bf1a781dd64e3590f64a984f9b194144affd4ce385a09ae0df5"
               }
          ]
     },
     {
          "original_rule_class": "//third_party/py:python_repo.bzl%python_repository",
          "definition_information": "Repository python_version_repo instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:18:25: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/third_party/py/python_init_repositories.bzl:13:22: in python_init_repositories\nRepository rule python_repository defined at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/third_party/py/python_repo.bzl:209:36: in <toplevel>\n",
          "original_attributes": {
               "name": "python_version_repo",
               "generator_name": "python_version_repo",
               "generator_function": "python_init_repositories",
               "generator_location": None,
               "requirements_versions": [
                    "3.11"
               ],
               "requirements_locks": [
                    "//:requirements_lock_3_11.txt"
               ],
               "local_wheel_workspaces": [],
               "local_wheel_inclusion_list": [
                    "*"
               ],
               "local_wheel_exclusion_list": []
          },
          "repositories": [
               {
                    "rule_class": "//third_party/py:python_repo.bzl%python_repository",
                    "attributes": {
                         "name": "python_version_repo",
                         "generator_name": "python_version_repo",
                         "generator_function": "python_init_repositories",
                         "generator_location": None,
                         "requirements_versions": [
                              "3.11"
                         ],
                         "requirements_locks": [
                              "//:requirements_lock_3_11.txt"
                         ],
                         "local_wheel_workspaces": [],
                         "local_wheel_inclusion_list": [
                              "*"
                         ],
                         "local_wheel_exclusion_list": []
                    },
                    "output_tree_hash": "528656017552b70c05198e75f64029560c8d6ec018da669ccfb427d77b7add3a"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_python//python/private:internal_config_repo.bzl%internal_config_repo",
          "definition_information": "Repository rules_python_internal instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:18:25: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/third_party/py/python_init_repositories.bzl:23:20: in python_init_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_python/python/private/py_repositories.bzl:33:10: in py_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\nRepository rule internal_config_repo defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_python/python/private/internal_config_repo.bzl:108:39: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_python_internal",
               "generator_name": "rules_python_internal",
               "generator_function": "python_init_repositories",
               "generator_location": None
          },
          "repositories": [
               {
                    "rule_class": "@@rules_python//python/private:internal_config_repo.bzl%internal_config_repo",
                    "attributes": {
                         "name": "rules_python_internal",
                         "generator_name": "rules_python_internal",
                         "generator_function": "python_init_repositories",
                         "generator_location": None
                    },
                    "output_tree_hash": "ffdec66b8b1e449fdc8b40bddcaf5d49bd385780897d6486833127a21203f617"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_python//python/private:toolchains_repo.bzl%toolchain_aliases",
          "definition_information": "Repository python instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:26:23: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/third_party/py/python_init_toolchains.bzl:60:35: in python_init_toolchains\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_python/python/private/python_register_toolchains.bzl:165:22: in python_register_toolchains\nRepository rule toolchain_aliases defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_python/python/private/toolchains_repo.bzl:224:36: in <toplevel>\n",
          "original_attributes": {
               "name": "python",
               "generator_name": "python",
               "generator_function": "python_init_toolchains",
               "generator_location": None,
               "platforms": [
                    "aarch64-apple-darwin",
                    "aarch64-unknown-linux-gnu",
                    "ppc64le-unknown-linux-gnu",
                    "s390x-unknown-linux-gnu",
                    "x86_64-apple-darwin",
                    "x86_64-pc-windows-msvc",
                    "x86_64-unknown-linux-gnu"
               ],
               "python_version": "3.11.10",
               "user_repository_name": "python"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_python//python/private:toolchains_repo.bzl%toolchain_aliases",
                    "attributes": {
                         "name": "python",
                         "generator_name": "python",
                         "generator_function": "python_init_toolchains",
                         "generator_location": None,
                         "platforms": [
                              "aarch64-apple-darwin",
                              "aarch64-unknown-linux-gnu",
                              "ppc64le-unknown-linux-gnu",
                              "s390x-unknown-linux-gnu",
                              "x86_64-apple-darwin",
                              "x86_64-pc-windows-msvc",
                              "x86_64-unknown-linux-gnu"
                         ],
                         "python_version": "3.11.10",
                         "user_repository_name": "python"
                    },
                    "output_tree_hash": "b39fd5631a323155f6c8c696302249f6c7d9049e4d2ed4220230392ce08c7883"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository bazel_skylib instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:18:25: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/third_party/py/python_init_repositories.bzl:23:20: in python_init_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_python/python/private/py_repositories.bzl:48:17: in py_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_python/python/private/py_repositories.bzl:25:10: in http_archive\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\nRepository rule http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/http.bzl:387:31: in <toplevel>\n",
          "original_attributes": {
               "name": "bazel_skylib",
               "generator_name": "bazel_skylib",
               "generator_function": "python_init_repositories",
               "generator_location": None,
               "urls": [
                    "https://mirror.bazel.build/github.com/bazelbuild/bazel-skylib/releases/download/1.3.0/bazel-skylib-1.3.0.tar.gz",
                    "https://github.com/bazelbuild/bazel-skylib/releases/download/1.3.0/bazel-skylib-1.3.0.tar.gz"
               ],
               "sha256": "74d544d96f4a5bb630d465ca8bbcfe231e3594e5aae57e1edbf17a6eb3ca2506"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://mirror.bazel.build/github.com/bazelbuild/bazel-skylib/releases/download/1.3.0/bazel-skylib-1.3.0.tar.gz",
                              "https://github.com/bazelbuild/bazel-skylib/releases/download/1.3.0/bazel-skylib-1.3.0.tar.gz"
                         ],
                         "sha256": "74d544d96f4a5bb630d465ca8bbcfe231e3594e5aae57e1edbf17a6eb3ca2506",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "bazel_skylib"
                    },
                    "output_tree_hash": "ea7c4298620705f0369110da5db3dec89df5ed43983fc85435f336e5fb95b3f9"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository rules_cc instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:18:25: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/third_party/py/python_init_repositories.bzl:23:20: in python_init_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_python/python/private/py_repositories.bzl:56:17: in py_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_python/python/private/py_repositories.bzl:25:10: in http_archive\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\nRepository rule http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/http.bzl:387:31: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_cc",
               "generator_name": "rules_cc",
               "generator_function": "python_init_repositories",
               "generator_location": None,
               "urls": [
                    "https://github.com/bazelbuild/rules_cc/releases/download/0.0.13/rules_cc-0.0.13.tar.gz"
               ],
               "sha256": "d9bdd3ec66b6871456ec9c965809f43a0901e692d754885e89293807762d3d80",
               "strip_prefix": "rules_cc-0.0.13"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/bazelbuild/rules_cc/releases/download/0.0.13/rules_cc-0.0.13.tar.gz"
                         ],
                         "sha256": "d9bdd3ec66b6871456ec9c965809f43a0901e692d754885e89293807762d3d80",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "rules_cc-0.0.13",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "rules_cc"
                    },
                    "output_tree_hash": "1f6270850c5700968827fef8b932ed0249a6276af734f539b05a1bd7824e47a8"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_python//python/private/pypi:pip_repository.bzl%pip_repository",
          "definition_information": "Repository pypi instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:30:16: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/third_party/py/python_init_pip.bzl:29:14: in python_init_pip\nRepository rule pip_repository defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_python/python/private/pypi/pip_repository.bzl:222:33: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi",
               "generator_name": "pypi",
               "generator_function": "python_init_pip",
               "generator_location": None,
               "annotations": {
                    "numpy": "{\"additive_build_content\":\"cc_library(\\n    name = \\\"numpy_headers_2\\\",\\n    hdrs = glob([\\\"site-packages/numpy/_core/include/**/*.h\\\"]),\\n    strip_include_prefix=\\\"site-packages/numpy/_core/include/\\\",\\n)\\ncc_library(\\n    name = \\\"numpy_headers_1\\\",\\n    hdrs = glob([\\\"site-packages/numpy/core/include/**/*.h\\\"]),\\n    strip_include_prefix=\\\"site-packages/numpy/core/include/\\\",\\n)\\ncc_library(\\n    name = \\\"numpy_headers\\\",\\n    deps = [\\\":numpy_headers_2\\\", \\\":numpy_headers_1\\\"],\\n)\\n\",\"copy_executables\":{},\"copy_files\":{},\"data\":[],\"data_exclude_glob\":[],\"srcs_exclude_glob\":[]}"
               },
               "requirements_lock": "//:requirements_lock_3_11.txt",
               "python_interpreter_target": "@@python_x86_64-unknown-linux-gnu//:bin/python3"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_python//python/private/pypi:pip_repository.bzl%pip_repository",
                    "attributes": {
                         "name": "pypi",
                         "generator_name": "pypi",
                         "generator_function": "python_init_pip",
                         "generator_location": None,
                         "annotations": {
                              "numpy": "{\"additive_build_content\":\"cc_library(\\n    name = \\\"numpy_headers_2\\\",\\n    hdrs = glob([\\\"site-packages/numpy/_core/include/**/*.h\\\"]),\\n    strip_include_prefix=\\\"site-packages/numpy/_core/include/\\\",\\n)\\ncc_library(\\n    name = \\\"numpy_headers_1\\\",\\n    hdrs = glob([\\\"site-packages/numpy/core/include/**/*.h\\\"]),\\n    strip_include_prefix=\\\"site-packages/numpy/core/include/\\\",\\n)\\ncc_library(\\n    name = \\\"numpy_headers\\\",\\n    deps = [\\\":numpy_headers_2\\\", \\\":numpy_headers_1\\\"],\\n)\\n\",\"copy_executables\":{},\"copy_files\":{},\"data\":[],\"data_exclude_glob\":[],\"srcs_exclude_glob\":[]}"
                         },
                         "requirements_lock": "//:requirements_lock_3_11.txt",
                         "python_interpreter_target": "@@python_x86_64-unknown-linux-gnu//:bin/python3"
                    },
                    "output_tree_hash": "8df574a6cd7e6f3bfad5f631658a42d09289aa5c6824055318c19648b67b6182"
               }
          ]
     },
     {
          "original_rule_class": "//third_party:repo.bzl%tf_vendored",
          "definition_information": "Repository tsl instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:38:15: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace4.bzl:9:16: in workspace\nRepository rule tf_vendored defined at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/third_party/repo.bzl:156:30: in <toplevel>\n",
          "original_attributes": {
               "name": "tsl",
               "generator_name": "tsl",
               "generator_function": "workspace",
               "generator_location": None,
               "relpath": "third_party/tsl"
          },
          "repositories": [
               {
                    "rule_class": "//third_party:repo.bzl%tf_vendored",
                    "attributes": {
                         "name": "tsl",
                         "generator_name": "tsl",
                         "generator_function": "workspace",
                         "generator_location": None,
                         "relpath": "third_party/tsl"
                    },
                    "output_tree_hash": "23386f5b72062df95191eada1e783d6cb98f1bd9b128d33488b1e58499f32373"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository io_bazel_rules_closure instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:42:15: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace3.bzl:12:17: in workspace\nRepository rule http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/http.bzl:387:31: in <toplevel>\n",
          "original_attributes": {
               "name": "io_bazel_rules_closure",
               "generator_name": "io_bazel_rules_closure",
               "generator_function": "workspace",
               "generator_location": None,
               "urls": [
                    "https://storage.googleapis.com/mirror.tensorflow.org/github.com/bazelbuild/rules_closure/archive/308b05b2419edb5c8ee0471b67a40403df940149.tar.gz",
                    "https://github.com/bazelbuild/rules_closure/archive/308b05b2419edb5c8ee0471b67a40403df940149.tar.gz"
               ],
               "sha256": "5b00383d08dd71f28503736db0500b6fb4dda47489ff5fc6bed42557c07c6ba9",
               "strip_prefix": "rules_closure-308b05b2419edb5c8ee0471b67a40403df940149"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://storage.googleapis.com/mirror.tensorflow.org/github.com/bazelbuild/rules_closure/archive/308b05b2419edb5c8ee0471b67a40403df940149.tar.gz",
                              "https://github.com/bazelbuild/rules_closure/archive/308b05b2419edb5c8ee0471b67a40403df940149.tar.gz"
                         ],
                         "sha256": "5b00383d08dd71f28503736db0500b6fb4dda47489ff5fc6bed42557c07c6ba9",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "rules_closure-308b05b2419edb5c8ee0471b67a40403df940149",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "io_bazel_rules_closure"
                    },
                    "output_tree_hash": "b3bf45dbab21f41a3457b69d8263658e6792964275a63410e09e5f67de241456"
               }
          ]
     },
     {
          "original_rule_class": "@@tsl//third_party:repo.bzl%_tf_http_archive",
          "definition_information": "Repository llvm-raw instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:42:15: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace3.bzl:10:19: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace3.bzl:47:9: in workspace\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/llvm/workspace.bzl:10:20: in repo\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/repo.bzl:136:21: in tf_http_archive\nRepository rule _tf_http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/repo.bzl:89:35: in <toplevel>\n",
          "original_attributes": {
               "name": "llvm-raw",
               "generator_name": "llvm-raw",
               "generator_function": "workspace",
               "generator_location": None,
               "sha256": "9eeaef49e6a305e5f540f656ef851d80074476180963b5413c38c751f0e1339f",
               "urls": [
                    "https://storage.googleapis.com/mirror.tensorflow.org/github.com/llvm/llvm-project/archive/5586541d220ebbe27d8dea039d0165c3b2694b06.tar.gz",
                    "https://github.com/llvm/llvm-project/archive/5586541d220ebbe27d8dea039d0165c3b2694b06.tar.gz"
               ],
               "strip_prefix": "llvm-project-5586541d220ebbe27d8dea039d0165c3b2694b06",
               "patch_file": [
                    "//third_party/llvm:generated.patch",
                    "//third_party/llvm:build.patch",
                    "//third_party/llvm:mathextras.patch",
                    "//third_party/llvm:toolchains.patch",
                    "//third_party/llvm:zstd.patch"
               ],
               "build_file": "//third_party/llvm:llvm.BUILD",
               "link_files": {
                    "//third_party/llvm:run_lit.sh": "mlir/run_lit.sh"
               }
          },
          "repositories": [
               {
                    "rule_class": "@@tsl//third_party:repo.bzl%_tf_http_archive",
                    "attributes": {
                         "name": "llvm-raw",
                         "generator_name": "llvm-raw",
                         "generator_function": "workspace",
                         "generator_location": None,
                         "sha256": "9eeaef49e6a305e5f540f656ef851d80074476180963b5413c38c751f0e1339f",
                         "urls": [
                              "https://storage.googleapis.com/mirror.tensorflow.org/github.com/llvm/llvm-project/archive/5586541d220ebbe27d8dea039d0165c3b2694b06.tar.gz",
                              "https://github.com/llvm/llvm-project/archive/5586541d220ebbe27d8dea039d0165c3b2694b06.tar.gz"
                         ],
                         "strip_prefix": "llvm-project-5586541d220ebbe27d8dea039d0165c3b2694b06",
                         "patch_file": [
                              "//third_party/llvm:generated.patch",
                              "//third_party/llvm:build.patch",
                              "//third_party/llvm:mathextras.patch",
                              "//third_party/llvm:toolchains.patch",
                              "//third_party/llvm:zstd.patch"
                         ],
                         "build_file": "//third_party/llvm:llvm.BUILD",
                         "link_files": {
                              "//third_party/llvm:run_lit.sh": "mlir/run_lit.sh"
                         }
                    },
                    "output_tree_hash": "a802d40109cbd69fa8e2374558fc72c10bbba78f5a3cc5c983ceb7fc47b17d5b"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository rules_pkg instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:42:15: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace3.bzl:32:17: in workspace\nRepository rule http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/http.bzl:387:31: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_pkg",
               "generator_name": "rules_pkg",
               "generator_function": "workspace",
               "generator_location": None,
               "urls": [
                    "https://mirror.bazel.build/github.com/bazelbuild/rules_pkg/releases/download/0.7.1/rules_pkg-0.7.1.tar.gz",
                    "https://github.com/bazelbuild/rules_pkg/releases/download/0.7.1/rules_pkg-0.7.1.tar.gz"
               ],
               "sha256": "451e08a4d78988c06fa3f9306ec813b836b1d076d0f055595444ba4ff22b867f"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://mirror.bazel.build/github.com/bazelbuild/rules_pkg/releases/download/0.7.1/rules_pkg-0.7.1.tar.gz",
                              "https://github.com/bazelbuild/rules_pkg/releases/download/0.7.1/rules_pkg-0.7.1.tar.gz"
                         ],
                         "sha256": "451e08a4d78988c06fa3f9306ec813b836b1d076d0f055595444ba4ff22b867f",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "rules_pkg"
                    },
                    "output_tree_hash": "6eb97b6f5cc63a47d02df7339c021530a960a51ef62b390f1d1e2e70059522c7"
               }
          ]
     },
     {
          "original_rule_class": "@@tsl//third_party:repo.bzl%_tf_http_archive",
          "definition_information": "Repository com_github_grpc_grpc instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:46:15: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace2.bzl:164:19: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:604:21: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:331:20: in _tf_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/repo.bzl:136:21: in tf_http_archive\nRepository rule _tf_http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/repo.bzl:89:35: in <toplevel>\n",
          "original_attributes": {
               "name": "com_github_grpc_grpc",
               "generator_name": "com_github_grpc_grpc",
               "generator_function": "workspace",
               "generator_location": None,
               "sha256": "b956598d8cbe168b5ee717b5dafa56563eb5201a947856a6688bbeac9cac4e1f",
               "urls": [
                    "https://storage.googleapis.com/mirror.tensorflow.org/github.com/grpc/grpc/archive/b54a5b338637f92bfcf4b0bc05e0f57a5fd8fadd.tar.gz",
                    "https://github.com/grpc/grpc/archive/b54a5b338637f92bfcf4b0bc05e0f57a5fd8fadd.tar.gz"
               ],
               "strip_prefix": "grpc-b54a5b338637f92bfcf4b0bc05e0f57a5fd8fadd",
               "patch_file": [
                    "@tsl//third_party/grpc:generate_cc_env_fix.patch",
                    "@tsl//third_party/grpc:register_go_toolchain.patch"
               ],
               "system_build_file": "@tsl//third_party/systemlibs:grpc.BUILD",
               "system_link_files": {
                    "@tsl//third_party/systemlibs:BUILD": "bazel/BUILD",
                    "@tsl//third_party/systemlibs:grpc.BUILD": "src/compiler/BUILD",
                    "@tsl//third_party/systemlibs:grpc.bazel.grpc_deps.bzl": "bazel/grpc_deps.bzl",
                    "@tsl//third_party/systemlibs:grpc.bazel.grpc_extra_deps.bzl": "bazel/grpc_extra_deps.bzl",
                    "@tsl//third_party/systemlibs:grpc.bazel.cc_grpc_library.bzl": "bazel/cc_grpc_library.bzl",
                    "@tsl//third_party/systemlibs:grpc.bazel.generate_cc.bzl": "bazel/generate_cc.bzl",
                    "@tsl//third_party/systemlibs:grpc.bazel.protobuf.bzl": "bazel/protobuf.bzl"
               }
          },
          "repositories": [
               {
                    "rule_class": "@@tsl//third_party:repo.bzl%_tf_http_archive",
                    "attributes": {
                         "name": "com_github_grpc_grpc",
                         "generator_name": "com_github_grpc_grpc",
                         "generator_function": "workspace",
                         "generator_location": None,
                         "sha256": "b956598d8cbe168b5ee717b5dafa56563eb5201a947856a6688bbeac9cac4e1f",
                         "urls": [
                              "https://storage.googleapis.com/mirror.tensorflow.org/github.com/grpc/grpc/archive/b54a5b338637f92bfcf4b0bc05e0f57a5fd8fadd.tar.gz",
                              "https://github.com/grpc/grpc/archive/b54a5b338637f92bfcf4b0bc05e0f57a5fd8fadd.tar.gz"
                         ],
                         "strip_prefix": "grpc-b54a5b338637f92bfcf4b0bc05e0f57a5fd8fadd",
                         "patch_file": [
                              "@tsl//third_party/grpc:generate_cc_env_fix.patch",
                              "@tsl//third_party/grpc:register_go_toolchain.patch"
                         ],
                         "system_build_file": "@tsl//third_party/systemlibs:grpc.BUILD",
                         "system_link_files": {
                              "@tsl//third_party/systemlibs:BUILD": "bazel/BUILD",
                              "@tsl//third_party/systemlibs:grpc.BUILD": "src/compiler/BUILD",
                              "@tsl//third_party/systemlibs:grpc.bazel.grpc_deps.bzl": "bazel/grpc_deps.bzl",
                              "@tsl//third_party/systemlibs:grpc.bazel.grpc_extra_deps.bzl": "bazel/grpc_extra_deps.bzl",
                              "@tsl//third_party/systemlibs:grpc.bazel.cc_grpc_library.bzl": "bazel/cc_grpc_library.bzl",
                              "@tsl//third_party/systemlibs:grpc.bazel.generate_cc.bzl": "bazel/generate_cc.bzl",
                              "@tsl//third_party/systemlibs:grpc.bazel.protobuf.bzl": "bazel/protobuf.bzl"
                         }
                    },
                    "output_tree_hash": "d971c8be4defe3a8975641755062ac0601168f801f1aeee829f764e1f6929a14"
               }
          ]
     },
     {
          "original_rule_class": "@@tsl//third_party:repo.bzl%_tf_http_archive",
          "definition_information": "Repository build_bazel_apple_support instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:46:15: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace2.bzl:164:19: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:604:21: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:508:20: in _tf_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/repo.bzl:136:21: in tf_http_archive\nRepository rule _tf_http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/repo.bzl:89:35: in <toplevel>\n",
          "original_attributes": {
               "name": "build_bazel_apple_support",
               "generator_name": "build_bazel_apple_support",
               "generator_function": "workspace",
               "generator_location": None,
               "sha256": "c4bb2b7367c484382300aee75be598b92f847896fb31bbd22f3a2346adf66a80",
               "urls": [
                    "https://storage.googleapis.com/mirror.tensorflow.org/github.com/bazelbuild/apple_support/releases/download/1.15.1/apple_support.1.15.1.tar.gz",
                    "https://github.com/bazelbuild/apple_support/releases/download/1.15.1/apple_support.1.15.1.tar.gz"
               ]
          },
          "repositories": [
               {
                    "rule_class": "@@tsl//third_party:repo.bzl%_tf_http_archive",
                    "attributes": {
                         "name": "build_bazel_apple_support",
                         "generator_name": "build_bazel_apple_support",
                         "generator_function": "workspace",
                         "generator_location": None,
                         "sha256": "c4bb2b7367c484382300aee75be598b92f847896fb31bbd22f3a2346adf66a80",
                         "urls": [
                              "https://storage.googleapis.com/mirror.tensorflow.org/github.com/bazelbuild/apple_support/releases/download/1.15.1/apple_support.1.15.1.tar.gz",
                              "https://github.com/bazelbuild/apple_support/releases/download/1.15.1/apple_support.1.15.1.tar.gz"
                         ]
                    },
                    "output_tree_hash": "fa8518bcefbd863bcc95766a6fea6182f11e35076994496b1bbabd6903990f72"
               }
          ]
     },
     {
          "original_rule_class": "@@tsl//third_party:repo.bzl%_tf_http_archive",
          "definition_information": "Repository com_google_benchmark instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:46:15: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace2.bzl:164:19: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:597:28: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:44:14: in _initialize_third_party\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/benchmark/workspace.bzl:9:20: in repo\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/repo.bzl:136:21: in tf_http_archive\nRepository rule _tf_http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/repo.bzl:89:35: in <toplevel>\n",
          "original_attributes": {
               "name": "com_google_benchmark",
               "generator_name": "com_google_benchmark",
               "generator_function": "workspace",
               "generator_location": None,
               "sha256": "552ca3d4d1af4beeb1907980f7096315aa24150d6baf5ac1e5ad90f04846c670",
               "urls": [
                    "https://storage.googleapis.com/mirror.tensorflow.org/github.com/google/benchmark/archive/f7547e29ccaed7b64ef4f7495ecfff1c9f6f3d03.tar.gz",
                    "https://github.com/google/benchmark/archive/f7547e29ccaed7b64ef4f7495ecfff1c9f6f3d03.tar.gz"
               ],
               "strip_prefix": "benchmark-f7547e29ccaed7b64ef4f7495ecfff1c9f6f3d03"
          },
          "repositories": [
               {
                    "rule_class": "@@tsl//third_party:repo.bzl%_tf_http_archive",
                    "attributes": {
                         "name": "com_google_benchmark",
                         "generator_name": "com_google_benchmark",
                         "generator_function": "workspace",
                         "generator_location": None,
                         "sha256": "552ca3d4d1af4beeb1907980f7096315aa24150d6baf5ac1e5ad90f04846c670",
                         "urls": [
                              "https://storage.googleapis.com/mirror.tensorflow.org/github.com/google/benchmark/archive/f7547e29ccaed7b64ef4f7495ecfff1c9f6f3d03.tar.gz",
                              "https://github.com/google/benchmark/archive/f7547e29ccaed7b64ef4f7495ecfff1c9f6f3d03.tar.gz"
                         ],
                         "strip_prefix": "benchmark-f7547e29ccaed7b64ef4f7495ecfff1c9f6f3d03"
                    },
                    "output_tree_hash": "c559d9a5ce75e7f98c103216a1f51bae1ca7d3224c945aada11bd65f3174e0fa"
               }
          ]
     },
     {
          "original_rule_class": "@@tsl//third_party:repo.bzl%_tf_http_archive",
          "definition_information": "Repository build_bazel_rules_swift instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:46:15: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace2.bzl:164:19: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:604:21: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:501:20: in _tf_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/repo.bzl:136:21: in tf_http_archive\nRepository rule _tf_http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/repo.bzl:89:35: in <toplevel>\n",
          "original_attributes": {
               "name": "build_bazel_rules_swift",
               "generator_name": "build_bazel_rules_swift",
               "generator_function": "workspace",
               "generator_location": None,
               "sha256": "bb01097c7c7a1407f8ad49a1a0b1960655cf823c26ad2782d0b7d15b323838e2",
               "urls": [
                    "https://storage.googleapis.com/mirror.tensorflow.org/github.com/bazelbuild/rules_swift/releases/download/1.18.0/rules_swift.1.18.0.tar.gz",
                    "https://github.com/bazelbuild/rules_swift/releases/download/1.18.0/rules_swift.1.18.0.tar.gz"
               ]
          },
          "repositories": [
               {
                    "rule_class": "@@tsl//third_party:repo.bzl%_tf_http_archive",
                    "attributes": {
                         "name": "build_bazel_rules_swift",
                         "generator_name": "build_bazel_rules_swift",
                         "generator_function": "workspace",
                         "generator_location": None,
                         "sha256": "bb01097c7c7a1407f8ad49a1a0b1960655cf823c26ad2782d0b7d15b323838e2",
                         "urls": [
                              "https://storage.googleapis.com/mirror.tensorflow.org/github.com/bazelbuild/rules_swift/releases/download/1.18.0/rules_swift.1.18.0.tar.gz",
                              "https://github.com/bazelbuild/rules_swift/releases/download/1.18.0/rules_swift.1.18.0.tar.gz"
                         ]
                    },
                    "output_tree_hash": "d000587d8570f92ac4a513c3d4c88923d2a881492f7029e4b08d94472634e10e"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository bazel_toolchains instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:50:15: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace1.bzl:19:17: in workspace\nRepository rule http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/http.bzl:387:31: in <toplevel>\n",
          "original_attributes": {
               "name": "bazel_toolchains",
               "generator_name": "bazel_toolchains",
               "generator_function": "workspace",
               "generator_location": None,
               "urls": [
                    "http://mirror.tensorflow.org/github.com/bazelbuild/bazel-toolchains/archive/8c717f8258cd5f6c7a45b97d974292755852b658.tar.gz",
                    "https://github.com/bazelbuild/bazel-toolchains/archive/8c717f8258cd5f6c7a45b97d974292755852b658.tar.gz"
               ],
               "sha256": "294cdd859e57fcaf101d4301978c408c88683fbc46fbc1a3829da92afbea55fb",
               "strip_prefix": "bazel-toolchains-8c717f8258cd5f6c7a45b97d974292755852b658"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "http://mirror.tensorflow.org/github.com/bazelbuild/bazel-toolchains/archive/8c717f8258cd5f6c7a45b97d974292755852b658.tar.gz",
                              "https://github.com/bazelbuild/bazel-toolchains/archive/8c717f8258cd5f6c7a45b97d974292755852b658.tar.gz"
                         ],
                         "sha256": "294cdd859e57fcaf101d4301978c408c88683fbc46fbc1a3829da92afbea55fb",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "bazel-toolchains-8c717f8258cd5f6c7a45b97d974292755852b658",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "bazel_toolchains"
                    },
                    "output_tree_hash": "8ce4badddbdd914b865129b6659261fe8fb81ca4c52680d649fe2a9478a42783"
               }
          ]
     },
     {
          "original_rule_class": "@@tsl//third_party:repo.bzl%_tf_http_archive",
          "definition_information": "Repository upb instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:46:15: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace2.bzl:164:19: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:604:21: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:556:20: in _tf_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/repo.bzl:136:21: in tf_http_archive\nRepository rule _tf_http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/repo.bzl:89:35: in <toplevel>\n",
          "original_attributes": {
               "name": "upb",
               "generator_name": "upb",
               "generator_function": "workspace",
               "generator_location": None,
               "sha256": "61d0417abd60e65ed589c9deee7c124fe76a4106831f6ad39464e1525cef1454",
               "urls": [
                    "https://storage.googleapis.com/mirror.tensorflow.org/github.com/protocolbuffers/upb/archive/9effcbcb27f0a665f9f345030188c0b291e32482.tar.gz",
                    "https://github.com/protocolbuffers/upb/archive/9effcbcb27f0a665f9f345030188c0b291e32482.tar.gz"
               ],
               "strip_prefix": "upb-9effcbcb27f0a665f9f345030188c0b291e32482",
               "patch_file": [
                    "@tsl//third_party/grpc:upb_platform_fix.patch"
               ]
          },
          "repositories": [
               {
                    "rule_class": "@@tsl//third_party:repo.bzl%_tf_http_archive",
                    "attributes": {
                         "name": "upb",
                         "generator_name": "upb",
                         "generator_function": "workspace",
                         "generator_location": None,
                         "sha256": "61d0417abd60e65ed589c9deee7c124fe76a4106831f6ad39464e1525cef1454",
                         "urls": [
                              "https://storage.googleapis.com/mirror.tensorflow.org/github.com/protocolbuffers/upb/archive/9effcbcb27f0a665f9f345030188c0b291e32482.tar.gz",
                              "https://github.com/protocolbuffers/upb/archive/9effcbcb27f0a665f9f345030188c0b291e32482.tar.gz"
                         ],
                         "strip_prefix": "upb-9effcbcb27f0a665f9f345030188c0b291e32482",
                         "patch_file": [
                              "@tsl//third_party/grpc:upb_platform_fix.patch"
                         ]
                    },
                    "output_tree_hash": "b8a5cf8026a15884a99e4b585ad33e13032b0e9d27aaedf46ae359faedfa5895"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository envoy_api instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:50:15: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace1.bzl:12:19: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace1.bzl:30:14: in workspace\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/com_github_grpc_grpc/bazel/grpc_deps.bzl:235:21: in grpc_deps\nRepository rule http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/http.bzl:387:31: in <toplevel>\n",
          "original_attributes": {
               "name": "envoy_api",
               "generator_name": "envoy_api",
               "generator_function": "workspace",
               "generator_location": None,
               "url": "https://github.com/envoyproxy/data-plane-api/archive/c83ed7ea9eb5fb3b93d1ad52b59750f1958b8bde.tar.gz",
               "sha256": "9e8cf42abce32c9b0e9e271b0cb62803084cbe5e5b49f5d5c2aef0766f9d69ca",
               "strip_prefix": "data-plane-api-c83ed7ea9eb5fb3b93d1ad52b59750f1958b8bde"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://github.com/envoyproxy/data-plane-api/archive/c83ed7ea9eb5fb3b93d1ad52b59750f1958b8bde.tar.gz",
                         "urls": [],
                         "sha256": "9e8cf42abce32c9b0e9e271b0cb62803084cbe5e5b49f5d5c2aef0766f9d69ca",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "data-plane-api-c83ed7ea9eb5fb3b93d1ad52b59750f1958b8bde",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "envoy_api"
                    },
                    "output_tree_hash": "7b18e057808a2fbf520dbe63b9109239c79c06c8de382f01dba980b4d513689a"
               }
          ]
     },
     {
          "original_rule_class": "@@tsl//third_party:repo.bzl%_tf_http_archive",
          "definition_information": "Repository build_bazel_rules_apple instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:46:15: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace2.bzl:164:19: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:604:21: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:494:20: in _tf_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/repo.bzl:136:21: in tf_http_archive\nRepository rule _tf_http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/repo.bzl:89:35: in <toplevel>\n",
          "original_attributes": {
               "name": "build_bazel_rules_apple",
               "generator_name": "build_bazel_rules_apple",
               "generator_function": "workspace",
               "generator_location": None,
               "sha256": "b4df908ec14868369021182ab191dbd1f40830c9b300650d5dc389e0b9266c8d",
               "urls": [
                    "https://storage.googleapis.com/mirror.tensorflow.org/github.com/bazelbuild/rules_apple/releases/download/3.5.1/rules_apple.3.5.1.tar.gz",
                    "https://github.com/bazelbuild/rules_apple/releases/download/3.5.1/rules_apple.3.5.1.tar.gz"
               ]
          },
          "repositories": [
               {
                    "rule_class": "@@tsl//third_party:repo.bzl%_tf_http_archive",
                    "attributes": {
                         "name": "build_bazel_rules_apple",
                         "generator_name": "build_bazel_rules_apple",
                         "generator_function": "workspace",
                         "generator_location": None,
                         "sha256": "b4df908ec14868369021182ab191dbd1f40830c9b300650d5dc389e0b9266c8d",
                         "urls": [
                              "https://storage.googleapis.com/mirror.tensorflow.org/github.com/bazelbuild/rules_apple/releases/download/3.5.1/rules_apple.3.5.1.tar.gz",
                              "https://github.com/bazelbuild/rules_apple/releases/download/3.5.1/rules_apple.3.5.1.tar.gz"
                         ]
                    },
                    "output_tree_hash": "ed0b36d22e7a616b8c203180142e6005a49f448e516943e2fb1493ab89b76a13"
               }
          ]
     },
     {
          "original_rule_class": "@@tsl//third_party:repo.bzl%_tf_http_archive",
          "definition_information": "Repository io_bazel_rules_go instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:46:15: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace2.bzl:164:19: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:604:21: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:550:20: in _tf_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/repo.bzl:136:21: in tf_http_archive\nRepository rule _tf_http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/repo.bzl:89:35: in <toplevel>\n",
          "original_attributes": {
               "name": "io_bazel_rules_go",
               "generator_name": "io_bazel_rules_go",
               "generator_function": "workspace",
               "generator_location": None,
               "sha256": "16e9fca53ed6bd4ff4ad76facc9b7b651a89db1689a2877d6fd7b82aa824e366",
               "urls": [
                    "https://storage.googleapis.com/mirror.tensorflow.org/github.com/bazelbuild/rules_go/releases/download/v0.34.0/rules_go-v0.34.0.zip",
                    "https://github.com/bazelbuild/rules_go/releases/download/v0.34.0/rules_go-v0.34.0.zip"
               ]
          },
          "repositories": [
               {
                    "rule_class": "@@tsl//third_party:repo.bzl%_tf_http_archive",
                    "attributes": {
                         "name": "io_bazel_rules_go",
                         "generator_name": "io_bazel_rules_go",
                         "generator_function": "workspace",
                         "generator_location": None,
                         "sha256": "16e9fca53ed6bd4ff4ad76facc9b7b651a89db1689a2877d6fd7b82aa824e366",
                         "urls": [
                              "https://storage.googleapis.com/mirror.tensorflow.org/github.com/bazelbuild/rules_go/releases/download/v0.34.0/rules_go-v0.34.0.zip",
                              "https://github.com/bazelbuild/rules_go/releases/download/v0.34.0/rules_go-v0.34.0.zip"
                         ]
                    },
                    "output_tree_hash": "4ffeb2afa39c551b5b71df6405c803ea86c1b43da776da21f69e40683562b517"
               }
          ]
     },
     {
          "original_rule_class": "@@tsl//third_party:repo.bzl%_tf_http_archive",
          "definition_information": "Repository com_google_protobuf instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:46:15: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace2.bzl:164:19: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:604:21: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:287:20: in _tf_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/repo.bzl:136:21: in tf_http_archive\nRepository rule _tf_http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/repo.bzl:89:35: in <toplevel>\n",
          "original_attributes": {
               "name": "com_google_protobuf",
               "generator_name": "com_google_protobuf",
               "generator_function": "workspace",
               "generator_location": None,
               "sha256": "f66073dee0bc159157b0bd7f502d7d1ee0bc76b3c1eac9836927511bdc4b3fc1",
               "urls": [
                    "https://storage.googleapis.com/mirror.tensorflow.org/github.com/protocolbuffers/protobuf/archive/v3.21.9.zip",
                    "https://github.com/protocolbuffers/protobuf/archive/v3.21.9.zip"
               ],
               "strip_prefix": "protobuf-3.21.9",
               "patch_file": [
                    "@tsl//third_party/protobuf:protobuf.patch"
               ],
               "system_build_file": "@tsl//third_party/systemlibs:protobuf.BUILD",
               "system_link_files": {
                    "@tsl//third_party/systemlibs:protobuf.bzl": "protobuf.bzl",
                    "@tsl//third_party/systemlibs:protobuf_deps.bzl": "protobuf_deps.bzl"
               }
          },
          "repositories": [
               {
                    "rule_class": "@@tsl//third_party:repo.bzl%_tf_http_archive",
                    "attributes": {
                         "name": "com_google_protobuf",
                         "generator_name": "com_google_protobuf",
                         "generator_function": "workspace",
                         "generator_location": None,
                         "sha256": "f66073dee0bc159157b0bd7f502d7d1ee0bc76b3c1eac9836927511bdc4b3fc1",
                         "urls": [
                              "https://storage.googleapis.com/mirror.tensorflow.org/github.com/protocolbuffers/protobuf/archive/v3.21.9.zip",
                              "https://github.com/protocolbuffers/protobuf/archive/v3.21.9.zip"
                         ],
                         "strip_prefix": "protobuf-3.21.9",
                         "patch_file": [
                              "@tsl//third_party/protobuf:protobuf.patch"
                         ],
                         "system_build_file": "@tsl//third_party/systemlibs:protobuf.BUILD",
                         "system_link_files": {
                              "@tsl//third_party/systemlibs:protobuf.bzl": "protobuf.bzl",
                              "@tsl//third_party/systemlibs:protobuf_deps.bzl": "protobuf_deps.bzl"
                         }
                    },
                    "output_tree_hash": "3acc7d5e6e4b81494630761e3319eb68109d6537f4dfab906802d6cddc14985f"
               }
          ]
     },
     {
          "original_rule_class": "@@tsl//third_party/gpus/cuda/hermetic:cuda_json_init_repository.bzl%cuda_redist_json",
          "definition_information": "Repository cuda_redist_json instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:61:26: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/gpus/cuda/hermetic/cuda_json_init_repository.bzl:121:21: in cuda_json_init_repository\nRepository rule cuda_redist_json defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/gpus/cuda/hermetic/cuda_json_init_repository.bzl:102:35: in <toplevel>\n",
          "original_attributes": {
               "name": "cuda_redist_json",
               "generator_name": "cuda_redist_json",
               "generator_function": "cuda_json_init_repository",
               "generator_location": None,
               "cuda_json_dict": {
                    "11.8": [
                         "https://developer.download.nvidia.com/compute/cuda/redist/redistrib_11.8.0.json",
                         "941a950a4ab3b95311c50df7b3c8bca973e0cdda76fc2f4b456d2d5e4dac0281"
                    ],
                    "12.1.1": [
                         "https://developer.download.nvidia.com/compute/cuda/redist/redistrib_12.1.1.json",
                         "bafea3cb83a4cf5c764eeedcaac0040d0d3c5db3f9a74550da0e7b6ac24d378c"
                    ],
                    "12.2.0": [
                         "https://developer.download.nvidia.com/compute/cuda/redist/redistrib_12.2.0.json",
                         "d883762c6339c8ebb3ffb072facc8f7265cd257d2db16a475fff9a9306ecea89"
                    ],
                    "12.3.1": [
                         "https://developer.download.nvidia.com/compute/cuda/redist/redistrib_12.3.1.json",
                         "b3cc4181d711cf9b6e3718f323b23813c24f9478119911d7b4bceec9b437dbc3"
                    ],
                    "12.3.2": [
                         "https://developer.download.nvidia.com/compute/cuda/redist/redistrib_12.3.2.json",
                         "1b6eacf335dd49803633fed53ef261d62c193e5a56eee5019e7d2f634e39e7ef"
                    ],
                    "12.4.0": [
                         "https://developer.download.nvidia.com/compute/cuda/redist/redistrib_12.4.0.json",
                         "a4f496b8d5299939b34c9ef88dc4274821f8c9451b2d7c9bcee53166932da067"
                    ],
                    "12.4.1": [
                         "https://developer.download.nvidia.com/compute/cuda/redist/redistrib_12.4.1.json",
                         "9cd815f3b71c2e3686ef2219b7794b81044f9dcefaa8e21dacfcb5bc4d931892"
                    ],
                    "12.5.0": [
                         "https://developer.download.nvidia.com/compute/cuda/redist/redistrib_12.5.0.json",
                         "166664b520bfe51f27abcc8c7a934f4cb6ea287f8c399b5f8255f6f4d214569a"
                    ],
                    "12.5.1": [
                         "https://developer.download.nvidia.com/compute/cuda/redist/redistrib_12.5.1.json",
                         "7ab9c76014ae4907fa1b51738af599607a5fd8ca3a5c4bb4c3b31338cc642a93"
                    ],
                    "12.6.0": [
                         "https://developer.download.nvidia.com/compute/cuda/redist/redistrib_12.6.0.json",
                         "87740b01676b3d18982982ab96ec7fa1a626d03a96df070a6b0f258d01ff5fab"
                    ],
                    "12.6.1": [
                         "https://developer.download.nvidia.com/compute/cuda/redist/redistrib_12.6.1.json",
                         "22ddfeb81a6f9cee4a708a2e3b4db1c36c7db0a1daa1f33f9c7f2f12a1e790de"
                    ],
                    "12.6.2": [
                         "https://developer.download.nvidia.com/compute/cuda/redist/redistrib_12.6.2.json",
                         "8056da1f5acca8e613da1349d9b8782b774ad0254e3eddcc95734ded4d33f2df"
                    ],
                    "12.6.3": [
                         "https://developer.download.nvidia.com/compute/cuda/redist/redistrib_12.6.3.json",
                         "9c598598457a6463eb92889080c16b2b9dc04150e501b8bfc1536d403ba70aaf"
                    ],
                    "12.8.0": [
                         "https://developer.download.nvidia.com/compute/cuda/redist/redistrib_12.8.0.json",
                         "daa0d766b36feaa933592162c27be5fb63b68fc547ca6886c160a35d96ee8891"
                    ]
               },
               "cudnn_json_dict": {
                    "8.6": [
                         "https://developer.download.nvidia.com/compute/cudnn/redist/redistrib_8.6.0.json",
                         "7f6f50bed4fd8216dc10d6ef505771dc0ecc99cce813993ab405cb507a21d51d"
                    ],
                    "8.9.4.25": [
                         "https://developer.download.nvidia.com/compute/cudnn/redist/redistrib_8.9.4.25.json",
                         "02258dba8384860c9230fe3c78522e7bd8e350e461ccd37a8d932cb64127ba57"
                    ],
                    "8.9.6": [
                         "https://developer.download.nvidia.com/compute/cudnn/redist/redistrib_8.9.6.json",
                         "6069ef92a2b9bb18cebfbc944964bd2b024b76f2c2c35a43812982e0bc45cf0c"
                    ],
                    "8.9.7.29": [
                         "https://developer.download.nvidia.com/compute/cudnn/redist/redistrib_8.9.7.29.json",
                         "a0734f26f068522464fa09b2f2c186dfbe6ad7407a88ea0c50dd331f0c3389ec"
                    ],
                    "9.1.1": [
                         "https://developer.download.nvidia.com/compute/cudnn/redist/redistrib_9.1.1.json",
                         "d22d569405e5683ff8e563d00d6e8c27e5e6a902c564c23d752b22a8b8b3fe20"
                    ],
                    "9.2.0": [
                         "https://developer.download.nvidia.com/compute/cudnn/redist/redistrib_9.2.0.json",
                         "6852eb279b95d2b5775f7a7737ec133bed059107f863cdd8588f3ae6f13eadd7"
                    ],
                    "9.2.1": [
                         "https://developer.download.nvidia.com/compute/cudnn/redist/redistrib_9.2.1.json",
                         "9a4198c59b2e66b2b115a736ebe4dc8f3dc6d78161bb494702f824da8fc77b99"
                    ],
                    "9.3.0": [
                         "https://developer.download.nvidia.com/compute/cudnn/redist/redistrib_9.3.0.json",
                         "d17d9a7878365736758550294f03e633a0b023bec879bf173349bfb34781972e"
                    ],
                    "9.4.0": [
                         "https://developer.download.nvidia.com/compute/cudnn/redist/redistrib_9.4.0.json",
                         "6eeaafc5cc3d4bb2f283e6298e4c55d4c59d7c83c5d9fd8721a2c0e55aee4e54"
                    ],
                    "9.5.0": [
                         "https://developer.download.nvidia.com/compute/cudnn/redist/redistrib_9.5.0.json",
                         "3939f0533fdd0d3aa7edd1ac358d43da18e438e5d8f39c3c15bb72519bad7fb5"
                    ],
                    "9.5.1": [
                         "https://developer.download.nvidia.com/compute/cudnn/redist/redistrib_9.5.1.json",
                         "a5484eef575bbb1fd4f96136cf12244ebc194b661f5ae9ed3b8aaa07e06434b1"
                    ],
                    "9.6.0": [
                         "https://developer.download.nvidia.com/compute/cudnn/redist/redistrib_9.6.0.json",
                         "6dd9a931d981fe5afc7e7ed0c422a4035b1411db4e28a39cf2429e62e3efcd3e"
                    ],
                    "9.7.0": [
                         "https://developer.download.nvidia.com/compute/cudnn/redist/redistrib_9.7.0.json",
                         "e715c1d028585d228c4678c2cdc5ad9a34fde54515a1c52aa60e36021a90dd90"
                    ],
                    "9.7.1": [
                         "https://developer.download.nvidia.com/compute/cudnn/redist/redistrib_9.7.1.json",
                         "f9bc411a4908f0931e7323f89049e3a38453632c4ac5f4aa3220af69ddded9dc"
                    ]
               }
          },
          "repositories": [
               {
                    "rule_class": "@@tsl//third_party/gpus/cuda/hermetic:cuda_json_init_repository.bzl%cuda_redist_json",
                    "attributes": {
                         "name": "cuda_redist_json",
                         "generator_name": "cuda_redist_json",
                         "generator_function": "cuda_json_init_repository",
                         "generator_location": None,
                         "cuda_json_dict": {
                              "11.8": [
                                   "https://developer.download.nvidia.com/compute/cuda/redist/redistrib_11.8.0.json",
                                   "941a950a4ab3b95311c50df7b3c8bca973e0cdda76fc2f4b456d2d5e4dac0281"
                              ],
                              "12.1.1": [
                                   "https://developer.download.nvidia.com/compute/cuda/redist/redistrib_12.1.1.json",
                                   "bafea3cb83a4cf5c764eeedcaac0040d0d3c5db3f9a74550da0e7b6ac24d378c"
                              ],
                              "12.2.0": [
                                   "https://developer.download.nvidia.com/compute/cuda/redist/redistrib_12.2.0.json",
                                   "d883762c6339c8ebb3ffb072facc8f7265cd257d2db16a475fff9a9306ecea89"
                              ],
                              "12.3.1": [
                                   "https://developer.download.nvidia.com/compute/cuda/redist/redistrib_12.3.1.json",
                                   "b3cc4181d711cf9b6e3718f323b23813c24f9478119911d7b4bceec9b437dbc3"
                              ],
                              "12.3.2": [
                                   "https://developer.download.nvidia.com/compute/cuda/redist/redistrib_12.3.2.json",
                                   "1b6eacf335dd49803633fed53ef261d62c193e5a56eee5019e7d2f634e39e7ef"
                              ],
                              "12.4.0": [
                                   "https://developer.download.nvidia.com/compute/cuda/redist/redistrib_12.4.0.json",
                                   "a4f496b8d5299939b34c9ef88dc4274821f8c9451b2d7c9bcee53166932da067"
                              ],
                              "12.4.1": [
                                   "https://developer.download.nvidia.com/compute/cuda/redist/redistrib_12.4.1.json",
                                   "9cd815f3b71c2e3686ef2219b7794b81044f9dcefaa8e21dacfcb5bc4d931892"
                              ],
                              "12.5.0": [
                                   "https://developer.download.nvidia.com/compute/cuda/redist/redistrib_12.5.0.json",
                                   "166664b520bfe51f27abcc8c7a934f4cb6ea287f8c399b5f8255f6f4d214569a"
                              ],
                              "12.5.1": [
                                   "https://developer.download.nvidia.com/compute/cuda/redist/redistrib_12.5.1.json",
                                   "7ab9c76014ae4907fa1b51738af599607a5fd8ca3a5c4bb4c3b31338cc642a93"
                              ],
                              "12.6.0": [
                                   "https://developer.download.nvidia.com/compute/cuda/redist/redistrib_12.6.0.json",
                                   "87740b01676b3d18982982ab96ec7fa1a626d03a96df070a6b0f258d01ff5fab"
                              ],
                              "12.6.1": [
                                   "https://developer.download.nvidia.com/compute/cuda/redist/redistrib_12.6.1.json",
                                   "22ddfeb81a6f9cee4a708a2e3b4db1c36c7db0a1daa1f33f9c7f2f12a1e790de"
                              ],
                              "12.6.2": [
                                   "https://developer.download.nvidia.com/compute/cuda/redist/redistrib_12.6.2.json",
                                   "8056da1f5acca8e613da1349d9b8782b774ad0254e3eddcc95734ded4d33f2df"
                              ],
                              "12.6.3": [
                                   "https://developer.download.nvidia.com/compute/cuda/redist/redistrib_12.6.3.json",
                                   "9c598598457a6463eb92889080c16b2b9dc04150e501b8bfc1536d403ba70aaf"
                              ],
                              "12.8.0": [
                                   "https://developer.download.nvidia.com/compute/cuda/redist/redistrib_12.8.0.json",
                                   "daa0d766b36feaa933592162c27be5fb63b68fc547ca6886c160a35d96ee8891"
                              ]
                         },
                         "cudnn_json_dict": {
                              "8.6": [
                                   "https://developer.download.nvidia.com/compute/cudnn/redist/redistrib_8.6.0.json",
                                   "7f6f50bed4fd8216dc10d6ef505771dc0ecc99cce813993ab405cb507a21d51d"
                              ],
                              "8.9.4.25": [
                                   "https://developer.download.nvidia.com/compute/cudnn/redist/redistrib_8.9.4.25.json",
                                   "02258dba8384860c9230fe3c78522e7bd8e350e461ccd37a8d932cb64127ba57"
                              ],
                              "8.9.6": [
                                   "https://developer.download.nvidia.com/compute/cudnn/redist/redistrib_8.9.6.json",
                                   "6069ef92a2b9bb18cebfbc944964bd2b024b76f2c2c35a43812982e0bc45cf0c"
                              ],
                              "8.9.7.29": [
                                   "https://developer.download.nvidia.com/compute/cudnn/redist/redistrib_8.9.7.29.json",
                                   "a0734f26f068522464fa09b2f2c186dfbe6ad7407a88ea0c50dd331f0c3389ec"
                              ],
                              "9.1.1": [
                                   "https://developer.download.nvidia.com/compute/cudnn/redist/redistrib_9.1.1.json",
                                   "d22d569405e5683ff8e563d00d6e8c27e5e6a902c564c23d752b22a8b8b3fe20"
                              ],
                              "9.2.0": [
                                   "https://developer.download.nvidia.com/compute/cudnn/redist/redistrib_9.2.0.json",
                                   "6852eb279b95d2b5775f7a7737ec133bed059107f863cdd8588f3ae6f13eadd7"
                              ],
                              "9.2.1": [
                                   "https://developer.download.nvidia.com/compute/cudnn/redist/redistrib_9.2.1.json",
                                   "9a4198c59b2e66b2b115a736ebe4dc8f3dc6d78161bb494702f824da8fc77b99"
                              ],
                              "9.3.0": [
                                   "https://developer.download.nvidia.com/compute/cudnn/redist/redistrib_9.3.0.json",
                                   "d17d9a7878365736758550294f03e633a0b023bec879bf173349bfb34781972e"
                              ],
                              "9.4.0": [
                                   "https://developer.download.nvidia.com/compute/cudnn/redist/redistrib_9.4.0.json",
                                   "6eeaafc5cc3d4bb2f283e6298e4c55d4c59d7c83c5d9fd8721a2c0e55aee4e54"
                              ],
                              "9.5.0": [
                                   "https://developer.download.nvidia.com/compute/cudnn/redist/redistrib_9.5.0.json",
                                   "3939f0533fdd0d3aa7edd1ac358d43da18e438e5d8f39c3c15bb72519bad7fb5"
                              ],
                              "9.5.1": [
                                   "https://developer.download.nvidia.com/compute/cudnn/redist/redistrib_9.5.1.json",
                                   "a5484eef575bbb1fd4f96136cf12244ebc194b661f5ae9ed3b8aaa07e06434b1"
                              ],
                              "9.6.0": [
                                   "https://developer.download.nvidia.com/compute/cudnn/redist/redistrib_9.6.0.json",
                                   "6dd9a931d981fe5afc7e7ed0c422a4035b1411db4e28a39cf2429e62e3efcd3e"
                              ],
                              "9.7.0": [
                                   "https://developer.download.nvidia.com/compute/cudnn/redist/redistrib_9.7.0.json",
                                   "e715c1d028585d228c4678c2cdc5ad9a34fde54515a1c52aa60e36021a90dd90"
                              ],
                              "9.7.1": [
                                   "https://developer.download.nvidia.com/compute/cudnn/redist/redistrib_9.7.1.json",
                                   "f9bc411a4908f0931e7323f89049e3a38453632c4ac5f4aa3220af69ddded9dc"
                              ]
                         }
                    },
                    "output_tree_hash": "b589f781f6c41fb9eccfd6f4a5ca82c803604d0ccfeb2026033aaf8c83345b70"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:local.bzl%local_repository",
          "definition_information": "Repository rules_java_builtin instantiated at:\n  /DEFAULT.WORKSPACE:12:36: in <toplevel>\nRepository rule local_repository defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/local.bzl:64:35: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_java_builtin",
               "path": "/usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/install/bd3f2062f72dd67fde166eda94178459/rules_java"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:local.bzl%local_repository",
                    "attributes": {
                         "name": "rules_java_builtin",
                         "path": "/usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/install/bd3f2062f72dd67fde166eda94178459/rules_java"
                    },
                    "output_tree_hash": "23156af102e8441d4b3e5358092fc1dce333786289d48b1df6503ecb8c735cf3"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:local.bzl%local_repository",
          "definition_information": "Repository internal_platforms_do_not_use instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:153:6: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\nRepository rule local_repository defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/local.bzl:64:35: in <toplevel>\n",
          "original_attributes": {
               "name": "internal_platforms_do_not_use",
               "generator_name": "internal_platforms_do_not_use",
               "generator_function": "maybe",
               "generator_location": None,
               "path": "/usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/install/bd3f2062f72dd67fde166eda94178459/platforms"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:local.bzl%local_repository",
                    "attributes": {
                         "name": "internal_platforms_do_not_use",
                         "generator_name": "internal_platforms_do_not_use",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "path": "/usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/install/bd3f2062f72dd67fde166eda94178459/platforms"
                    },
                    "output_tree_hash": "db797f5ddb49595460e727f2c71af1b3adfed4d65132bbe31bd9d3a06bd95dba"
               }
          ]
     },
     {
          "original_rule_class": "@@tsl//third_party/gpus:sycl_configure.bzl%sycl_configure",
          "definition_information": "Repository local_config_sycl instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:46:15: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace2.bzl:164:19: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:594:19: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:75:19: in _tf_toolchains\nRepository rule sycl_configure defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/gpus/sycl_configure.bzl:519:33: in <toplevel>\n",
          "original_attributes": {
               "name": "local_config_sycl",
               "generator_name": "local_config_sycl",
               "generator_function": "workspace",
               "generator_location": None
          },
          "repositories": [
               {
                    "rule_class": "@@tsl//third_party/gpus:sycl_configure.bzl%sycl_configure",
                    "attributes": {
                         "name": "local_config_sycl",
                         "generator_name": "local_config_sycl",
                         "generator_function": "workspace",
                         "generator_location": None
                    },
                    "output_tree_hash": "2dd7d6e5d025247fc4a8a79d504679f51604dadf88dfa2832c623921a6b2a312"
               }
          ]
     },
     {
          "original_rule_class": "@@tsl//third_party/gpus:rocm_configure.bzl%rocm_configure",
          "definition_information": "Repository local_config_rocm instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:46:15: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace2.bzl:164:19: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:594:19: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:74:19: in _tf_toolchains\nRepository rule rocm_configure defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/gpus/rocm_configure.bzl:885:33: in <toplevel>\n",
          "original_attributes": {
               "name": "local_config_rocm",
               "generator_name": "local_config_rocm",
               "generator_function": "workspace",
               "generator_location": None
          },
          "repositories": [
               {
                    "rule_class": "@@tsl//third_party/gpus:rocm_configure.bzl%rocm_configure",
                    "attributes": {
                         "name": "local_config_rocm",
                         "generator_name": "local_config_rocm",
                         "generator_function": "workspace",
                         "generator_location": None
                    },
                    "output_tree_hash": "aa90d56b2c09febfa90ab8f9b75a45caaaf7dbd337ab0b97a7cf7de779b1236f"
               }
          ]
     },
     {
          "original_rule_class": "//tools/toolchains/remote:configure.bzl%remote_execution_configure",
          "definition_information": "Repository local_config_remote_execution instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:46:15: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace2.bzl:164:19: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:594:19: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:76:31: in _tf_toolchains\nRepository rule remote_execution_configure defined at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tools/toolchains/remote/configure.bzl:40:45: in <toplevel>\n",
          "original_attributes": {
               "name": "local_config_remote_execution",
               "generator_name": "local_config_remote_execution",
               "generator_function": "workspace",
               "generator_location": None
          },
          "repositories": [
               {
                    "rule_class": "//tools/toolchains/remote:configure.bzl%remote_execution_configure",
                    "attributes": {
                         "name": "local_config_remote_execution",
                         "generator_name": "local_config_remote_execution",
                         "generator_function": "workspace",
                         "generator_location": None
                    },
                    "output_tree_hash": "e73b1f4b0799c1d92c9e9f18e7f965c712ef58b3368647243b1df139c7db935a"
               }
          ]
     },
     {
          "original_rule_class": "@@tsl//third_party/tensorrt:tensorrt_configure.bzl%tensorrt_configure",
          "definition_information": "Repository local_config_tensorrt instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:46:15: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace2.bzl:164:19: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:594:19: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:70:23: in _tf_toolchains\nRepository rule tensorrt_configure defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/tensorrt/tensorrt_configure.bzl:337:37: in <toplevel>\n",
          "original_attributes": {
               "name": "local_config_tensorrt",
               "generator_name": "local_config_tensorrt",
               "generator_function": "workspace",
               "generator_location": None
          },
          "repositories": [
               {
                    "rule_class": "@@tsl//third_party/tensorrt:tensorrt_configure.bzl%tensorrt_configure",
                    "attributes": {
                         "name": "local_config_tensorrt",
                         "generator_name": "local_config_tensorrt",
                         "generator_function": "workspace",
                         "generator_location": None
                    },
                    "output_tree_hash": "8fe2a524053b9d22850dafbb4e21a454ba76187b4b68abff4128bda16744af5f"
               }
          ]
     },
     {
          "original_rule_class": "@@llvm-raw//utils/bazel:configure.bzl%llvm_configure",
          "definition_information": "Repository llvm-project instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:46:15: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace2.bzl:164:19: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:604:21: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:352:15: in _tf_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/llvm/setup.bzl:19:19: in llvm_setup\nRepository rule llvm_configure defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/llvm-raw/utils/bazel/configure.bzl:182:33: in <toplevel>\n",
          "original_attributes": {
               "name": "llvm-project",
               "generator_name": "llvm-project",
               "generator_function": "workspace",
               "generator_location": None,
               "targets": [
                    "AArch64",
                    "AMDGPU",
                    "ARM",
                    "NVPTX",
                    "PowerPC",
                    "RISCV",
                    "SystemZ",
                    "X86"
               ]
          },
          "repositories": [
               {
                    "rule_class": "@@llvm-raw//utils/bazel:configure.bzl%llvm_configure",
                    "attributes": {
                         "name": "llvm-project",
                         "generator_name": "llvm-project",
                         "generator_function": "workspace",
                         "generator_location": None,
                         "targets": [
                              "AArch64",
                              "AMDGPU",
                              "ARM",
                              "NVPTX",
                              "PowerPC",
                              "RISCV",
                              "SystemZ",
                              "X86"
                         ]
                    },
                    "output_tree_hash": "f3e960ad2066b66970df9e095cc523494d437449ebd2c8ea9c243f014558844e"
               }
          ]
     },
     {
          "original_rule_class": "@@tsl//third_party/gpus/cuda/hermetic:cuda_configure.bzl%cuda_configure",
          "definition_information": "Repository local_config_cuda instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:87:15: in <toplevel>\nRepository rule cuda_configure defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/gpus/cuda/hermetic/cuda_configure.bzl:555:33: in <toplevel>\n",
          "original_attributes": {
               "name": "local_config_cuda"
          },
          "repositories": [
               {
                    "rule_class": "@@tsl//third_party/gpus/cuda/hermetic:cuda_configure.bzl%cuda_configure",
                    "attributes": {
                         "name": "local_config_cuda"
                    },
                    "output_tree_hash": "783192ba18c0f673bea219ece7cc216d4922a83c1486c6226ee7f81d7912216f"
               }
          ]
     },
     {
          "original_rule_class": "@@internal_platforms_do_not_use//host:extension.bzl%host_platform_repo",
          "definition_information": "Repository host_platform instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:165:6: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\nRepository rule host_platform_repo defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/internal_platforms_do_not_use/host/extension.bzl:51:37: in <toplevel>\n",
          "original_attributes": {
               "name": "host_platform",
               "generator_name": "host_platform",
               "generator_function": "maybe",
               "generator_location": None
          },
          "repositories": [
               {
                    "rule_class": "@@internal_platforms_do_not_use//host:extension.bzl%host_platform_repo",
                    "attributes": {
                         "name": "host_platform",
                         "generator_name": "host_platform",
                         "generator_function": "maybe",
                         "generator_location": None
                    },
                    "output_tree_hash": "7bb7732a410e479305fb8602fbfbe14a04e932eed9f8384852c03def646e87d5"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository platforms instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:54:15: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace0.bzl:53:19: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace0.bzl:122:29: in workspace\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/build_bazel_rules_apple/apple/repositories.bzl:130:15: in apple_rules_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/build_bazel_rules_apple/apple/repositories.bzl:86:14: in _maybe\nRepository rule http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/http.bzl:387:31: in <toplevel>\n",
          "original_attributes": {
               "name": "platforms",
               "generator_name": "platforms",
               "generator_function": "workspace",
               "generator_location": None,
               "urls": [
                    "https://mirror.bazel.build/github.com/bazelbuild/platforms/releases/download/0.0.9/platforms-0.0.7.tar.gz",
                    "https://github.com/bazelbuild/platforms/releases/download/0.0.9/platforms-0.0.9.tar.gz"
               ],
               "sha256": "5eda539c841265031c2f82d8ae7a3a6490bd62176e0c038fc469eabf91f6149b"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://mirror.bazel.build/github.com/bazelbuild/platforms/releases/download/0.0.9/platforms-0.0.7.tar.gz",
                              "https://github.com/bazelbuild/platforms/releases/download/0.0.9/platforms-0.0.9.tar.gz"
                         ],
                         "sha256": "5eda539c841265031c2f82d8ae7a3a6490bd62176e0c038fc469eabf91f6149b",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "platforms"
                    },
                    "output_tree_hash": "567cadb959c1beeda065e093b6599dc3a3f7b8c41db40593f601b2c99830eb3d"
               }
          ]
     },
     {
          "original_rule_class": "@@tsl//third_party/remote_config:remote_platform_configure.bzl%remote_platform_configure",
          "definition_information": "Repository local_execution_config_platform instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:46:15: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace2.bzl:164:19: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:594:19: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:65:27: in _tf_toolchains\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tools/toolchains/remote_config/configs.bzl:6:28: in initialize_rbe_configs\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tools/toolchains/remote_config/rbe_config.bzl:85:30: in _tensorflow_local_config\nRepository rule remote_platform_configure defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/remote_config/remote_platform_configure.bzl:49:44: in <toplevel>\n",
          "original_attributes": {
               "name": "local_execution_config_platform",
               "generator_name": "local_execution_config_platform",
               "generator_function": "workspace",
               "generator_location": None,
               "platform_exec_properties": {},
               "platform": "local"
          },
          "repositories": [
               {
                    "rule_class": "@@tsl//third_party/remote_config:remote_platform_configure.bzl%remote_platform_configure",
                    "attributes": {
                         "name": "local_execution_config_platform",
                         "generator_name": "local_execution_config_platform",
                         "generator_function": "workspace",
                         "generator_location": None,
                         "platform_exec_properties": {},
                         "platform": "local"
                    },
                    "output_tree_hash": "7867e60dd14c11ddb89dc39bc70e8b9b656452d8b3164121111e19503b7d4017"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remote_jdk8_macos_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:370:22: in rules_java_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:349:34: in remote_jdk8_repos\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remote_jdk8_macos_toolchain_config_repo",
               "generator_name": "remote_jdk8_macos_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_8\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"8\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_macos//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_macos//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remote_jdk8_macos_toolchain_config_repo",
                         "generator_name": "remote_jdk8_macos_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_8\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"8\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_macos//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_macos//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "e0d82dc2dbe8ec49d859811afe4973ec36226875a39ac7fc8419e91e7e9c89fb"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remote_jdk8_linux_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:370:22: in rules_java_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:349:34: in remote_jdk8_repos\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remote_jdk8_linux_toolchain_config_repo",
               "generator_name": "remote_jdk8_linux_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_8\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"8\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_linux//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_linux//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remote_jdk8_linux_toolchain_config_repo",
                         "generator_name": "remote_jdk8_linux_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_8\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"8\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_linux//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_linux//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "b6a178fc0ca08a4473490f1c5d0f9f633db0ca0f2834c69dd08ce8290cf9ca86"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk11_macos_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:371:23: in rules_java_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:353:34: in remote_jdk11_repos\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk11_macos_toolchain_config_repo",
               "generator_name": "remotejdk11_macos_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_macos//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_macos//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk11_macos_toolchain_config_repo",
                         "generator_name": "remotejdk11_macos_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_macos//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_macos//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "45b3b36d22d3e614745e7a5e838351c32fe0eabb09a4a197bac0f4d416a950ce"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remote_jdk8_linux_aarch64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:370:22: in rules_java_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:349:34: in remote_jdk8_repos\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remote_jdk8_linux_aarch64_toolchain_config_repo",
               "generator_name": "remote_jdk8_linux_aarch64_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_8\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"8\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_linux_aarch64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_linux_aarch64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remote_jdk8_linux_aarch64_toolchain_config_repo",
                         "generator_name": "remote_jdk8_linux_aarch64_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_8\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"8\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_linux_aarch64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_linux_aarch64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "c9c795851cffbf2a808bfc7cccea597c3b3fef46cfefa084f7e9de7e90b65447"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk11_linux_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:371:23: in rules_java_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:353:34: in remote_jdk11_repos\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk11_linux_toolchain_config_repo",
               "generator_name": "remotejdk11_linux_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk11_linux_toolchain_config_repo",
                         "generator_name": "remotejdk11_linux_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "0a170bf4f31e6c4621aeb4d4ce4b75b808be2f3a63cb55dc8172c27707d299ab"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk17_macos_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:372:23: in rules_java_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:357:34: in remote_jdk17_repos\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk17_macos_toolchain_config_repo",
               "generator_name": "remotejdk17_macos_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_macos//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_macos//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk17_macos_toolchain_config_repo",
                         "generator_name": "remotejdk17_macos_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_macos//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_macos//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "41aa7b3317f8d9001746e908454760bf544ffaa058abe22f40711246608022ba"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk11_win_arm64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:371:23: in rules_java_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:353:34: in remote_jdk11_repos\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk11_win_arm64_toolchain_config_repo",
               "generator_name": "remotejdk11_win_arm64_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_win_arm64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_win_arm64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk11_win_arm64_toolchain_config_repo",
                         "generator_name": "remotejdk11_win_arm64_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_win_arm64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_win_arm64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "c237bd9668de9b6437c452c020ea5bc717ff80b1a5ffd581adfdc7d4a6c5fe03"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk11_win_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:371:23: in rules_java_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:353:34: in remote_jdk11_repos\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk11_win_toolchain_config_repo",
               "generator_name": "remotejdk11_win_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_win//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_win//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk11_win_toolchain_config_repo",
                         "generator_name": "remotejdk11_win_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_win//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_win//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "d0587a4ecc9323d5cf65314b2d284b520ffb5ee1d3231cc6601efa13dadcc0f4"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk21_linux_s390x_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:373:23: in rules_java_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:361:34: in remote_jdk21_repos\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk21_linux_s390x_toolchain_config_repo",
               "generator_name": "remotejdk21_linux_s390x_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_21\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"21\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_linux_s390x//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_linux_s390x//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk21_linux_s390x_toolchain_config_repo",
                         "generator_name": "remotejdk21_linux_s390x_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_21\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"21\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_linux_s390x//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_linux_s390x//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "30b78e0951c37c2d7ae1318f83045ff42ef261dbb93c5b4fd3ba963e12cf68d6"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk17_linux_ppc64le_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:372:23: in rules_java_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:357:34: in remote_jdk17_repos\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk17_linux_ppc64le_toolchain_config_repo",
               "generator_name": "remotejdk17_linux_ppc64le_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:ppc\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux_ppc64le//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:ppc\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux_ppc64le//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk17_linux_ppc64le_toolchain_config_repo",
                         "generator_name": "remotejdk17_linux_ppc64le_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:ppc\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux_ppc64le//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:ppc\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux_ppc64le//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "fdc8ae00f2436bfc46b2f54c84f2bd84122787ede232a4d61ffc284bfe6f61ec"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk17_linux_aarch64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:372:23: in rules_java_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:357:34: in remote_jdk17_repos\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk17_linux_aarch64_toolchain_config_repo",
               "generator_name": "remotejdk17_linux_aarch64_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux_aarch64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux_aarch64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk17_linux_aarch64_toolchain_config_repo",
                         "generator_name": "remotejdk17_linux_aarch64_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux_aarch64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux_aarch64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "b169b01ac1a169d7eb5e3525454c3e408e9127993ac0f578dc2c5ad183fd4e3e"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk17_linux_s390x_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:372:23: in rules_java_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:357:34: in remote_jdk17_repos\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk17_linux_s390x_toolchain_config_repo",
               "generator_name": "remotejdk17_linux_s390x_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux_s390x//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux_s390x//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk17_linux_s390x_toolchain_config_repo",
                         "generator_name": "remotejdk17_linux_s390x_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux_s390x//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux_s390x//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "6ba1870e09fccfdcd423f4169b966a73f8e9deaff859ec6fb3b626ed61ebd8b5"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remote_jdk8_linux_s390x_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:370:22: in rules_java_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:349:34: in remote_jdk8_repos\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remote_jdk8_linux_s390x_toolchain_config_repo",
               "generator_name": "remote_jdk8_linux_s390x_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_8\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"8\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_linux_s390x//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_linux_s390x//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remote_jdk8_linux_s390x_toolchain_config_repo",
                         "generator_name": "remote_jdk8_linux_s390x_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_8\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"8\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_linux_s390x//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_linux_s390x//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "f1e3f0b4884e21863a7c19a3a12a8995ed4162e02bd07cbb61b42799fc2d7359"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk21_win_arm64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:373:23: in rules_java_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:361:34: in remote_jdk21_repos\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk21_win_arm64_toolchain_config_repo",
               "generator_name": "remotejdk21_win_arm64_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_21\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"21\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_win_arm64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_win_arm64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk21_win_arm64_toolchain_config_repo",
                         "generator_name": "remotejdk21_win_arm64_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_21\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"21\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_win_arm64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_win_arm64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "9bbdbb329eeba27bc482582360abc6e3351d9a9a07ee11cba3a0026c90223e85"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk17_linux_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:372:23: in rules_java_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:357:34: in remote_jdk17_repos\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk17_linux_toolchain_config_repo",
               "generator_name": "remotejdk17_linux_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk17_linux_toolchain_config_repo",
                         "generator_name": "remotejdk17_linux_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "f0f07fe0f645f2dc7b8c9953c7962627e1c7425cc52f543729dbff16cd20e461"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk17_macos_aarch64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:372:23: in rules_java_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:357:34: in remote_jdk17_repos\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk17_macos_aarch64_toolchain_config_repo",
               "generator_name": "remotejdk17_macos_aarch64_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_macos_aarch64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_macos_aarch64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk17_macos_aarch64_toolchain_config_repo",
                         "generator_name": "remotejdk17_macos_aarch64_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_macos_aarch64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_macos_aarch64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "0eb17f6d969bc665a21e55d29eb51e88a067159ee62cf5094b17658a07d3accb"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk17_win_arm64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:372:23: in rules_java_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:357:34: in remote_jdk17_repos\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk17_win_arm64_toolchain_config_repo",
               "generator_name": "remotejdk17_win_arm64_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_win_arm64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_win_arm64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk17_win_arm64_toolchain_config_repo",
                         "generator_name": "remotejdk17_win_arm64_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_win_arm64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_win_arm64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "86b129d9c464a9b08f97eca7d8bc5bdb3676b581f8aac044451dbdfaa49e69d3"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remote_jdk8_windows_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:370:22: in rules_java_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:349:34: in remote_jdk8_repos\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remote_jdk8_windows_toolchain_config_repo",
               "generator_name": "remote_jdk8_windows_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_8\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"8\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_windows//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_windows//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remote_jdk8_windows_toolchain_config_repo",
                         "generator_name": "remote_jdk8_windows_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_8\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"8\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_windows//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_windows//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "8d0b08c18f215c185d64efe72054a5ffef36325906c34ebf1d3c710d4ba5c685"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/cpp:cc_configure.bzl%cc_autoconf_toolchains",
          "definition_information": "Repository local_config_cc_toolchains instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:181:13: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/cpp/cc_configure.bzl:148:27: in cc_configure\nRepository rule cc_autoconf_toolchains defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/cpp/cc_configure.bzl:47:41: in <toplevel>\n",
          "original_attributes": {
               "name": "local_config_cc_toolchains",
               "generator_name": "local_config_cc_toolchains",
               "generator_function": "cc_configure",
               "generator_location": None
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/cpp:cc_configure.bzl%cc_autoconf_toolchains",
                    "attributes": {
                         "name": "local_config_cc_toolchains",
                         "generator_name": "local_config_cc_toolchains",
                         "generator_function": "cc_configure",
                         "generator_location": None
                    },
                    "output_tree_hash": "f95f3d84ac75b4a4d9817af803f1d998a755bd9c20c700c79fa82cb159e98cfc"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/sh:sh_configure.bzl%sh_config",
          "definition_information": "Repository local_config_sh instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:187:13: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/sh/sh_configure.bzl:83:14: in sh_configure\nRepository rule sh_config defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/sh/sh_configure.bzl:72:28: in <toplevel>\n",
          "original_attributes": {
               "name": "local_config_sh",
               "generator_name": "local_config_sh",
               "generator_function": "sh_configure",
               "generator_location": None
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/sh:sh_configure.bzl%sh_config",
                    "attributes": {
                         "name": "local_config_sh",
                         "generator_name": "local_config_sh",
                         "generator_function": "sh_configure",
                         "generator_location": None
                    },
                    "output_tree_hash": "7bf5ba89669bcdf4526f821bc9f1f9f49409ae9c61c4e8f21c9f17e06c475127"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk11_linux_ppc64le_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:371:23: in rules_java_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:353:34: in remote_jdk11_repos\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk11_linux_ppc64le_toolchain_config_repo",
               "generator_name": "remotejdk11_linux_ppc64le_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:ppc\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_ppc64le//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:ppc\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_ppc64le//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk11_linux_ppc64le_toolchain_config_repo",
                         "generator_name": "remotejdk11_linux_ppc64le_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:ppc\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_ppc64le//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:ppc\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_ppc64le//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "3272b586976beea589d09ea8029fd5d714da40127c8850e3480991c2440c5825"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk17_win_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:372:23: in rules_java_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:357:34: in remote_jdk17_repos\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk17_win_toolchain_config_repo",
               "generator_name": "remotejdk17_win_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_win//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_win//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk17_win_toolchain_config_repo",
                         "generator_name": "remotejdk17_win_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_win//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_win//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "170c3c9a35e502555dc9f04b345e064880acbf7df935f673154011356f4aad34"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk21_macos_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:373:23: in rules_java_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:361:34: in remote_jdk21_repos\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk21_macos_toolchain_config_repo",
               "generator_name": "remotejdk21_macos_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_21\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"21\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_macos//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_macos//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk21_macos_toolchain_config_repo",
                         "generator_name": "remotejdk21_macos_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_21\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"21\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_macos//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_macos//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "434446eddb7f6a3dcc7a2a5330ed9ab26579c5142c19866b197475a695fbb32f"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk21_win_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:373:23: in rules_java_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:361:34: in remote_jdk21_repos\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk21_win_toolchain_config_repo",
               "generator_name": "remotejdk21_win_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_21\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"21\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_win//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_win//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk21_win_toolchain_config_repo",
                         "generator_name": "remotejdk21_win_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_21\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"21\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_win//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_win//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "87012328b07a779503deec0ef47132a0de50efd69afe7df87619bcc07b1dc4ed"
               }
          ]
     },
     {
          "original_rule_class": "@@build_bazel_apple_support//crosstool:setup.bzl%_apple_cc_autoconf_toolchains",
          "definition_information": "Repository local_config_apple_cc_toolchains instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:54:15: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace0.bzl:127:31: in workspace\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/build_bazel_apple_support/lib/repositories.bzl:59:23: in apple_support_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/build_bazel_apple_support/crosstool/setup.bzl:72:34: in apple_cc_configure\nRepository rule _apple_cc_autoconf_toolchains defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/build_bazel_apple_support/crosstool/setup.bzl:30:48: in <toplevel>\n",
          "original_attributes": {
               "name": "local_config_apple_cc_toolchains",
               "generator_name": "local_config_apple_cc_toolchains",
               "generator_function": "workspace",
               "generator_location": None
          },
          "repositories": [
               {
                    "rule_class": "@@build_bazel_apple_support//crosstool:setup.bzl%_apple_cc_autoconf_toolchains",
                    "attributes": {
                         "name": "local_config_apple_cc_toolchains",
                         "generator_name": "local_config_apple_cc_toolchains",
                         "generator_function": "workspace",
                         "generator_location": None
                    },
                    "output_tree_hash": "0ec8a982054aec9d2e41b47379c80fed3bbec8d463264cc4146886ab81342d36"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk11_linux_s390x_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:371:23: in rules_java_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:353:34: in remote_jdk11_repos\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk11_linux_s390x_toolchain_config_repo",
               "generator_name": "remotejdk11_linux_s390x_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_s390x//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_s390x//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk11_linux_s390x_toolchain_config_repo",
                         "generator_name": "remotejdk11_linux_s390x_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_s390x//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_s390x//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "244e11245106a8495ac4744a90023b87008e3e553766ba11d47a9fe5b4bb408d"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk21_linux_ppc64le_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:373:23: in rules_java_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:361:34: in remote_jdk21_repos\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk21_linux_ppc64le_toolchain_config_repo",
               "generator_name": "remotejdk21_linux_ppc64le_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_21\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"21\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:ppc\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_linux_ppc64le//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:ppc\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_linux_ppc64le//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk21_linux_ppc64le_toolchain_config_repo",
                         "generator_name": "remotejdk21_linux_ppc64le_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_21\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"21\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:ppc\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_linux_ppc64le//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:ppc\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_linux_ppc64le//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "7886e497d586c3f3c8225685281b0940e9aa699af208dc98de3db8839e197be3"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk21_linux_aarch64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:373:23: in rules_java_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:361:34: in remote_jdk21_repos\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk21_linux_aarch64_toolchain_config_repo",
               "generator_name": "remotejdk21_linux_aarch64_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_21\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"21\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_linux_aarch64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_linux_aarch64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk21_linux_aarch64_toolchain_config_repo",
                         "generator_name": "remotejdk21_linux_aarch64_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_21\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"21\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_linux_aarch64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_linux_aarch64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "bb33021f243382d2fb849ec204c5c8be5083c37e081df71d34a84324687cf001"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk21_linux_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:373:23: in rules_java_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:361:34: in remote_jdk21_repos\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk21_linux_toolchain_config_repo",
               "generator_name": "remotejdk21_linux_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_21\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"21\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_linux//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_linux//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk21_linux_toolchain_config_repo",
                         "generator_name": "remotejdk21_linux_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_21\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"21\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_linux//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_linux//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "ee548ad054c9b75286ff3cd19792e433a2d1236378d3a0d8076fca0bb1a88e05"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk21_macos_aarch64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:373:23: in rules_java_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:361:34: in remote_jdk21_repos\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk21_macos_aarch64_toolchain_config_repo",
               "generator_name": "remotejdk21_macos_aarch64_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_21\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"21\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_macos_aarch64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_macos_aarch64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk21_macos_aarch64_toolchain_config_repo",
                         "generator_name": "remotejdk21_macos_aarch64_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_21\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"21\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_macos_aarch64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_macos_aarch64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "706d910cc6809ea7f77fa4f938a4f019dd90d9dad927fb804a14b04321300a36"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remote_jdk8_macos_aarch64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:370:22: in rules_java_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:349:34: in remote_jdk8_repos\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remote_jdk8_macos_aarch64_toolchain_config_repo",
               "generator_name": "remote_jdk8_macos_aarch64_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_8\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"8\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_macos_aarch64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_macos_aarch64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remote_jdk8_macos_aarch64_toolchain_config_repo",
                         "generator_name": "remote_jdk8_macos_aarch64_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_8\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"8\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_macos_aarch64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_macos_aarch64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "4d721d8b0731cfb50f963f8b55c7bef9f572de0e2f251f07a12c722ef1acbb2f"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk11_linux_aarch64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:371:23: in rules_java_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:353:34: in remote_jdk11_repos\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk11_linux_aarch64_toolchain_config_repo",
               "generator_name": "remotejdk11_linux_aarch64_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_aarch64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_aarch64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk11_linux_aarch64_toolchain_config_repo",
                         "generator_name": "remotejdk11_linux_aarch64_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_aarch64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_aarch64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "bef508c068dd47d605f62c53ab0628f1f7f5101fdcc8ada09b2067b36c47931f"
               }
          ]
     },
     {
          "original_rule_class": "@@tsl//third_party/py:python_configure.bzl%local_python_configure",
          "definition_information": "Repository local_execution_config_python instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:46:15: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace2.bzl:164:19: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:594:19: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:65:27: in _tf_toolchains\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tools/toolchains/remote_config/configs.bzl:6:28: in initialize_rbe_configs\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tools/toolchains/remote_config/rbe_config.bzl:90:27: in _tensorflow_local_config\nRepository rule local_python_configure defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/py/python_configure.bzl:33:41: in <toplevel>\n",
          "original_attributes": {
               "name": "local_execution_config_python",
               "generator_name": "local_execution_config_python",
               "generator_function": "workspace",
               "generator_location": None,
               "platform_constraint": "@local_execution_config_platform//:platform_constraint"
          },
          "repositories": [
               {
                    "rule_class": "@@tsl//third_party/py:python_configure.bzl%local_python_configure",
                    "attributes": {
                         "name": "local_execution_config_python",
                         "generator_name": "local_execution_config_python",
                         "generator_function": "workspace",
                         "generator_location": None,
                         "platform_constraint": "@local_execution_config_platform//:platform_constraint"
                    },
                    "output_tree_hash": "8f8c2f619f8ff714593a0af5e65cff3ff673ed26ab2ae462bd7069d74eaa2d24"
               }
          ]
     },
     {
          "original_rule_class": "@@tsl//third_party/py:python_configure.bzl%python_configure",
          "definition_information": "Repository local_config_python instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:46:15: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace2.bzl:164:19: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:594:19: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:73:21: in _tf_toolchains\nRepository rule python_configure defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/py/python_configure.bzl:51:35: in <toplevel>\n",
          "original_attributes": {
               "name": "local_config_python",
               "generator_name": "local_config_python",
               "generator_function": "workspace",
               "generator_location": None
          },
          "repositories": [
               {
                    "rule_class": "@@tsl//third_party/py:python_configure.bzl%python_configure",
                    "attributes": {
                         "name": "local_config_python",
                         "generator_name": "local_config_python",
                         "generator_function": "workspace",
                         "generator_location": None
                    },
                    "output_tree_hash": "115bb3f98f12daeeb2d8fa67c406f976274fd0acade6fcf5953d82631036f45d"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk11_macos_aarch64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:371:23: in rules_java_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:353:34: in remote_jdk11_repos\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk11_macos_aarch64_toolchain_config_repo",
               "generator_name": "remotejdk11_macos_aarch64_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_macos_aarch64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_macos_aarch64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk11_macos_aarch64_toolchain_config_repo",
                         "generator_name": "remotejdk11_macos_aarch64_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_macos_aarch64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_macos_aarch64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "ca1d067909669aa58188026a7da06d43bdec74a3ba5c122af8a4c3660acd8d8f"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_python//python/private:toolchains_repo.bzl%toolchains_repo",
          "definition_information": "Repository python_toolchains instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:26:23: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/third_party/py/python_init_toolchains.bzl:60:35: in python_init_toolchains\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_python/python/private/python_register_toolchains.bzl:176:20: in python_register_toolchains\nRepository rule toolchains_repo defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_python/python/private/toolchains_repo.bzl:115:34: in <toplevel>\n",
          "original_attributes": {
               "name": "python_toolchains",
               "generator_name": "python_toolchains",
               "generator_function": "python_init_toolchains",
               "generator_location": None,
               "platforms": [
                    "aarch64-apple-darwin",
                    "aarch64-unknown-linux-gnu",
                    "ppc64le-unknown-linux-gnu",
                    "s390x-unknown-linux-gnu",
                    "x86_64-apple-darwin",
                    "x86_64-pc-windows-msvc",
                    "x86_64-unknown-linux-gnu"
               ],
               "python_version": "3.11.10",
               "set_python_version_constraint": False,
               "user_repository_name": "python"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_python//python/private:toolchains_repo.bzl%toolchains_repo",
                    "attributes": {
                         "name": "python_toolchains",
                         "generator_name": "python_toolchains",
                         "generator_function": "python_init_toolchains",
                         "generator_location": None,
                         "platforms": [
                              "aarch64-apple-darwin",
                              "aarch64-unknown-linux-gnu",
                              "ppc64le-unknown-linux-gnu",
                              "s390x-unknown-linux-gnu",
                              "x86_64-apple-darwin",
                              "x86_64-pc-windows-msvc",
                              "x86_64-unknown-linux-gnu"
                         ],
                         "python_version": "3.11.10",
                         "set_python_version_constraint": False,
                         "user_repository_name": "python"
                    },
                    "output_tree_hash": "f81614081cceade95fa02d203f832754e72db092625781db702f82a8227a2608"
               }
          ]
     },
     {
          "original_rule_class": "local_config_platform",
          "original_attributes": {
               "name": "local_config_platform"
          },
          "native": "local_config_platform(name = 'local_config_platform')"
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository rules_java instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:54:15: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace0.bzl:53:19: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace0.bzl:130:20: in workspace\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/com_github_grpc_grpc/bazel/grpc_extra_deps.bzl:29:18: in grpc_extra_deps\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/com_google_protobuf/protobuf_deps.bzl:68:24: in protobuf_deps\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/com_google_protobuf/protobuf_deps.bzl:19:17: in _github_archive\nRepository rule http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/http.bzl:387:31: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_java",
               "generator_name": "rules_java",
               "generator_function": "workspace",
               "generator_location": None,
               "urls": [
                    "https://github.com/bazelbuild/rules_java/archive/981f06c3d2bd10225e85209904090eb7b5fb26bd.zip"
               ],
               "sha256": "7979ece89e82546b0dcd1dff7538c34b5a6ebc9148971106f0e3705444f00665",
               "strip_prefix": "rules_java-981f06c3d2bd10225e85209904090eb7b5fb26bd"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/bazelbuild/rules_java/archive/981f06c3d2bd10225e85209904090eb7b5fb26bd.zip"
                         ],
                         "sha256": "7979ece89e82546b0dcd1dff7538c34b5a6ebc9148971106f0e3705444f00665",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "rules_java-981f06c3d2bd10225e85209904090eb7b5fb26bd",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "rules_java"
                    },
                    "output_tree_hash": "da2ec8d78f7273154d4b7eeb3fe6aeeeddd71330cdc8c5593e3e3d060e0fa465"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository rules_proto instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:54:15: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace0.bzl:114:17: in workspace\nRepository rule http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/http.bzl:387:31: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_proto",
               "generator_name": "rules_proto",
               "generator_function": "workspace",
               "generator_location": None,
               "urls": [
                    "https://storage.googleapis.com/mirror.tensorflow.org/github.com/bazelbuild/rules_proto/archive/11bf7c25e666dd7ddacbcd4d4c4a9de7a25175f8.tar.gz",
                    "https://github.com/bazelbuild/rules_proto/archive/11bf7c25e666dd7ddacbcd4d4c4a9de7a25175f8.tar.gz"
               ],
               "sha256": "20b240eba17a36be4b0b22635aca63053913d5c1ee36e16be36499d167a2f533",
               "strip_prefix": "rules_proto-11bf7c25e666dd7ddacbcd4d4c4a9de7a25175f8"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://storage.googleapis.com/mirror.tensorflow.org/github.com/bazelbuild/rules_proto/archive/11bf7c25e666dd7ddacbcd4d4c4a9de7a25175f8.tar.gz",
                              "https://github.com/bazelbuild/rules_proto/archive/11bf7c25e666dd7ddacbcd4d4c4a9de7a25175f8.tar.gz"
                         ],
                         "sha256": "20b240eba17a36be4b0b22635aca63053913d5c1ee36e16be36499d167a2f533",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "rules_proto-11bf7c25e666dd7ddacbcd4d4c4a9de7a25175f8",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "rules_proto"
                    },
                    "output_tree_hash": "e2913701562f2b46ad300ed62d4387619662379b97b3cd6b9a3b9da499febfca"
               }
          ]
     },
     {
          "original_rule_class": "@@tsl//third_party:repo.bzl%_tf_http_archive",
          "definition_information": "Repository absl_py instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:46:15: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace2.bzl:164:19: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:604:21: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:265:20: in _tf_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/repo.bzl:136:21: in tf_http_archive\nRepository rule _tf_http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/repo.bzl:89:35: in <toplevel>\n",
          "original_attributes": {
               "name": "absl_py",
               "generator_name": "absl_py",
               "generator_function": "workspace",
               "generator_location": None,
               "sha256": "a7c51b2a0aa6357a9cbb2d9437e8cd787200531867dc02565218930b6a32166e",
               "urls": [
                    "https://storage.googleapis.com/mirror.tensorflow.org/github.com/abseil/abseil-py/archive/refs/tags/v1.0.0.tar.gz",
                    "https://github.com/abseil/abseil-py/archive/refs/tags/v1.0.0.tar.gz"
               ],
               "strip_prefix": "abseil-py-1.0.0",
               "system_build_file": "@tsl//third_party/systemlibs:absl_py.BUILD",
               "system_link_files": {
                    "@tsl//third_party/systemlibs:absl_py.absl.BUILD": "absl/BUILD",
                    "@tsl//third_party/systemlibs:absl_py.absl.flags.BUILD": "absl/flags/BUILD",
                    "@tsl//third_party/systemlibs:absl_py.absl.testing.BUILD": "absl/testing/BUILD",
                    "@tsl//third_party/systemlibs:absl_py.absl.logging.BUILD": "absl/logging/BUILD"
               }
          },
          "repositories": [
               {
                    "rule_class": "@@tsl//third_party:repo.bzl%_tf_http_archive",
                    "attributes": {
                         "name": "absl_py",
                         "generator_name": "absl_py",
                         "generator_function": "workspace",
                         "generator_location": None,
                         "sha256": "a7c51b2a0aa6357a9cbb2d9437e8cd787200531867dc02565218930b6a32166e",
                         "urls": [
                              "https://storage.googleapis.com/mirror.tensorflow.org/github.com/abseil/abseil-py/archive/refs/tags/v1.0.0.tar.gz",
                              "https://github.com/abseil/abseil-py/archive/refs/tags/v1.0.0.tar.gz"
                         ],
                         "strip_prefix": "abseil-py-1.0.0",
                         "system_build_file": "@tsl//third_party/systemlibs:absl_py.BUILD",
                         "system_link_files": {
                              "@tsl//third_party/systemlibs:absl_py.absl.BUILD": "absl/BUILD",
                              "@tsl//third_party/systemlibs:absl_py.absl.flags.BUILD": "absl/flags/BUILD",
                              "@tsl//third_party/systemlibs:absl_py.absl.testing.BUILD": "absl/testing/BUILD",
                              "@tsl//third_party/systemlibs:absl_py.absl.logging.BUILD": "absl/logging/BUILD"
                         }
                    },
                    "output_tree_hash": "b5e614a9e11fa065d868771ef21f9f95be6f681103ad176f924e8bd315edd12d"
               }
          ]
     },
     {
          "original_rule_class": "@@tsl//third_party:repo.bzl%_tf_http_archive",
          "definition_information": "Repository ml_dtypes_py instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:46:15: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace2.bzl:164:19: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:597:28: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:51:14: in _initialize_third_party\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/py/ml_dtypes/workspace.bzl:12:20: in repo\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/repo.bzl:136:21: in tf_http_archive\nRepository rule _tf_http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/repo.bzl:89:35: in <toplevel>\n",
          "original_attributes": {
               "name": "ml_dtypes_py",
               "generator_name": "ml_dtypes_py",
               "generator_function": "workspace",
               "generator_location": None,
               "sha256": "f6e5880666661351e6cd084ac4178ddc4dabcde7e9a73722981c0d1500cf5937",
               "urls": [
                    "https://storage.googleapis.com/mirror.tensorflow.org/github.com/jax-ml/ml_dtypes/archive/00d98cd92ade342fef589c0470379abb27baebe9/ml_dtypes-00d98cd92ade342fef589c0470379abb27baebe9.tar.gz",
                    "https://github.com/jax-ml/ml_dtypes/archive/00d98cd92ade342fef589c0470379abb27baebe9/ml_dtypes-00d98cd92ade342fef589c0470379abb27baebe9.tar.gz"
               ],
               "strip_prefix": "ml_dtypes-00d98cd92ade342fef589c0470379abb27baebe9",
               "build_file": "//third_party/py/ml_dtypes:ml_dtypes_py.BUILD",
               "link_files": {
                    "//third_party/py/ml_dtypes:ml_dtypes.BUILD": "ml_dtypes/BUILD.bazel"
               }
          },
          "repositories": [
               {
                    "rule_class": "@@tsl//third_party:repo.bzl%_tf_http_archive",
                    "attributes": {
                         "name": "ml_dtypes_py",
                         "generator_name": "ml_dtypes_py",
                         "generator_function": "workspace",
                         "generator_location": None,
                         "sha256": "f6e5880666661351e6cd084ac4178ddc4dabcde7e9a73722981c0d1500cf5937",
                         "urls": [
                              "https://storage.googleapis.com/mirror.tensorflow.org/github.com/jax-ml/ml_dtypes/archive/00d98cd92ade342fef589c0470379abb27baebe9/ml_dtypes-00d98cd92ade342fef589c0470379abb27baebe9.tar.gz",
                              "https://github.com/jax-ml/ml_dtypes/archive/00d98cd92ade342fef589c0470379abb27baebe9/ml_dtypes-00d98cd92ade342fef589c0470379abb27baebe9.tar.gz"
                         ],
                         "strip_prefix": "ml_dtypes-00d98cd92ade342fef589c0470379abb27baebe9",
                         "build_file": "//third_party/py/ml_dtypes:ml_dtypes_py.BUILD",
                         "link_files": {
                              "//third_party/py/ml_dtypes:ml_dtypes.BUILD": "ml_dtypes/BUILD.bazel"
                         }
                    },
                    "output_tree_hash": "a571d2456a611c612b8b097522022d993f0410a87a459a8872765cf437ee086a"
               }
          ]
     },
     {
          "original_rule_class": "@@upb//bazel:repository_defs.bzl%bazel_version_repository",
          "definition_information": "Repository bazel_version instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:54:15: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace0.bzl:53:19: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace0.bzl:130:20: in workspace\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/com_github_grpc_grpc/bazel/grpc_extra_deps.bzl:31:13: in grpc_extra_deps\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/upb/bazel/workspace_deps.bzl:7:29: in upb_deps\nRepository rule bazel_version_repository defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/upb/bazel/repository_defs.bzl:12:43: in <toplevel>\n",
          "original_attributes": {
               "name": "bazel_version",
               "generator_name": "bazel_version",
               "generator_function": "workspace",
               "generator_location": None
          },
          "repositories": [
               {
                    "rule_class": "@@upb//bazel:repository_defs.bzl%bazel_version_repository",
                    "attributes": {
                         "name": "bazel_version",
                         "generator_name": "bazel_version",
                         "generator_function": "workspace",
                         "generator_location": None
                    },
                    "output_tree_hash": "4ac1eb65ccdb480e65a77ab2fcff796a18ea84938bd83062b9e482d968818082"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository rules_license instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:50:15: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace1.bzl:12:19: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace1.bzl:16:27: in workspace\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_pkg/pkg/deps.bzl:39:10: in rules_pkg_dependencies\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\nRepository rule http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/http.bzl:387:31: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_license",
               "generator_name": "rules_license",
               "generator_function": "workspace",
               "generator_location": None,
               "urls": [
                    "https://mirror.bazel.build/github.com/bazelbuild/rules_license/releases/download/0.0.1/rules_license-0.0.1.tar.gz"
               ],
               "sha256": "4865059254da674e3d18ab242e21c17f7e3e8c6b1f1421fffa4c5070f82e98b5"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://mirror.bazel.build/github.com/bazelbuild/rules_license/releases/download/0.0.1/rules_license-0.0.1.tar.gz"
                         ],
                         "sha256": "4865059254da674e3d18ab242e21c17f7e3e8c6b1f1421fffa4c5070f82e98b5",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "rules_license"
                    },
                    "output_tree_hash": "8df21c9eb9fabf43459d1e5cb84bb8674279c5efff279340258e1786de3b99b9"
               }
          ]
     },
     {
          "original_rule_class": "@@tsl//third_party:repo.bzl%_tf_http_archive",
          "definition_information": "Repository pybind11_bazel instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:46:15: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace2.bzl:164:19: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:597:28: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:54:19: in _initialize_third_party\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/pybind11_bazel/workspace.bzl:11:20: in repo\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/repo.bzl:136:21: in tf_http_archive\nRepository rule _tf_http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/repo.bzl:89:35: in <toplevel>\n",
          "original_attributes": {
               "name": "pybind11_bazel",
               "generator_name": "pybind11_bazel",
               "generator_function": "workspace",
               "generator_location": None,
               "sha256": "516c1b3a10d87740d2b7de6f121f8e19dde2c372ecbfe59aef44cd1872c10395",
               "urls": [
                    "https://storage.googleapis.com/mirror.tensorflow.org/github.com/pybind/pybind11_bazel/archive/72cbbf1fbc830e487e3012862b7b720001b70672.tar.gz",
                    "https://github.com/pybind/pybind11_bazel/archive/72cbbf1fbc830e487e3012862b7b720001b70672.tar.gz"
               ],
               "strip_prefix": "pybind11_bazel-72cbbf1fbc830e487e3012862b7b720001b70672",
               "patch_file": [
                    "//third_party/pybind11_bazel:pybind11_bazel.patch"
               ]
          },
          "repositories": [
               {
                    "rule_class": "@@tsl//third_party:repo.bzl%_tf_http_archive",
                    "attributes": {
                         "name": "pybind11_bazel",
                         "generator_name": "pybind11_bazel",
                         "generator_function": "workspace",
                         "generator_location": None,
                         "sha256": "516c1b3a10d87740d2b7de6f121f8e19dde2c372ecbfe59aef44cd1872c10395",
                         "urls": [
                              "https://storage.googleapis.com/mirror.tensorflow.org/github.com/pybind/pybind11_bazel/archive/72cbbf1fbc830e487e3012862b7b720001b70672.tar.gz",
                              "https://github.com/pybind/pybind11_bazel/archive/72cbbf1fbc830e487e3012862b7b720001b70672.tar.gz"
                         ],
                         "strip_prefix": "pybind11_bazel-72cbbf1fbc830e487e3012862b7b720001b70672",
                         "patch_file": [
                              "//third_party/pybind11_bazel:pybind11_bazel.patch"
                         ]
                    },
                    "output_tree_hash": "e7676fa373e3c15a91c16af8662fba3cb6520ab89b0d359800361846a7c00ede"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:local_java_repository.bzl%_local_java_repository_rule",
          "definition_information": "Repository local_jdk instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:85:6: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/toolchains/local_java_repository.bzl:335:32: in local_java_repository\nRepository rule _local_java_repository_rule defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_java_builtin/toolchains/local_java_repository.bzl:290:46: in <toplevel>\n",
          "original_attributes": {
               "name": "local_jdk",
               "generator_name": "local_jdk",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file_content": "load(\"@rules_java//java:defs.bzl\", \"java_runtime\")\n\npackage(default_visibility = [\"//visibility:public\"])\n\nexports_files([\"WORKSPACE\", \"BUILD.bazel\"])\n\nfilegroup(\n    name = \"jre\",\n    srcs = glob(\n        [\n            \"jre/bin/**\",\n            \"jre/lib/**\",\n        ],\n        allow_empty = True,\n        # In some configurations, Java browser plugin is considered harmful and\n        # common antivirus software blocks access to npjp2.dll interfering with Bazel,\n        # so do not include it in JRE on Windows.\n        exclude = [\"jre/bin/plugin2/**\"],\n    ),\n)\n\nfilegroup(\n    name = \"jdk-bin\",\n    srcs = glob(\n        [\"bin/**\"],\n        # The JDK on Windows sometimes contains a directory called\n        # \"%systemroot%\", which is not a valid label.\n        exclude = [\"**/*%*/**\"],\n    ),\n)\n\n# This folder holds security policies.\nfilegroup(\n    name = \"jdk-conf\",\n    srcs = glob(\n        [\"conf/**\"],\n        allow_empty = True,\n    ),\n)\n\nfilegroup(\n    name = \"jdk-include\",\n    srcs = glob(\n        [\"include/**\"],\n        allow_empty = True,\n    ),\n)\n\nfilegroup(\n    name = \"jdk-lib\",\n    srcs = glob(\n        [\"lib/**\", \"release\"],\n        allow_empty = True,\n        exclude = [\n            \"lib/missioncontrol/**\",\n            \"lib/visualvm/**\",\n        ],\n    ),\n)\n\njava_runtime(\n    name = \"jdk\",\n    srcs = [\n        \":jdk-bin\",\n        \":jdk-conf\",\n        \":jdk-include\",\n        \":jdk-lib\",\n        \":jre\",\n    ],\n    # Provide the 'java` binary explicitly so that the correct path is used by\n    # Bazel even when the host platform differs from the execution platform.\n    # Exactly one of the two globs will be empty depending on the host platform.\n    # When --incompatible_disallow_empty_glob is enabled, each individual empty\n    # glob will fail without allow_empty = True, even if the overall result is\n    # non-empty.\n    java = glob([\"bin/java.exe\", \"bin/java\"], allow_empty = True)[0],\n    version = {RUNTIME_VERSION},\n)\n\nfilegroup(\n    name = \"jdk-jmods\",\n    srcs = glob(\n        [\"jmods/**\"],\n        allow_empty = True,\n    ),\n)\n\njava_runtime(\n    name = \"jdk-with-jmods\",\n    srcs = [\n        \":jdk-bin\",\n        \":jdk-conf\",\n        \":jdk-include\",\n        \":jdk-lib\",\n        \":jdk-jmods\",\n        \":jre\",\n    ],\n    java = glob([\"bin/java.exe\", \"bin/java\"], allow_empty = True)[0],\n    version = {RUNTIME_VERSION},\n)\n",
               "java_home": "",
               "version": ""
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:local_java_repository.bzl%_local_java_repository_rule",
                    "attributes": {
                         "name": "local_jdk",
                         "generator_name": "local_jdk",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file_content": "load(\"@rules_java//java:defs.bzl\", \"java_runtime\")\n\npackage(default_visibility = [\"//visibility:public\"])\n\nexports_files([\"WORKSPACE\", \"BUILD.bazel\"])\n\nfilegroup(\n    name = \"jre\",\n    srcs = glob(\n        [\n            \"jre/bin/**\",\n            \"jre/lib/**\",\n        ],\n        allow_empty = True,\n        # In some configurations, Java browser plugin is considered harmful and\n        # common antivirus software blocks access to npjp2.dll interfering with Bazel,\n        # so do not include it in JRE on Windows.\n        exclude = [\"jre/bin/plugin2/**\"],\n    ),\n)\n\nfilegroup(\n    name = \"jdk-bin\",\n    srcs = glob(\n        [\"bin/**\"],\n        # The JDK on Windows sometimes contains a directory called\n        # \"%systemroot%\", which is not a valid label.\n        exclude = [\"**/*%*/**\"],\n    ),\n)\n\n# This folder holds security policies.\nfilegroup(\n    name = \"jdk-conf\",\n    srcs = glob(\n        [\"conf/**\"],\n        allow_empty = True,\n    ),\n)\n\nfilegroup(\n    name = \"jdk-include\",\n    srcs = glob(\n        [\"include/**\"],\n        allow_empty = True,\n    ),\n)\n\nfilegroup(\n    name = \"jdk-lib\",\n    srcs = glob(\n        [\"lib/**\", \"release\"],\n        allow_empty = True,\n        exclude = [\n            \"lib/missioncontrol/**\",\n            \"lib/visualvm/**\",\n        ],\n    ),\n)\n\njava_runtime(\n    name = \"jdk\",\n    srcs = [\n        \":jdk-bin\",\n        \":jdk-conf\",\n        \":jdk-include\",\n        \":jdk-lib\",\n        \":jre\",\n    ],\n    # Provide the 'java` binary explicitly so that the correct path is used by\n    # Bazel even when the host platform differs from the execution platform.\n    # Exactly one of the two globs will be empty depending on the host platform.\n    # When --incompatible_disallow_empty_glob is enabled, each individual empty\n    # glob will fail without allow_empty = True, even if the overall result is\n    # non-empty.\n    java = glob([\"bin/java.exe\", \"bin/java\"], allow_empty = True)[0],\n    version = {RUNTIME_VERSION},\n)\n\nfilegroup(\n    name = \"jdk-jmods\",\n    srcs = glob(\n        [\"jmods/**\"],\n        allow_empty = True,\n    ),\n)\n\njava_runtime(\n    name = \"jdk-with-jmods\",\n    srcs = [\n        \":jdk-bin\",\n        \":jdk-conf\",\n        \":jdk-include\",\n        \":jdk-lib\",\n        \":jdk-jmods\",\n        \":jre\",\n    ],\n    java = glob([\"bin/java.exe\", \"bin/java\"], allow_empty = True)[0],\n    version = {RUNTIME_VERSION},\n)\n",
                         "java_home": "",
                         "version": ""
                    },
                    "output_tree_hash": "2d99335237224b49c0e52ac22906538e9732162d3a3defa5fe7febc597439611"
               }
          ]
     },
     {
          "original_rule_class": "@@tsl//third_party:repo.bzl%_tf_http_archive",
          "definition_information": "Repository six_archive instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:46:15: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace2.bzl:164:19: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:604:21: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:248:20: in _tf_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/repo.bzl:136:21: in tf_http_archive\nRepository rule _tf_http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/repo.bzl:89:35: in <toplevel>\n",
          "original_attributes": {
               "name": "six_archive",
               "generator_name": "six_archive",
               "generator_function": "workspace",
               "generator_location": None,
               "sha256": "1e61c37477a1626458e36f7b1d82aa5c9b094fa4802892072e49de9c60c4c926",
               "urls": [
                    "https://storage.googleapis.com/mirror.tensorflow.org/pypi.python.org/packages/source/s/six/six-1.16.0.tar.gz",
                    "https://pypi.python.org/packages/source/s/six/six-1.16.0.tar.gz"
               ],
               "strip_prefix": "six-1.16.0",
               "build_file": "//third_party:six.BUILD",
               "system_build_file": "@tsl//third_party/systemlibs:six.BUILD"
          },
          "repositories": [
               {
                    "rule_class": "@@tsl//third_party:repo.bzl%_tf_http_archive",
                    "attributes": {
                         "name": "six_archive",
                         "generator_name": "six_archive",
                         "generator_function": "workspace",
                         "generator_location": None,
                         "sha256": "1e61c37477a1626458e36f7b1d82aa5c9b094fa4802892072e49de9c60c4c926",
                         "urls": [
                              "https://storage.googleapis.com/mirror.tensorflow.org/pypi.python.org/packages/source/s/six/six-1.16.0.tar.gz",
                              "https://pypi.python.org/packages/source/s/six/six-1.16.0.tar.gz"
                         ],
                         "strip_prefix": "six-1.16.0",
                         "build_file": "//third_party:six.BUILD",
                         "system_build_file": "@tsl//third_party/systemlibs:six.BUILD"
                    },
                    "output_tree_hash": "19a71157c2bd96cb3e6279165cb528193fbf057f5abfa8166961b0d9986902e0"
               }
          ]
     },
     {
          "original_rule_class": "@@tsl//third_party:repo.bzl%_tf_http_archive",
          "definition_information": "Repository pybind11 instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:46:15: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace2.bzl:164:19: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:604:21: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:538:20: in _tf_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/repo.bzl:136:21: in tf_http_archive\nRepository rule _tf_http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/repo.bzl:89:35: in <toplevel>\n",
          "original_attributes": {
               "name": "pybind11",
               "generator_name": "pybind11",
               "generator_function": "workspace",
               "generator_location": None,
               "sha256": "efc901aa0aab439a3fea6efeaf930b5a349fb06394bf845c64ce15a9cf8f0240",
               "urls": [
                    "https://storage.googleapis.com/mirror.tensorflow.org/github.com/pybind/pybind11/archive/v2.13.4.tar.gz",
                    "https://github.com/pybind/pybind11/archive/v2.13.4.tar.gz"
               ],
               "strip_prefix": "pybind11-2.13.4",
               "build_file": "//third_party:pybind11.BUILD",
               "system_build_file": "@tsl//third_party/systemlibs:pybind11.BUILD"
          },
          "repositories": [
               {
                    "rule_class": "@@tsl//third_party:repo.bzl%_tf_http_archive",
                    "attributes": {
                         "name": "pybind11",
                         "generator_name": "pybind11",
                         "generator_function": "workspace",
                         "generator_location": None,
                         "sha256": "efc901aa0aab439a3fea6efeaf930b5a349fb06394bf845c64ce15a9cf8f0240",
                         "urls": [
                              "https://storage.googleapis.com/mirror.tensorflow.org/github.com/pybind/pybind11/archive/v2.13.4.tar.gz",
                              "https://github.com/pybind/pybind11/archive/v2.13.4.tar.gz"
                         ],
                         "strip_prefix": "pybind11-2.13.4",
                         "build_file": "//third_party:pybind11.BUILD",
                         "system_build_file": "@tsl//third_party/systemlibs:pybind11.BUILD"
                    },
                    "output_tree_hash": "49390d83e9d559807ce51cc629158284951664f4d1b33f6f67c972d0054448eb"
               }
          ]
     },
     {
          "original_rule_class": "//third_party:repo.bzl%_tf_http_archive",
          "definition_information": "Repository triton instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:46:15: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace2.bzl:171:28: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace2.bzl:32:11: in _initialize_third_party\n  /usr/local/google/home/kotlaja/bzl_mod/xla/third_party/triton/workspace.bzl:13:20: in repo\n  /usr/local/google/home/kotlaja/bzl_mod/xla/third_party/repo.bzl:138:21: in tf_http_archive\nRepository rule _tf_http_archive defined at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/third_party/repo.bzl:89:35: in <toplevel>\n",
          "original_attributes": {
               "name": "triton",
               "generator_name": "triton",
               "generator_function": "workspace",
               "generator_location": None,
               "sha256": "3c5de0e06947cc8cd6b6b06d0c28b3234f6ff72a4ae8f63c80e6d276413e5d7e",
               "urls": [
                    "https://storage.googleapis.com/mirror.tensorflow.org/github.com/openxla/triton/archive/cl722997049.tar.gz",
                    "https://github.com/openxla/triton/archive/cl722997049.tar.gz"
               ],
               "strip_prefix": "triton-cl722997049",
               "patch_file": [
                    "//third_party/triton:temporary/fix_fence_insertion_race.patch",
                    "//third_party/triton:temporary/enable_peer_access.patch",
                    "//third_party/triton:temporary/sm120.patch"
               ]
          },
          "repositories": [
               {
                    "rule_class": "//third_party:repo.bzl%_tf_http_archive",
                    "attributes": {
                         "name": "triton",
                         "generator_name": "triton",
                         "generator_function": "workspace",
                         "generator_location": None,
                         "sha256": "3c5de0e06947cc8cd6b6b06d0c28b3234f6ff72a4ae8f63c80e6d276413e5d7e",
                         "urls": [
                              "https://storage.googleapis.com/mirror.tensorflow.org/github.com/openxla/triton/archive/cl722997049.tar.gz",
                              "https://github.com/openxla/triton/archive/cl722997049.tar.gz"
                         ],
                         "strip_prefix": "triton-cl722997049",
                         "patch_file": [
                              "//third_party/triton:temporary/fix_fence_insertion_race.patch",
                              "//third_party/triton:temporary/enable_peer_access.patch",
                              "//third_party/triton:temporary/sm120.patch"
                         ]
                    },
                    "output_tree_hash": "feae0991e87497790ac989bd2c54b0f19574b079c899dabab7907d2165fe2242"
               }
          ]
     },
     {
          "original_rule_class": "@@tsl//third_party:repo.bzl%_tf_http_archive",
          "definition_information": "Repository llvm_openmp instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:46:15: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace2.bzl:164:19: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:604:21: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:355:20: in _tf_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/repo.bzl:136:21: in tf_http_archive\nRepository rule _tf_http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/repo.bzl:89:35: in <toplevel>\n",
          "original_attributes": {
               "name": "llvm_openmp",
               "generator_name": "llvm_openmp",
               "generator_function": "workspace",
               "generator_location": None,
               "sha256": "d19f728c8e04fb1e94566c8d76aef50ec926cd2f95ef3bf1e0a5de4909b28b44",
               "urls": [
                    "https://storage.googleapis.com/mirror.tensorflow.org/github.com/llvm/llvm-project/releases/download/llvmorg-10.0.1/openmp-10.0.1.src.tar.xz",
                    "https://github.com/llvm/llvm-project/releases/download/llvmorg-10.0.1/openmp-10.0.1.src.tar.xz"
               ],
               "strip_prefix": "openmp-10.0.1.src",
               "patch_file": [
                    "@tsl//third_party/llvm_openmp:openmp_switch_default_patch.patch"
               ],
               "build_file": "@tsl//third_party/llvm_openmp:BUILD"
          },
          "repositories": [
               {
                    "rule_class": "@@tsl//third_party:repo.bzl%_tf_http_archive",
                    "attributes": {
                         "name": "llvm_openmp",
                         "generator_name": "llvm_openmp",
                         "generator_function": "workspace",
                         "generator_location": None,
                         "sha256": "d19f728c8e04fb1e94566c8d76aef50ec926cd2f95ef3bf1e0a5de4909b28b44",
                         "urls": [
                              "https://storage.googleapis.com/mirror.tensorflow.org/github.com/llvm/llvm-project/releases/download/llvmorg-10.0.1/openmp-10.0.1.src.tar.xz",
                              "https://github.com/llvm/llvm-project/releases/download/llvmorg-10.0.1/openmp-10.0.1.src.tar.xz"
                         ],
                         "strip_prefix": "openmp-10.0.1.src",
                         "patch_file": [
                              "@tsl//third_party/llvm_openmp:openmp_switch_default_patch.patch"
                         ],
                         "build_file": "@tsl//third_party/llvm_openmp:BUILD"
                    },
                    "output_tree_hash": "e2df8b1b2eafd89772072ae1bc41f980a93f3fe7c282da0b774bbb1cc6126542"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository protobuf instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:18:25: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/third_party/py/python_init_repositories.bzl:23:20: in python_init_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_python/python/private/py_repositories.bzl:64:17: in py_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_python/python/private/py_repositories.bzl:25:10: in http_archive\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\nRepository rule http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/http.bzl:387:31: in <toplevel>\n",
          "original_attributes": {
               "name": "protobuf",
               "generator_name": "protobuf",
               "generator_function": "python_init_repositories",
               "generator_location": None,
               "url": "https://github.com/protocolbuffers/protobuf/releases/download/v27.0/protobuf-27.0.tar.gz",
               "sha256": "da288bf1daa6c04d03a9051781caa52aceb9163586bff9aa6cfb12f69b9395aa",
               "strip_prefix": "protobuf-27.0"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://github.com/protocolbuffers/protobuf/releases/download/v27.0/protobuf-27.0.tar.gz",
                         "urls": [],
                         "sha256": "da288bf1daa6c04d03a9051781caa52aceb9163586bff9aa6cfb12f69b9395aa",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "protobuf-27.0",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "protobuf"
                    },
                    "output_tree_hash": "991ce48949a481a11e94a196025e77f88be5bff424ddd63b4677df9bf3fa6a6a"
               }
          ]
     },
     {
          "original_rule_class": "//third_party:repo.bzl%_tf_http_archive",
          "definition_information": "Repository stablehlo instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:46:15: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace2.bzl:171:28: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace2.bzl:31:14: in _initialize_third_party\n  /usr/local/google/home/kotlaja/bzl_mod/xla/third_party/stablehlo/workspace.bzl:11:20: in repo\n  /usr/local/google/home/kotlaja/bzl_mod/xla/third_party/repo.bzl:138:21: in tf_http_archive\nRepository rule _tf_http_archive defined at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/third_party/repo.bzl:89:35: in <toplevel>\n",
          "original_attributes": {
               "name": "stablehlo",
               "generator_name": "stablehlo",
               "generator_function": "workspace",
               "generator_location": None,
               "sha256": "3eb4968cd57544850bc3b2ea2f605501ef43e9f245aee0bf0c141d4748c2d277",
               "urls": [
                    "https://storage.googleapis.com/mirror.tensorflow.org/github.com/openxla/stablehlo/archive/04c5a341abe43f50ea2f8eca97fcc07763230c00.zip",
                    "https://github.com/openxla/stablehlo/archive/04c5a341abe43f50ea2f8eca97fcc07763230c00.zip"
               ],
               "strip_prefix": "stablehlo-04c5a341abe43f50ea2f8eca97fcc07763230c00",
               "patch_file": [
                    "//third_party/stablehlo:temporary.patch"
               ]
          },
          "repositories": [
               {
                    "rule_class": "//third_party:repo.bzl%_tf_http_archive",
                    "attributes": {
                         "name": "stablehlo",
                         "generator_name": "stablehlo",
                         "generator_function": "workspace",
                         "generator_location": None,
                         "sha256": "3eb4968cd57544850bc3b2ea2f605501ef43e9f245aee0bf0c141d4748c2d277",
                         "urls": [
                              "https://storage.googleapis.com/mirror.tensorflow.org/github.com/openxla/stablehlo/archive/04c5a341abe43f50ea2f8eca97fcc07763230c00.zip",
                              "https://github.com/openxla/stablehlo/archive/04c5a341abe43f50ea2f8eca97fcc07763230c00.zip"
                         ],
                         "strip_prefix": "stablehlo-04c5a341abe43f50ea2f8eca97fcc07763230c00",
                         "patch_file": [
                              "//third_party/stablehlo:temporary.patch"
                         ]
                    },
                    "output_tree_hash": "d0d2ca77116bcfda72e34fd119b485b8ce14c14c5d24683ee568f180494fedf3"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_python//python/private:python_repository.bzl%python_repository",
          "definition_information": "Repository python_x86_64-unknown-linux-gnu instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:26:23: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/third_party/py/python_init_toolchains.bzl:60:35: in python_init_toolchains\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_python/python/private/python_register_toolchains.bzl:133:26: in python_register_toolchains\nRepository rule python_repository defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_python/python/private/python_repository.bzl:299:36: in <toplevel>\n",
          "original_attributes": {
               "name": "python_x86_64-unknown-linux-gnu",
               "generator_name": "python_x86_64-unknown-linux-gnu",
               "generator_function": "python_init_toolchains",
               "generator_location": None,
               "ignore_root_user_error": True,
               "patches": [],
               "platform": "x86_64-unknown-linux-gnu",
               "python_version": "3.11.10",
               "release_filename": "20241016/cpython-3.11.10+20241016-x86_64-unknown-linux-gnu-install_only.tar.gz",
               "sha256": "8b50a442b04724a24c1eebb65a36a0c0e833d35374dbdf9c9470d8a97b164cd9",
               "strip_prefix": "python",
               "urls": [
                    "https://github.com/indygreg/python-build-standalone/releases/download/20241016/cpython-3.11.10+20241016-x86_64-unknown-linux-gnu-install_only.tar.gz"
               ]
          },
          "repositories": [
               {
                    "rule_class": "@@rules_python//python/private:python_repository.bzl%python_repository",
                    "attributes": {
                         "auth_patterns": {},
                         "coverage_tool": "",
                         "distutils": None,
                         "distutils_content": "",
                         "ignore_root_user_error": True,
                         "name": "python_x86_64-unknown-linux-gnu",
                         "netrc": "",
                         "patch_strip": 1,
                         "patches": [],
                         "platform": "x86_64-unknown-linux-gnu",
                         "python_version": "3.11.10",
                         "release_filename": "20241016/cpython-3.11.10+20241016-x86_64-unknown-linux-gnu-install_only.tar.gz",
                         "sha256": "8b50a442b04724a24c1eebb65a36a0c0e833d35374dbdf9c9470d8a97b164cd9",
                         "strip_prefix": "python",
                         "urls": [
                              "https://github.com/indygreg/python-build-standalone/releases/download/20241016/cpython-3.11.10+20241016-x86_64-unknown-linux-gnu-install_only.tar.gz"
                         ]
                    },
                    "output_tree_hash": "d8b7b360ed33ac7f4aa0b62364c5300fd5d4b668cdb7a7cd46630bfaf88df54d"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__build instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:18:25: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/third_party/py/python_init_repositories.bzl:23:20: in python_init_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_python/python/private/py_repositories.bzl:70:14: in py_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_python/python/private/pypi/deps.bzl:133:14: in pypi_deps\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\nRepository rule http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/http.bzl:387:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__build",
               "generator_name": "pypi__build",
               "generator_function": "python_init_repositories",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/e2/03/f3c8ba0a6b6e30d7d18c40faab90807c9bb5e9a1e3b2fe2008af624a9c97/build-1.2.1-py3-none-any.whl",
               "sha256": "75e10f767a433d9a86e50d83f418e83efc18ede923ee5ff7df93b6cb0306c5d4",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\nload(\"@rules_python//python/private:glob_excludes.bzl\", \"glob_excludes\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude to avoid non-determinism.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ] + glob_excludes.version_dependent_exclusions()),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/e2/03/f3c8ba0a6b6e30d7d18c40faab90807c9bb5e9a1e3b2fe2008af624a9c97/build-1.2.1-py3-none-any.whl",
                         "urls": [],
                         "sha256": "75e10f767a433d9a86e50d83f418e83efc18ede923ee5ff7df93b6cb0306c5d4",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\nload(\"@rules_python//python/private:glob_excludes.bzl\", \"glob_excludes\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude to avoid non-determinism.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ] + glob_excludes.version_dependent_exclusions()),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__build"
                    },
                    "output_tree_hash": "333f137ceb01653f3256d554cc72ee1a511dd3a85fd8cd2f5dee52020d04b634"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__click instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:18:25: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/third_party/py/python_init_repositories.bzl:23:20: in python_init_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_python/python/private/py_repositories.bzl:70:14: in py_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_python/python/private/pypi/deps.bzl:133:14: in pypi_deps\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\nRepository rule http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/http.bzl:387:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__click",
               "generator_name": "pypi__click",
               "generator_function": "python_init_repositories",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/00/2e/d53fa4befbf2cfa713304affc7ca780ce4fc1fd8710527771b58311a3229/click-8.1.7-py3-none-any.whl",
               "sha256": "ae74fb96c20a0277a1d615f1e4d73c8414f5a98db8b799a7931d1582f3390c28",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\nload(\"@rules_python//python/private:glob_excludes.bzl\", \"glob_excludes\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude to avoid non-determinism.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ] + glob_excludes.version_dependent_exclusions()),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/00/2e/d53fa4befbf2cfa713304affc7ca780ce4fc1fd8710527771b58311a3229/click-8.1.7-py3-none-any.whl",
                         "urls": [],
                         "sha256": "ae74fb96c20a0277a1d615f1e4d73c8414f5a98db8b799a7931d1582f3390c28",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\nload(\"@rules_python//python/private:glob_excludes.bzl\", \"glob_excludes\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude to avoid non-determinism.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ] + glob_excludes.version_dependent_exclusions()),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__click"
                    },
                    "output_tree_hash": "a1c79d316ad6fd09772ead9542e0b0d42f60eb39c68d1fea5b8ba6852816a16d"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__colorama instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:18:25: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/third_party/py/python_init_repositories.bzl:23:20: in python_init_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_python/python/private/py_repositories.bzl:70:14: in py_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_python/python/private/pypi/deps.bzl:133:14: in pypi_deps\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\nRepository rule http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/http.bzl:387:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__colorama",
               "generator_name": "pypi__colorama",
               "generator_function": "python_init_repositories",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/d1/d6/3965ed04c63042e047cb6a3e6ed1a63a35087b6a609aa3a15ed8ac56c221/colorama-0.4.6-py2.py3-none-any.whl",
               "sha256": "4f1d9991f5acc0ca119f9d443620b77f9d6b33703e51011c16baf57afb285fc6",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\nload(\"@rules_python//python/private:glob_excludes.bzl\", \"glob_excludes\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude to avoid non-determinism.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ] + glob_excludes.version_dependent_exclusions()),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/d1/d6/3965ed04c63042e047cb6a3e6ed1a63a35087b6a609aa3a15ed8ac56c221/colorama-0.4.6-py2.py3-none-any.whl",
                         "urls": [],
                         "sha256": "4f1d9991f5acc0ca119f9d443620b77f9d6b33703e51011c16baf57afb285fc6",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\nload(\"@rules_python//python/private:glob_excludes.bzl\", \"glob_excludes\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude to avoid non-determinism.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ] + glob_excludes.version_dependent_exclusions()),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__colorama"
                    },
                    "output_tree_hash": "900738f2ceaf732a88b47f763f03e4a59bf44915f6cb55ef1901cf8373a85212"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__importlib_metadata instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:18:25: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/third_party/py/python_init_repositories.bzl:23:20: in python_init_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_python/python/private/py_repositories.bzl:70:14: in py_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_python/python/private/pypi/deps.bzl:133:14: in pypi_deps\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\nRepository rule http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/http.bzl:387:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__importlib_metadata",
               "generator_name": "pypi__importlib_metadata",
               "generator_function": "python_init_repositories",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/2d/0a/679461c511447ffaf176567d5c496d1de27cbe34a87df6677d7171b2fbd4/importlib_metadata-7.1.0-py3-none-any.whl",
               "sha256": "30962b96c0c223483ed6cc7280e7f0199feb01a0e40cfae4d4450fc6fab1f570",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\nload(\"@rules_python//python/private:glob_excludes.bzl\", \"glob_excludes\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude to avoid non-determinism.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ] + glob_excludes.version_dependent_exclusions()),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/2d/0a/679461c511447ffaf176567d5c496d1de27cbe34a87df6677d7171b2fbd4/importlib_metadata-7.1.0-py3-none-any.whl",
                         "urls": [],
                         "sha256": "30962b96c0c223483ed6cc7280e7f0199feb01a0e40cfae4d4450fc6fab1f570",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\nload(\"@rules_python//python/private:glob_excludes.bzl\", \"glob_excludes\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude to avoid non-determinism.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ] + glob_excludes.version_dependent_exclusions()),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__importlib_metadata"
                    },
                    "output_tree_hash": "df005f81346d21aa46405ac9cc59058f34e6677b9f86ea1f59575c640920b0de"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__installer instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:18:25: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/third_party/py/python_init_repositories.bzl:23:20: in python_init_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_python/python/private/py_repositories.bzl:70:14: in py_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_python/python/private/pypi/deps.bzl:133:14: in pypi_deps\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\nRepository rule http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/http.bzl:387:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__installer",
               "generator_name": "pypi__installer",
               "generator_function": "python_init_repositories",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/e5/ca/1172b6638d52f2d6caa2dd262ec4c811ba59eee96d54a7701930726bce18/installer-0.7.0-py3-none-any.whl",
               "sha256": "05d1933f0a5ba7d8d6296bb6d5018e7c94fa473ceb10cf198a92ccea19c27b53",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\nload(\"@rules_python//python/private:glob_excludes.bzl\", \"glob_excludes\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude to avoid non-determinism.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ] + glob_excludes.version_dependent_exclusions()),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/e5/ca/1172b6638d52f2d6caa2dd262ec4c811ba59eee96d54a7701930726bce18/installer-0.7.0-py3-none-any.whl",
                         "urls": [],
                         "sha256": "05d1933f0a5ba7d8d6296bb6d5018e7c94fa473ceb10cf198a92ccea19c27b53",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\nload(\"@rules_python//python/private:glob_excludes.bzl\", \"glob_excludes\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude to avoid non-determinism.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ] + glob_excludes.version_dependent_exclusions()),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__installer"
                    },
                    "output_tree_hash": "accb746c23e5ac231720cf8aa4095701ce426b0ffdcecb6ed8f5d9af7cba4b00"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__more_itertools instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:18:25: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/third_party/py/python_init_repositories.bzl:23:20: in python_init_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_python/python/private/py_repositories.bzl:70:14: in py_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_python/python/private/pypi/deps.bzl:133:14: in pypi_deps\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\nRepository rule http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/http.bzl:387:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__more_itertools",
               "generator_name": "pypi__more_itertools",
               "generator_function": "python_init_repositories",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/50/e2/8e10e465ee3987bb7c9ab69efb91d867d93959095f4807db102d07995d94/more_itertools-10.2.0-py3-none-any.whl",
               "sha256": "686b06abe565edfab151cb8fd385a05651e1fdf8f0a14191e4439283421f8684",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\nload(\"@rules_python//python/private:glob_excludes.bzl\", \"glob_excludes\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude to avoid non-determinism.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ] + glob_excludes.version_dependent_exclusions()),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/50/e2/8e10e465ee3987bb7c9ab69efb91d867d93959095f4807db102d07995d94/more_itertools-10.2.0-py3-none-any.whl",
                         "urls": [],
                         "sha256": "686b06abe565edfab151cb8fd385a05651e1fdf8f0a14191e4439283421f8684",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\nload(\"@rules_python//python/private:glob_excludes.bzl\", \"glob_excludes\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude to avoid non-determinism.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ] + glob_excludes.version_dependent_exclusions()),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__more_itertools"
                    },
                    "output_tree_hash": "a2d443d1de1cc90f4f65c9b51d24a70f6f939648bc427f0e975b81029f3b971c"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__packaging instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:18:25: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/third_party/py/python_init_repositories.bzl:23:20: in python_init_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_python/python/private/py_repositories.bzl:70:14: in py_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_python/python/private/pypi/deps.bzl:133:14: in pypi_deps\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\nRepository rule http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/http.bzl:387:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__packaging",
               "generator_name": "pypi__packaging",
               "generator_function": "python_init_repositories",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/88/ef/eb23f262cca3c0c4eb7ab1933c3b1f03d021f2c48f54763065b6f0e321be/packaging-24.2-py3-none-any.whl",
               "sha256": "09abb1bccd265c01f4a3aa3f7a7db064b36514d2cba19a2f694fe6150451a759",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\nload(\"@rules_python//python/private:glob_excludes.bzl\", \"glob_excludes\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude to avoid non-determinism.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ] + glob_excludes.version_dependent_exclusions()),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/88/ef/eb23f262cca3c0c4eb7ab1933c3b1f03d021f2c48f54763065b6f0e321be/packaging-24.2-py3-none-any.whl",
                         "urls": [],
                         "sha256": "09abb1bccd265c01f4a3aa3f7a7db064b36514d2cba19a2f694fe6150451a759",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\nload(\"@rules_python//python/private:glob_excludes.bzl\", \"glob_excludes\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude to avoid non-determinism.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ] + glob_excludes.version_dependent_exclusions()),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__packaging"
                    },
                    "output_tree_hash": "f87d36041146e1729a0c286f46882d666d11914e2b1b5244f6a0ee5003e2210f"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__pep517 instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:18:25: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/third_party/py/python_init_repositories.bzl:23:20: in python_init_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_python/python/private/py_repositories.bzl:70:14: in py_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_python/python/private/pypi/deps.bzl:133:14: in pypi_deps\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\nRepository rule http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/http.bzl:387:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__pep517",
               "generator_name": "pypi__pep517",
               "generator_function": "python_init_repositories",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/25/6e/ca4a5434eb0e502210f591b97537d322546e4833dcb4d470a48c375c5540/pep517-0.13.1-py3-none-any.whl",
               "sha256": "31b206f67165b3536dd577c5c3f1518e8fbaf38cbc57efff8369a392feff1721",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\nload(\"@rules_python//python/private:glob_excludes.bzl\", \"glob_excludes\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude to avoid non-determinism.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ] + glob_excludes.version_dependent_exclusions()),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/25/6e/ca4a5434eb0e502210f591b97537d322546e4833dcb4d470a48c375c5540/pep517-0.13.1-py3-none-any.whl",
                         "urls": [],
                         "sha256": "31b206f67165b3536dd577c5c3f1518e8fbaf38cbc57efff8369a392feff1721",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\nload(\"@rules_python//python/private:glob_excludes.bzl\", \"glob_excludes\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude to avoid non-determinism.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ] + glob_excludes.version_dependent_exclusions()),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__pep517"
                    },
                    "output_tree_hash": "82ab75f7a1b0eb150629d2e48201e1e63fff8e2648e28d6cd43c630024efa9d2"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__pip instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:18:25: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/third_party/py/python_init_repositories.bzl:23:20: in python_init_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_python/python/private/py_repositories.bzl:70:14: in py_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_python/python/private/pypi/deps.bzl:133:14: in pypi_deps\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\nRepository rule http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/http.bzl:387:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__pip",
               "generator_name": "pypi__pip",
               "generator_function": "python_init_repositories",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/ef/7d/500c9ad20238fcfcb4cb9243eede163594d7020ce87bd9610c9e02771876/pip-24.3.1-py3-none-any.whl",
               "sha256": "3790624780082365f47549d032f3770eeb2b1e8bd1f7b2e02dace1afa361b4ed",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\nload(\"@rules_python//python/private:glob_excludes.bzl\", \"glob_excludes\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude to avoid non-determinism.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ] + glob_excludes.version_dependent_exclusions()),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/ef/7d/500c9ad20238fcfcb4cb9243eede163594d7020ce87bd9610c9e02771876/pip-24.3.1-py3-none-any.whl",
                         "urls": [],
                         "sha256": "3790624780082365f47549d032f3770eeb2b1e8bd1f7b2e02dace1afa361b4ed",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\nload(\"@rules_python//python/private:glob_excludes.bzl\", \"glob_excludes\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude to avoid non-determinism.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ] + glob_excludes.version_dependent_exclusions()),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__pip"
                    },
                    "output_tree_hash": "7d6db0a257e0f50cd13e3bf2aa4867be5727c22c182d9e1353ed2b67d3db1931"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__pip_tools instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:18:25: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/third_party/py/python_init_repositories.bzl:23:20: in python_init_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_python/python/private/py_repositories.bzl:70:14: in py_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_python/python/private/pypi/deps.bzl:133:14: in pypi_deps\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\nRepository rule http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/http.bzl:387:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__pip_tools",
               "generator_name": "pypi__pip_tools",
               "generator_function": "python_init_repositories",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/0d/dc/38f4ce065e92c66f058ea7a368a9c5de4e702272b479c0992059f7693941/pip_tools-7.4.1-py3-none-any.whl",
               "sha256": "4c690e5fbae2f21e87843e89c26191f0d9454f362d8acdbd695716493ec8b3a9",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\nload(\"@rules_python//python/private:glob_excludes.bzl\", \"glob_excludes\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude to avoid non-determinism.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ] + glob_excludes.version_dependent_exclusions()),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/0d/dc/38f4ce065e92c66f058ea7a368a9c5de4e702272b479c0992059f7693941/pip_tools-7.4.1-py3-none-any.whl",
                         "urls": [],
                         "sha256": "4c690e5fbae2f21e87843e89c26191f0d9454f362d8acdbd695716493ec8b3a9",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\nload(\"@rules_python//python/private:glob_excludes.bzl\", \"glob_excludes\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude to avoid non-determinism.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ] + glob_excludes.version_dependent_exclusions()),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__pip_tools"
                    },
                    "output_tree_hash": "1660c2d9c52ae3331b7f607214e76fe4e36b0b904dcdbb1b5e4ac70fcf7df7c5"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__pyproject_hooks instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:18:25: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/third_party/py/python_init_repositories.bzl:23:20: in python_init_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_python/python/private/py_repositories.bzl:70:14: in py_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_python/python/private/pypi/deps.bzl:133:14: in pypi_deps\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\nRepository rule http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/http.bzl:387:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__pyproject_hooks",
               "generator_name": "pypi__pyproject_hooks",
               "generator_function": "python_init_repositories",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/ae/f3/431b9d5fe7d14af7a32340792ef43b8a714e7726f1d7b69cc4e8e7a3f1d7/pyproject_hooks-1.1.0-py3-none-any.whl",
               "sha256": "7ceeefe9aec63a1064c18d939bdc3adf2d8aa1988a510afec15151578b232aa2",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\nload(\"@rules_python//python/private:glob_excludes.bzl\", \"glob_excludes\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude to avoid non-determinism.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ] + glob_excludes.version_dependent_exclusions()),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/ae/f3/431b9d5fe7d14af7a32340792ef43b8a714e7726f1d7b69cc4e8e7a3f1d7/pyproject_hooks-1.1.0-py3-none-any.whl",
                         "urls": [],
                         "sha256": "7ceeefe9aec63a1064c18d939bdc3adf2d8aa1988a510afec15151578b232aa2",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\nload(\"@rules_python//python/private:glob_excludes.bzl\", \"glob_excludes\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude to avoid non-determinism.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ] + glob_excludes.version_dependent_exclusions()),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__pyproject_hooks"
                    },
                    "output_tree_hash": "4b433ef3dcec05f828b8ca4d100ad0dfd56f2da20f01d91c37b586898f794d92"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__setuptools instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:18:25: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/third_party/py/python_init_repositories.bzl:23:20: in python_init_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_python/python/private/py_repositories.bzl:70:14: in py_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_python/python/private/pypi/deps.bzl:133:14: in pypi_deps\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\nRepository rule http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/http.bzl:387:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__setuptools",
               "generator_name": "pypi__setuptools",
               "generator_function": "python_init_repositories",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/de/88/70c5767a0e43eb4451c2200f07d042a4bcd7639276003a9c54a68cfcc1f8/setuptools-70.0.0-py3-none-any.whl",
               "sha256": "54faa7f2e8d2d11bcd2c07bed282eef1046b5c080d1c32add737d7b5817b1ad4",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\nload(\"@rules_python//python/private:glob_excludes.bzl\", \"glob_excludes\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude to avoid non-determinism.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ] + glob_excludes.version_dependent_exclusions()),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/de/88/70c5767a0e43eb4451c2200f07d042a4bcd7639276003a9c54a68cfcc1f8/setuptools-70.0.0-py3-none-any.whl",
                         "urls": [],
                         "sha256": "54faa7f2e8d2d11bcd2c07bed282eef1046b5c080d1c32add737d7b5817b1ad4",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\nload(\"@rules_python//python/private:glob_excludes.bzl\", \"glob_excludes\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude to avoid non-determinism.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ] + glob_excludes.version_dependent_exclusions()),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__setuptools"
                    },
                    "output_tree_hash": "e9b4f72237d520588afd9990c92204b66d7d525d38a5a80a7ccbd1d3e552d346"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__tomli instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:18:25: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/third_party/py/python_init_repositories.bzl:23:20: in python_init_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_python/python/private/py_repositories.bzl:70:14: in py_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_python/python/private/pypi/deps.bzl:133:14: in pypi_deps\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\nRepository rule http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/http.bzl:387:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__tomli",
               "generator_name": "pypi__tomli",
               "generator_function": "python_init_repositories",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/97/75/10a9ebee3fd790d20926a90a2547f0bf78f371b2f13aa822c759680ca7b9/tomli-2.0.1-py3-none-any.whl",
               "sha256": "939de3e7a6161af0c887ef91b7d41a53e7c5a1ca976325f429cb46ea9bc30ecc",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\nload(\"@rules_python//python/private:glob_excludes.bzl\", \"glob_excludes\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude to avoid non-determinism.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ] + glob_excludes.version_dependent_exclusions()),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/97/75/10a9ebee3fd790d20926a90a2547f0bf78f371b2f13aa822c759680ca7b9/tomli-2.0.1-py3-none-any.whl",
                         "urls": [],
                         "sha256": "939de3e7a6161af0c887ef91b7d41a53e7c5a1ca976325f429cb46ea9bc30ecc",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\nload(\"@rules_python//python/private:glob_excludes.bzl\", \"glob_excludes\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude to avoid non-determinism.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ] + glob_excludes.version_dependent_exclusions()),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__tomli"
                    },
                    "output_tree_hash": "20e25b9ad6c3d0deea32d8135c4dda70426bd6345a81910008a560a7eac59753"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__wheel instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:18:25: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/third_party/py/python_init_repositories.bzl:23:20: in python_init_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_python/python/private/py_repositories.bzl:70:14: in py_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_python/python/private/pypi/deps.bzl:133:14: in pypi_deps\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\nRepository rule http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/http.bzl:387:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__wheel",
               "generator_name": "pypi__wheel",
               "generator_function": "python_init_repositories",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/7d/cd/d7460c9a869b16c3dd4e1e403cce337df165368c71d6af229a74699622ce/wheel-0.43.0-py3-none-any.whl",
               "sha256": "55c570405f142630c6b9f72fe09d9b67cf1477fcf543ae5b8dcb1f5b7377da81",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\nload(\"@rules_python//python/private:glob_excludes.bzl\", \"glob_excludes\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude to avoid non-determinism.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ] + glob_excludes.version_dependent_exclusions()),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/7d/cd/d7460c9a869b16c3dd4e1e403cce337df165368c71d6af229a74699622ce/wheel-0.43.0-py3-none-any.whl",
                         "urls": [],
                         "sha256": "55c570405f142630c6b9f72fe09d9b67cf1477fcf543ae5b8dcb1f5b7377da81",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\nload(\"@rules_python//python/private:glob_excludes.bzl\", \"glob_excludes\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude to avoid non-determinism.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ] + glob_excludes.version_dependent_exclusions()),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__wheel"
                    },
                    "output_tree_hash": "310881fd96921b2b6b729dd5132fe20ef2b01d267ffc22341eba36fe3b452a34"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__zipp instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:18:25: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/third_party/py/python_init_repositories.bzl:23:20: in python_init_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_python/python/private/py_repositories.bzl:70:14: in py_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_python/python/private/pypi/deps.bzl:133:14: in pypi_deps\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\nRepository rule http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/http.bzl:387:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__zipp",
               "generator_name": "pypi__zipp",
               "generator_function": "python_init_repositories",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/da/55/a03fd7240714916507e1fcf7ae355bd9d9ed2e6db492595f1a67f61681be/zipp-3.18.2-py3-none-any.whl",
               "sha256": "dce197b859eb796242b0622af1b8beb0a722d52aa2f57133ead08edd5bf5374e",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\nload(\"@rules_python//python/private:glob_excludes.bzl\", \"glob_excludes\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude to avoid non-determinism.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ] + glob_excludes.version_dependent_exclusions()),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/da/55/a03fd7240714916507e1fcf7ae355bd9d9ed2e6db492595f1a67f61681be/zipp-3.18.2-py3-none-any.whl",
                         "urls": [],
                         "sha256": "dce197b859eb796242b0622af1b8beb0a722d52aa2f57133ead08edd5bf5374e",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\nload(\"@rules_python//python/private:glob_excludes.bzl\", \"glob_excludes\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude to avoid non-determinism.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/*.pyc.*\",  # During pyc creation, temp files named *.pyc.NNN are created\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ] + glob_excludes.version_dependent_exclusions()),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__zipp"
                    },
                    "output_tree_hash": "c3dfbec840bcf00a82caf0fa43f0bf58d62952cda92afdf6ed51a60018706fba"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_python//python/private/pypi:whl_library.bzl%whl_library",
          "definition_information": "Repository pypi_lit instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:34:13: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/pypi/requirements.bzl:103:20: in install_deps\nRepository rule whl_library defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_python/python/private/pypi/whl_library.bzl:457:30: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi_lit",
               "generator_name": "pypi_lit",
               "generator_function": "install_deps",
               "generator_location": None,
               "group_deps": [],
               "repo": "pypi",
               "repo_prefix": "pypi_",
               "requirement": "lit==17.0.6     --hash=sha256:dfa9af9b55fc4509a56be7bf2346f079d7f4a242d583b9f2e0b078fd0abae31b",
               "download_only": False,
               "enable_implicit_namespace_pkgs": False,
               "environment": {},
               "envsubst": [],
               "extra_pip_args": [],
               "isolated": True,
               "pip_data_exclude": [],
               "python_interpreter": "python3",
               "python_interpreter_target": "@@python_x86_64-unknown-linux-gnu//:bin/python3",
               "quiet": True,
               "timeout": 600
          },
          "repositories": [
               {
                    "rule_class": "@@rules_python//python/private/pypi:whl_library.bzl%whl_library",
                    "attributes": {
                         "name": "pypi_lit",
                         "generator_name": "pypi_lit",
                         "generator_function": "install_deps",
                         "generator_location": None,
                         "group_deps": [],
                         "repo": "pypi",
                         "repo_prefix": "pypi_",
                         "requirement": "lit==17.0.6     --hash=sha256:dfa9af9b55fc4509a56be7bf2346f079d7f4a242d583b9f2e0b078fd0abae31b",
                         "download_only": False,
                         "enable_implicit_namespace_pkgs": False,
                         "environment": {},
                         "envsubst": [],
                         "extra_pip_args": [],
                         "isolated": True,
                         "pip_data_exclude": [],
                         "python_interpreter": "python3",
                         "python_interpreter_target": "@@python_x86_64-unknown-linux-gnu//:bin/python3",
                         "quiet": True,
                         "timeout": 600
                    },
                    "output_tree_hash": "e93c2f417d0fcfe5bf52e2c4855bb9166ccf40efd25bfdadc97617530be7087a"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_python//python/private/pypi:whl_library.bzl%whl_library",
          "definition_information": "Repository pypi_numpy instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:34:13: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/pypi/requirements.bzl:103:20: in install_deps\nRepository rule whl_library defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_python/python/private/pypi/whl_library.bzl:457:30: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi_numpy",
               "generator_name": "pypi_numpy",
               "generator_function": "install_deps",
               "generator_location": None,
               "annotation": "@@pypi//:numpy.annotation.json",
               "group_deps": [],
               "repo": "pypi",
               "repo_prefix": "pypi_",
               "requirement": "numpy==1.24.3     --hash=sha256:0ec87a7084caa559c36e0a2309e4ecb1baa03b687201d0a847c8b0ed476a7187     --hash=sha256:1a7d6acc2e7524c9955e5c903160aa4ea083736fde7e91276b0e5d98e6332812     --hash=sha256:202de8f38fc4a45a3eea4b63e2f376e5f2dc64ef0fa692838e31a808520efaf7     --hash=sha256:210461d87fb02a84ef243cac5e814aad2b7f4be953b32cb53327bb49fd77fbb4     --hash=sha256:2d926b52ba1367f9acb76b0df6ed21f0b16a1ad87c6720a1121674e5cf63e2b6     --hash=sha256:352ee00c7f8387b44d19f4cada524586f07379c0d49270f87233983bc5087ca0     --hash=sha256:35400e6a8d102fd07c71ed7dcadd9eb62ee9a6e84ec159bd48c28235bbb0f8e4     --hash=sha256:3c1104d3c036fb81ab923f507536daedc718d0ad5a8707c6061cdfd6d184e570     --hash=sha256:4719d5aefb5189f50887773699eaf94e7d1e02bf36c1a9d353d9f46703758ca4     --hash=sha256:4749e053a29364d3452c034827102ee100986903263e89884922ef01a0a6fd2f     --hash=sha256:5342cf6aad47943286afa6f1609cad9b4266a05e7f2ec408e2cf7aea7ff69d80     --hash=sha256:56e48aec79ae238f6e4395886b5eaed058abb7231fb3361ddd7bfdf4eed54289     --hash=sha256:76e3f4e85fc5d4fd311f6e9b794d0c00e7002ec122be271f2019d63376f1d385     --hash=sha256:7776ea65423ca6a15255ba1872d82d207bd1e09f6d0894ee4a64678dd2204078     --hash=sha256:784c6da1a07818491b0ffd63c6bbe5a33deaa0e25a20e1b3ea20cf0e43f8046c     --hash=sha256:8535303847b89aa6b0f00aa1dc62867b5a32923e4d1681a35b5eef2d9591a463     --hash=sha256:9a7721ec204d3a237225db3e194c25268faf92e19338a35f3a224469cb6039a3     --hash=sha256:a1d3c026f57ceaad42f8231305d4653d5f05dc6332a730ae5c0bea3513de0950     --hash=sha256:ab344f1bf21f140adab8e47fdbc7c35a477dc01408791f8ba00d018dd0bc5155     --hash=sha256:ab5f23af8c16022663a652d3b25dcdc272ac3f83c3af4c02eb8b824e6b3ab9d7     --hash=sha256:ae8d0be48d1b6ed82588934aaaa179875e7dc4f3d84da18d7eae6eb3f06c242c     --hash=sha256:c91c4afd8abc3908e00a44b2672718905b8611503f7ff87390cc0ac3423fb096     --hash=sha256:d5036197ecae68d7f491fcdb4df90082b0d4960ca6599ba2659957aafced7c17     --hash=sha256:d6cc757de514c00b24ae8cf5c876af2a7c3df189028d68c0cb4eaa9cd5afc2bf     --hash=sha256:d933fabd8f6a319e8530d0de4fcc2e6a61917e0b0c271fded460032db42a0fe4     --hash=sha256:ea8282b9bcfe2b5e7d491d0bf7f3e2da29700cec05b49e64d6246923329f2b02     --hash=sha256:ecde0f8adef7dfdec993fd54b0f78183051b6580f606111a6d789cd14c61ea0c     --hash=sha256:f21c442fdd2805e91799fbe044a7b999b8571bb0ab0f7850d0cb9641a687092b",
               "download_only": False,
               "enable_implicit_namespace_pkgs": False,
               "environment": {},
               "envsubst": [],
               "extra_pip_args": [],
               "isolated": True,
               "pip_data_exclude": [],
               "python_interpreter": "python3",
               "python_interpreter_target": "@@python_x86_64-unknown-linux-gnu//:bin/python3",
               "quiet": True,
               "timeout": 600
          },
          "repositories": [
               {
                    "rule_class": "@@rules_python//python/private/pypi:whl_library.bzl%whl_library",
                    "attributes": {
                         "name": "pypi_numpy",
                         "generator_name": "pypi_numpy",
                         "generator_function": "install_deps",
                         "generator_location": None,
                         "annotation": "@@pypi//:numpy.annotation.json",
                         "group_deps": [],
                         "repo": "pypi",
                         "repo_prefix": "pypi_",
                         "requirement": "numpy==1.24.3     --hash=sha256:0ec87a7084caa559c36e0a2309e4ecb1baa03b687201d0a847c8b0ed476a7187     --hash=sha256:1a7d6acc2e7524c9955e5c903160aa4ea083736fde7e91276b0e5d98e6332812     --hash=sha256:202de8f38fc4a45a3eea4b63e2f376e5f2dc64ef0fa692838e31a808520efaf7     --hash=sha256:210461d87fb02a84ef243cac5e814aad2b7f4be953b32cb53327bb49fd77fbb4     --hash=sha256:2d926b52ba1367f9acb76b0df6ed21f0b16a1ad87c6720a1121674e5cf63e2b6     --hash=sha256:352ee00c7f8387b44d19f4cada524586f07379c0d49270f87233983bc5087ca0     --hash=sha256:35400e6a8d102fd07c71ed7dcadd9eb62ee9a6e84ec159bd48c28235bbb0f8e4     --hash=sha256:3c1104d3c036fb81ab923f507536daedc718d0ad5a8707c6061cdfd6d184e570     --hash=sha256:4719d5aefb5189f50887773699eaf94e7d1e02bf36c1a9d353d9f46703758ca4     --hash=sha256:4749e053a29364d3452c034827102ee100986903263e89884922ef01a0a6fd2f     --hash=sha256:5342cf6aad47943286afa6f1609cad9b4266a05e7f2ec408e2cf7aea7ff69d80     --hash=sha256:56e48aec79ae238f6e4395886b5eaed058abb7231fb3361ddd7bfdf4eed54289     --hash=sha256:76e3f4e85fc5d4fd311f6e9b794d0c00e7002ec122be271f2019d63376f1d385     --hash=sha256:7776ea65423ca6a15255ba1872d82d207bd1e09f6d0894ee4a64678dd2204078     --hash=sha256:784c6da1a07818491b0ffd63c6bbe5a33deaa0e25a20e1b3ea20cf0e43f8046c     --hash=sha256:8535303847b89aa6b0f00aa1dc62867b5a32923e4d1681a35b5eef2d9591a463     --hash=sha256:9a7721ec204d3a237225db3e194c25268faf92e19338a35f3a224469cb6039a3     --hash=sha256:a1d3c026f57ceaad42f8231305d4653d5f05dc6332a730ae5c0bea3513de0950     --hash=sha256:ab344f1bf21f140adab8e47fdbc7c35a477dc01408791f8ba00d018dd0bc5155     --hash=sha256:ab5f23af8c16022663a652d3b25dcdc272ac3f83c3af4c02eb8b824e6b3ab9d7     --hash=sha256:ae8d0be48d1b6ed82588934aaaa179875e7dc4f3d84da18d7eae6eb3f06c242c     --hash=sha256:c91c4afd8abc3908e00a44b2672718905b8611503f7ff87390cc0ac3423fb096     --hash=sha256:d5036197ecae68d7f491fcdb4df90082b0d4960ca6599ba2659957aafced7c17     --hash=sha256:d6cc757de514c00b24ae8cf5c876af2a7c3df189028d68c0cb4eaa9cd5afc2bf     --hash=sha256:d933fabd8f6a319e8530d0de4fcc2e6a61917e0b0c271fded460032db42a0fe4     --hash=sha256:ea8282b9bcfe2b5e7d491d0bf7f3e2da29700cec05b49e64d6246923329f2b02     --hash=sha256:ecde0f8adef7dfdec993fd54b0f78183051b6580f606111a6d789cd14c61ea0c     --hash=sha256:f21c442fdd2805e91799fbe044a7b999b8571bb0ab0f7850d0cb9641a687092b",
                         "download_only": False,
                         "enable_implicit_namespace_pkgs": False,
                         "environment": {},
                         "envsubst": [],
                         "extra_pip_args": [],
                         "isolated": True,
                         "pip_data_exclude": [],
                         "python_interpreter": "python3",
                         "python_interpreter_target": "@@python_x86_64-unknown-linux-gnu//:bin/python3",
                         "quiet": True,
                         "timeout": 600
                    },
                    "output_tree_hash": "5e8e6360416b185d9588d9479e2b6e66ed9b53508ce366ae8e8860fa2d56f53c"
               }
          ]
     },
     {
          "original_rule_class": "@@io_bazel_rules_go//go/private:sdk.bzl%_go_download_sdk",
          "definition_information": "Repository go_sdk instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:54:15: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace0.bzl:53:19: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace0.bzl:130:20: in workspace\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/com_github_grpc_grpc/bazel/grpc_extra_deps.bzl:36:27: in grpc_extra_deps\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/io_bazel_rules_go/go/private/sdk.bzl:431:28: in go_register_toolchains\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/io_bazel_rules_go/go/private/sdk.bzl:130:21: in go_download_sdk\nRepository rule _go_download_sdk defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/io_bazel_rules_go/go/private/sdk.bzl:117:35: in <toplevel>\n",
          "original_attributes": {
               "name": "go_sdk",
               "generator_name": "go_sdk",
               "generator_function": "workspace",
               "generator_location": None,
               "version": "1.18.4"
          },
          "repositories": [
               {
                    "rule_class": "@@io_bazel_rules_go//go/private:sdk.bzl%_go_download_sdk",
                    "attributes": {
                         "name": "go_sdk",
                         "generator_name": "go_sdk",
                         "generator_function": "workspace",
                         "generator_location": None,
                         "version": "1.18.4"
                    },
                    "output_tree_hash": "ceb9275fc5e4f1e7ad489290e82aedbcb9fdb4287c3a827f5b4d3d86e66a6b5e"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_python//python/private:pythons_hub.bzl%hub_repo",
          "definition_information": "Repository pythons_hub instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:18:25: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/third_party/py/python_init_repositories.bzl:23:20: in python_init_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_python/python/private/py_repositories.bzl:37:10: in py_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\nRepository rule hub_repo defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/rules_python/python/private/pythons_hub.bzl:148:27: in <toplevel>\n",
          "original_attributes": {
               "name": "pythons_hub",
               "generator_name": "pythons_hub",
               "generator_function": "python_init_repositories",
               "generator_location": None,
               "default_python_version": "",
               "minor_mapping": {
                    "3.8": "3.8.20",
                    "3.9": "3.9.20",
                    "3.10": "3.10.15",
                    "3.11": "3.11.10",
                    "3.12": "3.12.7",
                    "3.13": "3.13.0"
               },
               "python_versions": [
                    "3.10.11",
                    "3.10.12",
                    "3.10.13",
                    "3.10.14",
                    "3.10.15",
                    "3.10.2",
                    "3.10.4",
                    "3.10.6",
                    "3.10.8",
                    "3.10.9",
                    "3.11.1",
                    "3.11.10",
                    "3.11.3",
                    "3.11.4",
                    "3.11.5",
                    "3.11.6",
                    "3.11.7",
                    "3.11.8",
                    "3.11.9",
                    "3.12.0",
                    "3.12.1",
                    "3.12.2",
                    "3.12.3",
                    "3.12.4",
                    "3.12.7",
                    "3.13.0",
                    "3.8.10",
                    "3.8.12",
                    "3.8.13",
                    "3.8.15",
                    "3.8.16",
                    "3.8.17",
                    "3.8.18",
                    "3.8.19",
                    "3.8.20",
                    "3.9.10",
                    "3.9.12",
                    "3.9.13",
                    "3.9.15",
                    "3.9.16",
                    "3.9.17",
                    "3.9.18",
                    "3.9.19",
                    "3.9.20"
               ],
               "toolchain_prefixes": [],
               "toolchain_python_versions": [],
               "toolchain_set_python_version_constraints": [],
               "toolchain_user_repository_names": []
          },
          "repositories": [
               {
                    "rule_class": "@@rules_python//python/private:pythons_hub.bzl%hub_repo",
                    "attributes": {
                         "name": "pythons_hub",
                         "generator_name": "pythons_hub",
                         "generator_function": "python_init_repositories",
                         "generator_location": None,
                         "default_python_version": "",
                         "minor_mapping": {
                              "3.8": "3.8.20",
                              "3.9": "3.9.20",
                              "3.10": "3.10.15",
                              "3.11": "3.11.10",
                              "3.12": "3.12.7",
                              "3.13": "3.13.0"
                         },
                         "python_versions": [
                              "3.10.11",
                              "3.10.12",
                              "3.10.13",
                              "3.10.14",
                              "3.10.15",
                              "3.10.2",
                              "3.10.4",
                              "3.10.6",
                              "3.10.8",
                              "3.10.9",
                              "3.11.1",
                              "3.11.10",
                              "3.11.3",
                              "3.11.4",
                              "3.11.5",
                              "3.11.6",
                              "3.11.7",
                              "3.11.8",
                              "3.11.9",
                              "3.12.0",
                              "3.12.1",
                              "3.12.2",
                              "3.12.3",
                              "3.12.4",
                              "3.12.7",
                              "3.13.0",
                              "3.8.10",
                              "3.8.12",
                              "3.8.13",
                              "3.8.15",
                              "3.8.16",
                              "3.8.17",
                              "3.8.18",
                              "3.8.19",
                              "3.8.20",
                              "3.9.10",
                              "3.9.12",
                              "3.9.13",
                              "3.9.15",
                              "3.9.16",
                              "3.9.17",
                              "3.9.18",
                              "3.9.19",
                              "3.9.20"
                         ],
                         "toolchain_prefixes": [],
                         "toolchain_python_versions": [],
                         "toolchain_set_python_version_constraints": [],
                         "toolchain_user_repository_names": []
                    },
                    "output_tree_hash": "8cfec3b4d6c24b45bbdd9b0fbb97fc029d00b92d44dbf175f2e5d37f6c1b6714"
               }
          ]
     },
     {
          "original_rule_class": "//third_party:repo.bzl%_tf_http_archive",
          "definition_information": "Repository mpitrampoline instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:46:15: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace2.bzl:171:28: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace2.bzl:27:18: in _initialize_third_party\n  /usr/local/google/home/kotlaja/bzl_mod/xla/third_party/mpitrampoline/workspace.bzl:11:20: in repo\n  /usr/local/google/home/kotlaja/bzl_mod/xla/third_party/repo.bzl:138:21: in tf_http_archive\nRepository rule _tf_http_archive defined at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/third_party/repo.bzl:89:35: in <toplevel>\n",
          "original_attributes": {
               "name": "mpitrampoline",
               "generator_name": "mpitrampoline",
               "generator_function": "workspace",
               "generator_location": None,
               "sha256": "5a36656205c472bdb639bffebb0f014523b32dda0c2cbedd9ce7abfc9e879e84",
               "urls": [
                    "https://storage.googleapis.com/mirror.tensorflow.org/github.com/eschnett/mpitrampoline/archive/25efb0f7a4cd00ed82bafb8b1a6285fc50d297ed.tar.gz",
                    "https://github.com/eschnett/mpitrampoline/archive/25efb0f7a4cd00ed82bafb8b1a6285fc50d297ed.tar.gz"
               ],
               "strip_prefix": "MPItrampoline-25efb0f7a4cd00ed82bafb8b1a6285fc50d297ed",
               "patch_file": [
                    "//third_party/mpitrampoline:gen.patch"
               ],
               "build_file": "//third_party/mpitrampoline:mpitrampoline.BUILD"
          },
          "repositories": [
               {
                    "rule_class": "//third_party:repo.bzl%_tf_http_archive",
                    "attributes": {
                         "name": "mpitrampoline",
                         "generator_name": "mpitrampoline",
                         "generator_function": "workspace",
                         "generator_location": None,
                         "sha256": "5a36656205c472bdb639bffebb0f014523b32dda0c2cbedd9ce7abfc9e879e84",
                         "urls": [
                              "https://storage.googleapis.com/mirror.tensorflow.org/github.com/eschnett/mpitrampoline/archive/25efb0f7a4cd00ed82bafb8b1a6285fc50d297ed.tar.gz",
                              "https://github.com/eschnett/mpitrampoline/archive/25efb0f7a4cd00ed82bafb8b1a6285fc50d297ed.tar.gz"
                         ],
                         "strip_prefix": "MPItrampoline-25efb0f7a4cd00ed82bafb8b1a6285fc50d297ed",
                         "patch_file": [
                              "//third_party/mpitrampoline:gen.patch"
                         ],
                         "build_file": "//third_party/mpitrampoline:mpitrampoline.BUILD"
                    },
                    "output_tree_hash": "8f69094f77e8ed1c1f4ddf664e7caf4a7c40914fe32760606a1fdc156a5e3347"
               }
          ]
     },
     {
          "original_rule_class": "//third_party:repo.bzl%_tf_http_archive",
          "definition_information": "Repository gloo instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:46:15: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace2.bzl:171:28: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace2.bzl:26:9: in _initialize_third_party\n  /usr/local/google/home/kotlaja/bzl_mod/xla/third_party/gloo/workspace.bzl:11:20: in repo\n  /usr/local/google/home/kotlaja/bzl_mod/xla/third_party/repo.bzl:138:21: in tf_http_archive\nRepository rule _tf_http_archive defined at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/third_party/repo.bzl:89:35: in <toplevel>\n",
          "original_attributes": {
               "name": "gloo",
               "generator_name": "gloo",
               "generator_function": "workspace",
               "generator_location": None,
               "sha256": "5759a06e6c8863c58e8ceadeb56f7c701fec89b2559ba33a103a447207bf69c7",
               "urls": [
                    "https://storage.googleapis.com/mirror.tensorflow.org/github.com/facebookincubator/gloo/archive/5354032ea08eadd7fc4456477f7f7c6308818509.tar.gz",
                    "https://github.com/facebookincubator/gloo/archive/5354032ea08eadd7fc4456477f7f7c6308818509.tar.gz"
               ],
               "strip_prefix": "gloo-5354032ea08eadd7fc4456477f7f7c6308818509",
               "build_file": "//third_party/gloo:gloo.BUILD"
          },
          "repositories": [
               {
                    "rule_class": "//third_party:repo.bzl%_tf_http_archive",
                    "attributes": {
                         "name": "gloo",
                         "generator_name": "gloo",
                         "generator_function": "workspace",
                         "generator_location": None,
                         "sha256": "5759a06e6c8863c58e8ceadeb56f7c701fec89b2559ba33a103a447207bf69c7",
                         "urls": [
                              "https://storage.googleapis.com/mirror.tensorflow.org/github.com/facebookincubator/gloo/archive/5354032ea08eadd7fc4456477f7f7c6308818509.tar.gz",
                              "https://github.com/facebookincubator/gloo/archive/5354032ea08eadd7fc4456477f7f7c6308818509.tar.gz"
                         ],
                         "strip_prefix": "gloo-5354032ea08eadd7fc4456477f7f7c6308818509",
                         "build_file": "//third_party/gloo:gloo.BUILD"
                    },
                    "output_tree_hash": "172ccf65b6a21ab8a06d3d8cfceb51c085eae870508ee26206395b4ee9a3bc32"
               }
          ]
     },
     {
          "original_rule_class": "//third_party:repo.bzl%_tf_http_archive",
          "definition_information": "Repository nanobind instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:46:15: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace2.bzl:171:28: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace2.bzl:28:13: in _initialize_third_party\n  /usr/local/google/home/kotlaja/bzl_mod/xla/third_party/nanobind/workspace.bzl:6:20: in repo\n  /usr/local/google/home/kotlaja/bzl_mod/xla/third_party/repo.bzl:138:21: in tf_http_archive\nRepository rule _tf_http_archive defined at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/third_party/repo.bzl:89:35: in <toplevel>\n",
          "original_attributes": {
               "name": "nanobind",
               "generator_name": "nanobind",
               "generator_function": "workspace",
               "generator_location": None,
               "sha256": "d1d8575f2bf76cc2ca357ac5521daa2f1bcf5397231d856f4ce66ba0670ac928",
               "urls": [
                    "https://storage.googleapis.com/mirror.tensorflow.org/github.com/wjakob/nanobind/archive/b4b933111fa61815f3f5b509fde80c24f029ac26.tar.gz",
                    "https://github.com/wjakob/nanobind/archive/b4b933111fa61815f3f5b509fde80c24f029ac26.tar.gz"
               ],
               "strip_prefix": "nanobind-b4b933111fa61815f3f5b509fde80c24f029ac26",
               "build_file": "//third_party/nanobind:nanobind.BUILD"
          },
          "repositories": [
               {
                    "rule_class": "//third_party:repo.bzl%_tf_http_archive",
                    "attributes": {
                         "name": "nanobind",
                         "generator_name": "nanobind",
                         "generator_function": "workspace",
                         "generator_location": None,
                         "sha256": "d1d8575f2bf76cc2ca357ac5521daa2f1bcf5397231d856f4ce66ba0670ac928",
                         "urls": [
                              "https://storage.googleapis.com/mirror.tensorflow.org/github.com/wjakob/nanobind/archive/b4b933111fa61815f3f5b509fde80c24f029ac26.tar.gz",
                              "https://github.com/wjakob/nanobind/archive/b4b933111fa61815f3f5b509fde80c24f029ac26.tar.gz"
                         ],
                         "strip_prefix": "nanobind-b4b933111fa61815f3f5b509fde80c24f029ac26",
                         "build_file": "//third_party/nanobind:nanobind.BUILD"
                    },
                    "output_tree_hash": "1d60cf584ae943705ca614a884f4d059058ac94eb914286f065c67d046a58e43"
               }
          ]
     },
     {
          "original_rule_class": "@@tsl//third_party/nccl/hermetic:nccl_configure.bzl%nccl_configure",
          "definition_information": "Repository local_config_nccl instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:101:15: in <toplevel>\nRepository rule nccl_configure defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/nccl/hermetic/nccl_configure.bzl:172:33: in <toplevel>\n",
          "original_attributes": {
               "name": "local_config_nccl"
          },
          "repositories": [
               {
                    "rule_class": "@@tsl//third_party/nccl/hermetic:nccl_configure.bzl%nccl_configure",
                    "attributes": {
                         "name": "local_config_nccl"
                    },
                    "output_tree_hash": "bfef7a5b71cde0b768c70bd1ca9739d13e780c0c46bc6aeef8470468b9aef9db"
               }
          ]
     },
     {
          "original_rule_class": "@@tsl//third_party:repo.bzl%_tf_http_archive",
          "definition_information": "Repository jsoncpp_git instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:46:15: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace2.bzl:164:19: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:604:21: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:364:20: in _tf_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/repo.bzl:136:21: in tf_http_archive\nRepository rule _tf_http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/repo.bzl:89:35: in <toplevel>\n",
          "original_attributes": {
               "name": "jsoncpp_git",
               "generator_name": "jsoncpp_git",
               "generator_function": "workspace",
               "generator_location": None,
               "sha256": "f409856e5920c18d0c2fb85276e24ee607d2a09b5e7d5f0a371368903c275da2",
               "urls": [
                    "https://storage.googleapis.com/mirror.tensorflow.org/github.com/open-source-parsers/jsoncpp/archive/1.9.5.tar.gz",
                    "https://github.com/open-source-parsers/jsoncpp/archive/1.9.5.tar.gz"
               ],
               "strip_prefix": "jsoncpp-1.9.5",
               "system_build_file": "@tsl//third_party/systemlibs:jsoncpp.BUILD"
          },
          "repositories": [
               {
                    "rule_class": "@@tsl//third_party:repo.bzl%_tf_http_archive",
                    "attributes": {
                         "name": "jsoncpp_git",
                         "generator_name": "jsoncpp_git",
                         "generator_function": "workspace",
                         "generator_location": None,
                         "sha256": "f409856e5920c18d0c2fb85276e24ee607d2a09b5e7d5f0a371368903c275da2",
                         "urls": [
                              "https://storage.googleapis.com/mirror.tensorflow.org/github.com/open-source-parsers/jsoncpp/archive/1.9.5.tar.gz",
                              "https://github.com/open-source-parsers/jsoncpp/archive/1.9.5.tar.gz"
                         ],
                         "strip_prefix": "jsoncpp-1.9.5",
                         "system_build_file": "@tsl//third_party/systemlibs:jsoncpp.BUILD"
                    },
                    "output_tree_hash": "08dc618a3ed33857c15a7273c350cf929ade5bee814964744ca8bf021df84013"
               }
          ]
     },
     {
          "original_rule_class": "@@tsl//third_party/gpus/cuda/hermetic:cuda_redist_init_repositories.bzl%cuda_repo",
          "definition_information": "Repository cuda_nvjitlink instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:74:30: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/gpus/cuda/hermetic/cuda_redist_init_repositories.bzl:573:18: in cuda_redist_init_repositories\nRepository rule cuda_repo defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/gpus/cuda/hermetic/cuda_redist_init_repositories.bzl:383:28: in <toplevel>\n",
          "original_attributes": {
               "name": "cuda_nvjitlink",
               "generator_name": "cuda_nvjitlink",
               "generator_function": "cuda_redist_init_repositories",
               "generator_location": None,
               "url_dict": {},
               "versions": [
                    "12"
               ],
               "build_templates": [
                    "@@tsl//third_party/gpus/cuda/hermetic:cuda_nvjitlink.BUILD.tpl"
               ],
               "cuda_redist_path_prefix": "https://developer.download.nvidia.com/compute/cuda/redist/"
          },
          "repositories": [
               {
                    "rule_class": "@@tsl//third_party/gpus/cuda/hermetic:cuda_redist_init_repositories.bzl%cuda_repo",
                    "attributes": {
                         "name": "cuda_nvjitlink",
                         "generator_name": "cuda_nvjitlink",
                         "generator_function": "cuda_redist_init_repositories",
                         "generator_location": None,
                         "url_dict": {},
                         "versions": [
                              "12"
                         ],
                         "build_templates": [
                              "@@tsl//third_party/gpus/cuda/hermetic:cuda_nvjitlink.BUILD.tpl"
                         ],
                         "cuda_redist_path_prefix": "https://developer.download.nvidia.com/compute/cuda/redist/"
                    },
                    "output_tree_hash": "bea324103456f35b7cf85adee6be1ebd5e95097f238536b4e8fce35c03c43adc"
               }
          ]
     },
     {
          "original_rule_class": "@@tsl//third_party/gpus/cuda/hermetic:cuda_redist_init_repositories.bzl%cuda_repo",
          "definition_information": "Repository cuda_cccl instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:74:30: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/gpus/cuda/hermetic/cuda_redist_init_repositories.bzl:573:18: in cuda_redist_init_repositories\nRepository rule cuda_repo defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/gpus/cuda/hermetic/cuda_redist_init_repositories.bzl:383:28: in <toplevel>\n",
          "original_attributes": {
               "name": "cuda_cccl",
               "generator_name": "cuda_cccl",
               "generator_function": "cuda_redist_init_repositories",
               "generator_location": None,
               "url_dict": {},
               "versions": [
                    "12,11"
               ],
               "build_templates": [
                    "@@tsl//third_party/gpus/cuda/hermetic:cuda_cccl.BUILD.tpl"
               ],
               "cuda_redist_path_prefix": "https://developer.download.nvidia.com/compute/cuda/redist/"
          },
          "repositories": [
               {
                    "rule_class": "@@tsl//third_party/gpus/cuda/hermetic:cuda_redist_init_repositories.bzl%cuda_repo",
                    "attributes": {
                         "name": "cuda_cccl",
                         "generator_name": "cuda_cccl",
                         "generator_function": "cuda_redist_init_repositories",
                         "generator_location": None,
                         "url_dict": {},
                         "versions": [
                              "12,11"
                         ],
                         "build_templates": [
                              "@@tsl//third_party/gpus/cuda/hermetic:cuda_cccl.BUILD.tpl"
                         ],
                         "cuda_redist_path_prefix": "https://developer.download.nvidia.com/compute/cuda/redist/"
                    },
                    "output_tree_hash": "480a1f7c89a2493314534557d45d151945974153b2f45862eb98ce1793eb170c"
               }
          ]
     },
     {
          "original_rule_class": "@@tsl//third_party/gpus/cuda/hermetic:cuda_redist_init_repositories.bzl%cuda_repo",
          "definition_information": "Repository cuda_curand instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:74:30: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/gpus/cuda/hermetic/cuda_redist_init_repositories.bzl:573:18: in cuda_redist_init_repositories\nRepository rule cuda_repo defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/gpus/cuda/hermetic/cuda_redist_init_repositories.bzl:383:28: in <toplevel>\n",
          "original_attributes": {
               "name": "cuda_curand",
               "generator_name": "cuda_curand",
               "generator_function": "cuda_redist_init_repositories",
               "generator_location": None,
               "url_dict": {},
               "versions": [
                    "10"
               ],
               "build_templates": [
                    "@@tsl//third_party/gpus/cuda/hermetic:cuda_curand.BUILD.tpl"
               ],
               "cuda_redist_path_prefix": "https://developer.download.nvidia.com/compute/cuda/redist/"
          },
          "repositories": [
               {
                    "rule_class": "@@tsl//third_party/gpus/cuda/hermetic:cuda_redist_init_repositories.bzl%cuda_repo",
                    "attributes": {
                         "name": "cuda_curand",
                         "generator_name": "cuda_curand",
                         "generator_function": "cuda_redist_init_repositories",
                         "generator_location": None,
                         "url_dict": {},
                         "versions": [
                              "10"
                         ],
                         "build_templates": [
                              "@@tsl//third_party/gpus/cuda/hermetic:cuda_curand.BUILD.tpl"
                         ],
                         "cuda_redist_path_prefix": "https://developer.download.nvidia.com/compute/cuda/redist/"
                    },
                    "output_tree_hash": "6a7ab3a45e4d149039f2d47bfc822e128fe01a12133681dc420e9f88f44a4ee5"
               }
          ]
     },
     {
          "original_rule_class": "@@tsl//third_party/gpus/cuda/hermetic:cuda_redist_init_repositories.bzl%cuda_repo",
          "definition_information": "Repository cuda_nvml instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:74:30: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/gpus/cuda/hermetic/cuda_redist_init_repositories.bzl:573:18: in cuda_redist_init_repositories\nRepository rule cuda_repo defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/gpus/cuda/hermetic/cuda_redist_init_repositories.bzl:383:28: in <toplevel>\n",
          "original_attributes": {
               "name": "cuda_nvml",
               "generator_name": "cuda_nvml",
               "generator_function": "cuda_redist_init_repositories",
               "generator_location": None,
               "url_dict": {},
               "versions": [
                    "12,11"
               ],
               "build_templates": [
                    "@@tsl//third_party/gpus/cuda/hermetic:cuda_nvml.BUILD.tpl"
               ],
               "cuda_redist_path_prefix": "https://developer.download.nvidia.com/compute/cuda/redist/"
          },
          "repositories": [
               {
                    "rule_class": "@@tsl//third_party/gpus/cuda/hermetic:cuda_redist_init_repositories.bzl%cuda_repo",
                    "attributes": {
                         "name": "cuda_nvml",
                         "generator_name": "cuda_nvml",
                         "generator_function": "cuda_redist_init_repositories",
                         "generator_location": None,
                         "url_dict": {},
                         "versions": [
                              "12,11"
                         ],
                         "build_templates": [
                              "@@tsl//third_party/gpus/cuda/hermetic:cuda_nvml.BUILD.tpl"
                         ],
                         "cuda_redist_path_prefix": "https://developer.download.nvidia.com/compute/cuda/redist/"
                    },
                    "output_tree_hash": "0daa3d91319c4abe60ff8cca64c104b33ef70536b8f67efe5da641daa12e385c"
               }
          ]
     },
     {
          "original_rule_class": "@@tsl//third_party/gpus/cuda/hermetic:cuda_redist_init_repositories.bzl%cuda_repo",
          "definition_information": "Repository cuda_cusparse instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:74:30: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/gpus/cuda/hermetic/cuda_redist_init_repositories.bzl:573:18: in cuda_redist_init_repositories\nRepository rule cuda_repo defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/gpus/cuda/hermetic/cuda_redist_init_repositories.bzl:383:28: in <toplevel>\n",
          "original_attributes": {
               "name": "cuda_cusparse",
               "generator_name": "cuda_cusparse",
               "generator_function": "cuda_redist_init_repositories",
               "generator_location": None,
               "url_dict": {},
               "versions": [
                    "12,11"
               ],
               "build_templates": [
                    "@@tsl//third_party/gpus/cuda/hermetic:cuda_cusparse.BUILD.tpl"
               ],
               "cuda_redist_path_prefix": "https://developer.download.nvidia.com/compute/cuda/redist/"
          },
          "repositories": [
               {
                    "rule_class": "@@tsl//third_party/gpus/cuda/hermetic:cuda_redist_init_repositories.bzl%cuda_repo",
                    "attributes": {
                         "name": "cuda_cusparse",
                         "generator_name": "cuda_cusparse",
                         "generator_function": "cuda_redist_init_repositories",
                         "generator_location": None,
                         "url_dict": {},
                         "versions": [
                              "12,11"
                         ],
                         "build_templates": [
                              "@@tsl//third_party/gpus/cuda/hermetic:cuda_cusparse.BUILD.tpl"
                         ],
                         "cuda_redist_path_prefix": "https://developer.download.nvidia.com/compute/cuda/redist/"
                    },
                    "output_tree_hash": "1d4edf9a399eb551c99a9fbfda4e87754c2a73ff8c0e9fdba2f40379b8f4a6fa"
               }
          ]
     },
     {
          "original_rule_class": "@@tsl//third_party/gpus/cuda/hermetic:cuda_redist_init_repositories.bzl%cuda_repo",
          "definition_information": "Repository cuda_cudart instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:74:30: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/gpus/cuda/hermetic/cuda_redist_init_repositories.bzl:573:18: in cuda_redist_init_repositories\nRepository rule cuda_repo defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/gpus/cuda/hermetic/cuda_redist_init_repositories.bzl:383:28: in <toplevel>\n",
          "original_attributes": {
               "name": "cuda_cudart",
               "generator_name": "cuda_cudart",
               "generator_function": "cuda_redist_init_repositories",
               "generator_location": None,
               "url_dict": {},
               "versions": [
                    "12,11"
               ],
               "build_templates": [
                    "@@tsl//third_party/gpus/cuda/hermetic:cuda_cudart.BUILD.tpl"
               ],
               "cuda_redist_path_prefix": "https://developer.download.nvidia.com/compute/cuda/redist/"
          },
          "repositories": [
               {
                    "rule_class": "@@tsl//third_party/gpus/cuda/hermetic:cuda_redist_init_repositories.bzl%cuda_repo",
                    "attributes": {
                         "name": "cuda_cudart",
                         "generator_name": "cuda_cudart",
                         "generator_function": "cuda_redist_init_repositories",
                         "generator_location": None,
                         "url_dict": {},
                         "versions": [
                              "12,11"
                         ],
                         "build_templates": [
                              "@@tsl//third_party/gpus/cuda/hermetic:cuda_cudart.BUILD.tpl"
                         ],
                         "cuda_redist_path_prefix": "https://developer.download.nvidia.com/compute/cuda/redist/"
                    },
                    "output_tree_hash": "35c8e2899079e453b7fd13b3834f66b4f4ade04a004959fd294eaa5fa7bb3c94"
               }
          ]
     },
     {
          "original_rule_class": "@@tsl//third_party/gpus/cuda/hermetic:cuda_redist_init_repositories.bzl%cuda_repo",
          "definition_information": "Repository cuda_nvtx instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:74:30: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/gpus/cuda/hermetic/cuda_redist_init_repositories.bzl:573:18: in cuda_redist_init_repositories\nRepository rule cuda_repo defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/gpus/cuda/hermetic/cuda_redist_init_repositories.bzl:383:28: in <toplevel>\n",
          "original_attributes": {
               "name": "cuda_nvtx",
               "generator_name": "cuda_nvtx",
               "generator_function": "cuda_redist_init_repositories",
               "generator_location": None,
               "url_dict": {},
               "versions": [
                    "12,11"
               ],
               "build_templates": [
                    "@@tsl//third_party/gpus/cuda/hermetic:cuda_nvtx.BUILD.tpl"
               ],
               "cuda_redist_path_prefix": "https://developer.download.nvidia.com/compute/cuda/redist/"
          },
          "repositories": [
               {
                    "rule_class": "@@tsl//third_party/gpus/cuda/hermetic:cuda_redist_init_repositories.bzl%cuda_repo",
                    "attributes": {
                         "name": "cuda_nvtx",
                         "generator_name": "cuda_nvtx",
                         "generator_function": "cuda_redist_init_repositories",
                         "generator_location": None,
                         "url_dict": {},
                         "versions": [
                              "12,11"
                         ],
                         "build_templates": [
                              "@@tsl//third_party/gpus/cuda/hermetic:cuda_nvtx.BUILD.tpl"
                         ],
                         "cuda_redist_path_prefix": "https://developer.download.nvidia.com/compute/cuda/redist/"
                    },
                    "output_tree_hash": "15b0dc1b88070a98839c4c1182fb130b3134f3789f2b2cd90f1e0ac40b6359e5"
               }
          ]
     },
     {
          "original_rule_class": "@@tsl//third_party/gpus/cuda/hermetic:cuda_redist_init_repositories.bzl%cuda_repo",
          "definition_information": "Repository cuda_cupti instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:74:30: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/gpus/cuda/hermetic/cuda_redist_init_repositories.bzl:573:18: in cuda_redist_init_repositories\nRepository rule cuda_repo defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/gpus/cuda/hermetic/cuda_redist_init_repositories.bzl:383:28: in <toplevel>\n",
          "original_attributes": {
               "name": "cuda_cupti",
               "generator_name": "cuda_cupti",
               "generator_function": "cuda_redist_init_repositories",
               "generator_location": None,
               "url_dict": {},
               "versions": [
                    "12,11"
               ],
               "build_templates": [
                    "@@tsl//third_party/gpus/cuda/hermetic:cuda_cupti.BUILD.tpl"
               ],
               "cuda_redist_path_prefix": "https://developer.download.nvidia.com/compute/cuda/redist/"
          },
          "repositories": [
               {
                    "rule_class": "@@tsl//third_party/gpus/cuda/hermetic:cuda_redist_init_repositories.bzl%cuda_repo",
                    "attributes": {
                         "name": "cuda_cupti",
                         "generator_name": "cuda_cupti",
                         "generator_function": "cuda_redist_init_repositories",
                         "generator_location": None,
                         "url_dict": {},
                         "versions": [
                              "12,11"
                         ],
                         "build_templates": [
                              "@@tsl//third_party/gpus/cuda/hermetic:cuda_cupti.BUILD.tpl"
                         ],
                         "cuda_redist_path_prefix": "https://developer.download.nvidia.com/compute/cuda/redist/"
                    },
                    "output_tree_hash": "7c543680c94fb54cb66ac9c90cb75bdb6e133984955fa5f96306567b10d3b0ac"
               }
          ]
     },
     {
          "original_rule_class": "@@tsl//third_party/gpus/cuda/hermetic:cuda_redist_init_repositories.bzl%cuda_repo",
          "definition_information": "Repository cuda_cublas instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:74:30: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/gpus/cuda/hermetic/cuda_redist_init_repositories.bzl:573:18: in cuda_redist_init_repositories\nRepository rule cuda_repo defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/gpus/cuda/hermetic/cuda_redist_init_repositories.bzl:383:28: in <toplevel>\n",
          "original_attributes": {
               "name": "cuda_cublas",
               "generator_name": "cuda_cublas",
               "generator_function": "cuda_redist_init_repositories",
               "generator_location": None,
               "url_dict": {},
               "versions": [
                    "12,11"
               ],
               "build_templates": [
                    "@@tsl//third_party/gpus/cuda/hermetic:cuda_cublas.BUILD.tpl"
               ],
               "cuda_redist_path_prefix": "https://developer.download.nvidia.com/compute/cuda/redist/"
          },
          "repositories": [
               {
                    "rule_class": "@@tsl//third_party/gpus/cuda/hermetic:cuda_redist_init_repositories.bzl%cuda_repo",
                    "attributes": {
                         "name": "cuda_cublas",
                         "generator_name": "cuda_cublas",
                         "generator_function": "cuda_redist_init_repositories",
                         "generator_location": None,
                         "url_dict": {},
                         "versions": [
                              "12,11"
                         ],
                         "build_templates": [
                              "@@tsl//third_party/gpus/cuda/hermetic:cuda_cublas.BUILD.tpl"
                         ],
                         "cuda_redist_path_prefix": "https://developer.download.nvidia.com/compute/cuda/redist/"
                    },
                    "output_tree_hash": "b133d5544a033b490f763722390088bea555c0c82538e6e1714978e651ffea7e"
               }
          ]
     },
     {
          "original_rule_class": "@@tsl//third_party/gpus/cuda/hermetic:cuda_redist_init_repositories.bzl%cuda_repo",
          "definition_information": "Repository cuda_cusolver instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:74:30: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/gpus/cuda/hermetic/cuda_redist_init_repositories.bzl:573:18: in cuda_redist_init_repositories\nRepository rule cuda_repo defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/gpus/cuda/hermetic/cuda_redist_init_repositories.bzl:383:28: in <toplevel>\n",
          "original_attributes": {
               "name": "cuda_cusolver",
               "generator_name": "cuda_cusolver",
               "generator_function": "cuda_redist_init_repositories",
               "generator_location": None,
               "url_dict": {},
               "versions": [
                    "11"
               ],
               "build_templates": [
                    "@@tsl//third_party/gpus/cuda/hermetic:cuda_cusolver.BUILD.tpl"
               ],
               "cuda_redist_path_prefix": "https://developer.download.nvidia.com/compute/cuda/redist/"
          },
          "repositories": [
               {
                    "rule_class": "@@tsl//third_party/gpus/cuda/hermetic:cuda_redist_init_repositories.bzl%cuda_repo",
                    "attributes": {
                         "name": "cuda_cusolver",
                         "generator_name": "cuda_cusolver",
                         "generator_function": "cuda_redist_init_repositories",
                         "generator_location": None,
                         "url_dict": {},
                         "versions": [
                              "11"
                         ],
                         "build_templates": [
                              "@@tsl//third_party/gpus/cuda/hermetic:cuda_cusolver.BUILD.tpl"
                         ],
                         "cuda_redist_path_prefix": "https://developer.download.nvidia.com/compute/cuda/redist/"
                    },
                    "output_tree_hash": "f7c6ef48c8786f3da7a0c6d3973d6b73040397c72e30b9d05113d77d63b598cc"
               }
          ]
     },
     {
          "original_rule_class": "@@tsl//third_party/gpus/cuda/hermetic:cuda_redist_init_repositories.bzl%cuda_repo",
          "definition_information": "Repository cuda_nvcc instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:74:30: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/gpus/cuda/hermetic/cuda_redist_init_repositories.bzl:573:18: in cuda_redist_init_repositories\nRepository rule cuda_repo defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/gpus/cuda/hermetic/cuda_redist_init_repositories.bzl:383:28: in <toplevel>\n",
          "original_attributes": {
               "name": "cuda_nvcc",
               "generator_name": "cuda_nvcc",
               "generator_function": "cuda_redist_init_repositories",
               "generator_location": None,
               "url_dict": {},
               "versions": [
                    "12,11"
               ],
               "build_templates": [
                    "@@tsl//third_party/gpus/cuda/hermetic:cuda_nvcc.BUILD.tpl"
               ],
               "cuda_redist_path_prefix": "https://developer.download.nvidia.com/compute/cuda/redist/"
          },
          "repositories": [
               {
                    "rule_class": "@@tsl//third_party/gpus/cuda/hermetic:cuda_redist_init_repositories.bzl%cuda_repo",
                    "attributes": {
                         "name": "cuda_nvcc",
                         "generator_name": "cuda_nvcc",
                         "generator_function": "cuda_redist_init_repositories",
                         "generator_location": None,
                         "url_dict": {},
                         "versions": [
                              "12,11"
                         ],
                         "build_templates": [
                              "@@tsl//third_party/gpus/cuda/hermetic:cuda_nvcc.BUILD.tpl"
                         ],
                         "cuda_redist_path_prefix": "https://developer.download.nvidia.com/compute/cuda/redist/"
                    },
                    "output_tree_hash": "d93d56473ad6c76116e7994b27c74413a658d0a35aa9ec7d63e322d9bab68403"
               }
          ]
     },
     {
          "original_rule_class": "@@tsl//third_party/gpus/cuda/hermetic:cuda_redist_init_repositories.bzl%cuda_repo",
          "definition_information": "Repository cuda_cufft instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:74:30: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/gpus/cuda/hermetic/cuda_redist_init_repositories.bzl:573:18: in cuda_redist_init_repositories\nRepository rule cuda_repo defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/gpus/cuda/hermetic/cuda_redist_init_repositories.bzl:383:28: in <toplevel>\n",
          "original_attributes": {
               "name": "cuda_cufft",
               "generator_name": "cuda_cufft",
               "generator_function": "cuda_redist_init_repositories",
               "generator_location": None,
               "url_dict": {},
               "versions": [
                    "11,10"
               ],
               "build_templates": [
                    "@@tsl//third_party/gpus/cuda/hermetic:cuda_cufft.BUILD.tpl"
               ],
               "cuda_redist_path_prefix": "https://developer.download.nvidia.com/compute/cuda/redist/"
          },
          "repositories": [
               {
                    "rule_class": "@@tsl//third_party/gpus/cuda/hermetic:cuda_redist_init_repositories.bzl%cuda_repo",
                    "attributes": {
                         "name": "cuda_cufft",
                         "generator_name": "cuda_cufft",
                         "generator_function": "cuda_redist_init_repositories",
                         "generator_location": None,
                         "url_dict": {},
                         "versions": [
                              "11,10"
                         ],
                         "build_templates": [
                              "@@tsl//third_party/gpus/cuda/hermetic:cuda_cufft.BUILD.tpl"
                         ],
                         "cuda_redist_path_prefix": "https://developer.download.nvidia.com/compute/cuda/redist/"
                    },
                    "output_tree_hash": "40ad08ef8e1dbba131e3200b1433de81ccc390d5dca72a52cc9391e0c0ccd915"
               }
          ]
     },
     {
          "original_rule_class": "@@tsl//third_party:repo.bzl%_tf_http_archive",
          "definition_information": "Repository com_googlesource_code_re2 instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:46:15: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace2.bzl:164:19: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:604:21: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:225:20: in _tf_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/repo.bzl:136:21: in tf_http_archive\nRepository rule _tf_http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/repo.bzl:89:35: in <toplevel>\n",
          "original_attributes": {
               "name": "com_googlesource_code_re2",
               "generator_name": "com_googlesource_code_re2",
               "generator_function": "workspace",
               "generator_location": None,
               "sha256": "ef516fb84824a597c4d5d0d6d330daedb18363b5a99eda87d027e6bdd9cba299",
               "urls": [
                    "https://storage.googleapis.com/mirror.tensorflow.org/github.com/google/re2/archive/03da4fc0857c285e3a26782f6bc8931c4c950df4.tar.gz",
                    "https://github.com/google/re2/archive/03da4fc0857c285e3a26782f6bc8931c4c950df4.tar.gz"
               ],
               "strip_prefix": "re2-03da4fc0857c285e3a26782f6bc8931c4c950df4",
               "system_build_file": "@tsl//third_party/systemlibs:re2.BUILD"
          },
          "repositories": [
               {
                    "rule_class": "@@tsl//third_party:repo.bzl%_tf_http_archive",
                    "attributes": {
                         "name": "com_googlesource_code_re2",
                         "generator_name": "com_googlesource_code_re2",
                         "generator_function": "workspace",
                         "generator_location": None,
                         "sha256": "ef516fb84824a597c4d5d0d6d330daedb18363b5a99eda87d027e6bdd9cba299",
                         "urls": [
                              "https://storage.googleapis.com/mirror.tensorflow.org/github.com/google/re2/archive/03da4fc0857c285e3a26782f6bc8931c4c950df4.tar.gz",
                              "https://github.com/google/re2/archive/03da4fc0857c285e3a26782f6bc8931c4c950df4.tar.gz"
                         ],
                         "strip_prefix": "re2-03da4fc0857c285e3a26782f6bc8931c4c950df4",
                         "system_build_file": "@tsl//third_party/systemlibs:re2.BUILD"
                    },
                    "output_tree_hash": "2a3b30fa94c80d5c8af18128134c080a747db7727f8db9a733872633eceb1fd4"
               }
          ]
     },
     {
          "original_rule_class": "@@tsl//third_party:repo.bzl%_tf_http_archive",
          "definition_information": "Repository com_google_googletest instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:46:15: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace2.bzl:164:19: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:604:21: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:300:20: in _tf_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/repo.bzl:136:21: in tf_http_archive\nRepository rule _tf_http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/repo.bzl:89:35: in <toplevel>\n",
          "original_attributes": {
               "name": "com_google_googletest",
               "generator_name": "com_google_googletest",
               "generator_function": "workspace",
               "generator_location": None,
               "sha256": "81964fe578e9bd7c94dfdb09c8e4d6e6759e19967e397dbea48d1c10e45d0df2",
               "urls": [
                    "https://storage.googleapis.com/mirror.tensorflow.org/github.com/google/googletest/archive/refs/tags/release-1.12.1.tar.gz",
                    "https://github.com/google/googletest/archive/refs/tags/release-1.12.1.tar.gz"
               ],
               "strip_prefix": "googletest-release-1.12.1"
          },
          "repositories": [
               {
                    "rule_class": "@@tsl//third_party:repo.bzl%_tf_http_archive",
                    "attributes": {
                         "name": "com_google_googletest",
                         "generator_name": "com_google_googletest",
                         "generator_function": "workspace",
                         "generator_location": None,
                         "sha256": "81964fe578e9bd7c94dfdb09c8e4d6e6759e19967e397dbea48d1c10e45d0df2",
                         "urls": [
                              "https://storage.googleapis.com/mirror.tensorflow.org/github.com/google/googletest/archive/refs/tags/release-1.12.1.tar.gz",
                              "https://github.com/google/googletest/archive/refs/tags/release-1.12.1.tar.gz"
                         ],
                         "strip_prefix": "googletest-release-1.12.1"
                    },
                    "output_tree_hash": "37c62ec4cbc5c3ad7079afac88145247e7f4a920aa4769e312833762143a1146"
               }
          ]
     },
     {
          "original_rule_class": "//third_party:repo.bzl%_tf_http_archive",
          "definition_information": "Repository dlpack instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:46:15: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace2.bzl:171:28: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace2.bzl:25:11: in _initialize_third_party\n  /usr/local/google/home/kotlaja/bzl_mod/xla/third_party/dlpack/workspace.bzl:6:20: in repo\n  /usr/local/google/home/kotlaja/bzl_mod/xla/third_party/repo.bzl:138:21: in tf_http_archive\nRepository rule _tf_http_archive defined at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/third_party/repo.bzl:89:35: in <toplevel>\n",
          "original_attributes": {
               "name": "dlpack",
               "generator_name": "dlpack",
               "generator_function": "workspace",
               "generator_location": None,
               "sha256": "044d2f5738e677c5f0f1ff9fb616a0245af67d09e42ae3514c73ba50cea0e4a5",
               "urls": [
                    "https://storage.googleapis.com/mirror.tensorflow.org/github.com/dmlc/dlpack/archive/2a7e9f1256ddc48186c86dff7a00e189b47e5310.tar.gz",
                    "https://github.com/dmlc/dlpack/archive/2a7e9f1256ddc48186c86dff7a00e189b47e5310.tar.gz"
               ],
               "strip_prefix": "dlpack-2a7e9f1256ddc48186c86dff7a00e189b47e5310",
               "build_file": "//third_party/dlpack:dlpack.BUILD"
          },
          "repositories": [
               {
                    "rule_class": "//third_party:repo.bzl%_tf_http_archive",
                    "attributes": {
                         "name": "dlpack",
                         "generator_name": "dlpack",
                         "generator_function": "workspace",
                         "generator_location": None,
                         "sha256": "044d2f5738e677c5f0f1ff9fb616a0245af67d09e42ae3514c73ba50cea0e4a5",
                         "urls": [
                              "https://storage.googleapis.com/mirror.tensorflow.org/github.com/dmlc/dlpack/archive/2a7e9f1256ddc48186c86dff7a00e189b47e5310.tar.gz",
                              "https://github.com/dmlc/dlpack/archive/2a7e9f1256ddc48186c86dff7a00e189b47e5310.tar.gz"
                         ],
                         "strip_prefix": "dlpack-2a7e9f1256ddc48186c86dff7a00e189b47e5310",
                         "build_file": "//third_party/dlpack:dlpack.BUILD"
                    },
                    "output_tree_hash": "6541625cd69fa9a63ca6aaa0d5d06f4ccc039e29578536937a9aae0b05e45686"
               }
          ]
     },
     {
          "original_rule_class": "@@tsl//third_party:repo.bzl%_tf_http_archive",
          "definition_information": "Repository pthreadpool instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:46:15: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace2.bzl:164:19: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:604:21: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:127:20: in _tf_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/repo.bzl:136:21: in tf_http_archive\nRepository rule _tf_http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/repo.bzl:89:35: in <toplevel>\n",
          "original_attributes": {
               "name": "pthreadpool",
               "generator_name": "pthreadpool",
               "generator_function": "workspace",
               "generator_location": None,
               "sha256": "cb668c32d6e05099492cc7ea19168e2dad0d1dcc4cbaa0e34fd4b38d39f0e03e",
               "urls": [
                    "https://storage.googleapis.com/mirror.tensorflow.org/github.com/Maratyszcza/pthreadpool/archive/f94ab76fe99754960035d520dce28e15b647e8cf.zip",
                    "https://github.com/Maratyszcza/pthreadpool/archive/f94ab76fe99754960035d520dce28e15b647e8cf.zip"
               ],
               "strip_prefix": "pthreadpool-f94ab76fe99754960035d520dce28e15b647e8cf"
          },
          "repositories": [
               {
                    "rule_class": "@@tsl//third_party:repo.bzl%_tf_http_archive",
                    "attributes": {
                         "name": "pthreadpool",
                         "generator_name": "pthreadpool",
                         "generator_function": "workspace",
                         "generator_location": None,
                         "sha256": "cb668c32d6e05099492cc7ea19168e2dad0d1dcc4cbaa0e34fd4b38d39f0e03e",
                         "urls": [
                              "https://storage.googleapis.com/mirror.tensorflow.org/github.com/Maratyszcza/pthreadpool/archive/f94ab76fe99754960035d520dce28e15b647e8cf.zip",
                              "https://github.com/Maratyszcza/pthreadpool/archive/f94ab76fe99754960035d520dce28e15b647e8cf.zip"
                         ],
                         "strip_prefix": "pthreadpool-f94ab76fe99754960035d520dce28e15b647e8cf"
                    },
                    "output_tree_hash": "f3e4ce8e316633300d5a68242fb4fdeeba904a20ec7e2a00db1dfeb1e98d7ed7"
               }
          ]
     },
     {
          "original_rule_class": "@@tsl//third_party:repo.bzl%_tf_http_archive",
          "definition_information": "Repository com_google_absl instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:46:15: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace2.bzl:164:19: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:597:28: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:43:9: in _initialize_third_party\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/absl/workspace.bzl:39:20: in repo\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/repo.bzl:136:21: in tf_http_archive\nRepository rule _tf_http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/repo.bzl:89:35: in <toplevel>\n",
          "original_attributes": {
               "name": "com_google_absl",
               "generator_name": "com_google_absl",
               "generator_function": "workspace",
               "generator_location": None,
               "sha256": "0320586856674d16b0b7a4d4afb22151bdc798490bb7f295eddd8f6a62b46fea",
               "urls": [
                    "https://storage.googleapis.com/mirror.tensorflow.org/github.com/abseil/abseil-cpp/archive/fb3621f4f897824c0dbe0615fa94543df6192f30.tar.gz",
                    "https://github.com/abseil/abseil-cpp/archive/fb3621f4f897824c0dbe0615fa94543df6192f30.tar.gz"
               ],
               "strip_prefix": "abseil-cpp-fb3621f4f897824c0dbe0615fa94543df6192f30",
               "patch_file": [
                    "@tsl//third_party/absl:nvidia_jetson.patch"
               ],
               "build_file": "@tsl//third_party/absl:com_google_absl.BUILD",
               "system_build_file": "@tsl//third_party/absl:system.BUILD",
               "system_link_files": {
                    "//third_party/absl:system.absl.algorithm.BUILD": "absl/algorithm/BUILD.bazel",
                    "//third_party/absl:system.absl.base.BUILD": "absl/base/BUILD.bazel",
                    "//third_party/absl:system.absl.cleanup.BUILD": "absl/cleanup/BUILD.bazel",
                    "//third_party/absl:system.absl.container.BUILD": "absl/container/BUILD.bazel",
                    "//third_party/absl:system.absl.debugging.BUILD": "absl/debugging/BUILD.bazel",
                    "//third_party/absl:system.absl.flags.BUILD": "absl/flags/BUILD.bazel",
                    "//third_party/absl:system.absl.functional.BUILD": "absl/functional/BUILD.bazel",
                    "//third_party/absl:system.absl.hash.BUILD": "absl/hash/BUILD.bazel",
                    "//third_party/absl:system.absl.memory.BUILD": "absl/memory/BUILD.bazel",
                    "//third_party/absl:system.absl.meta.BUILD": "absl/meta/BUILD.bazel",
                    "//third_party/absl:system.absl.numeric.BUILD": "absl/numeric/BUILD.bazel",
                    "//third_party/absl:system.absl.random.BUILD": "absl/random/BUILD.bazel",
                    "//third_party/absl:system.absl.status.BUILD": "absl/status/BUILD.bazel",
                    "//third_party/absl:system.absl.strings.BUILD": "absl/strings/BUILD.bazel",
                    "//third_party/absl:system.absl.synchronization.BUILD": "absl/synchronization/BUILD.bazel",
                    "//third_party/absl:system.absl.time.BUILD": "absl/time/BUILD.bazel",
                    "//third_party/absl:system.absl.types.BUILD": "absl/types/BUILD.bazel",
                    "//third_party/absl:system.absl.utility.BUILD": "absl/utility/BUILD.bazel"
               }
          },
          "repositories": [
               {
                    "rule_class": "@@tsl//third_party:repo.bzl%_tf_http_archive",
                    "attributes": {
                         "name": "com_google_absl",
                         "generator_name": "com_google_absl",
                         "generator_function": "workspace",
                         "generator_location": None,
                         "sha256": "0320586856674d16b0b7a4d4afb22151bdc798490bb7f295eddd8f6a62b46fea",
                         "urls": [
                              "https://storage.googleapis.com/mirror.tensorflow.org/github.com/abseil/abseil-cpp/archive/fb3621f4f897824c0dbe0615fa94543df6192f30.tar.gz",
                              "https://github.com/abseil/abseil-cpp/archive/fb3621f4f897824c0dbe0615fa94543df6192f30.tar.gz"
                         ],
                         "strip_prefix": "abseil-cpp-fb3621f4f897824c0dbe0615fa94543df6192f30",
                         "patch_file": [
                              "@tsl//third_party/absl:nvidia_jetson.patch"
                         ],
                         "build_file": "@tsl//third_party/absl:com_google_absl.BUILD",
                         "system_build_file": "@tsl//third_party/absl:system.BUILD",
                         "system_link_files": {
                              "//third_party/absl:system.absl.algorithm.BUILD": "absl/algorithm/BUILD.bazel",
                              "//third_party/absl:system.absl.base.BUILD": "absl/base/BUILD.bazel",
                              "//third_party/absl:system.absl.cleanup.BUILD": "absl/cleanup/BUILD.bazel",
                              "//third_party/absl:system.absl.container.BUILD": "absl/container/BUILD.bazel",
                              "//third_party/absl:system.absl.debugging.BUILD": "absl/debugging/BUILD.bazel",
                              "//third_party/absl:system.absl.flags.BUILD": "absl/flags/BUILD.bazel",
                              "//third_party/absl:system.absl.functional.BUILD": "absl/functional/BUILD.bazel",
                              "//third_party/absl:system.absl.hash.BUILD": "absl/hash/BUILD.bazel",
                              "//third_party/absl:system.absl.memory.BUILD": "absl/memory/BUILD.bazel",
                              "//third_party/absl:system.absl.meta.BUILD": "absl/meta/BUILD.bazel",
                              "//third_party/absl:system.absl.numeric.BUILD": "absl/numeric/BUILD.bazel",
                              "//third_party/absl:system.absl.random.BUILD": "absl/random/BUILD.bazel",
                              "//third_party/absl:system.absl.status.BUILD": "absl/status/BUILD.bazel",
                              "//third_party/absl:system.absl.strings.BUILD": "absl/strings/BUILD.bazel",
                              "//third_party/absl:system.absl.synchronization.BUILD": "absl/synchronization/BUILD.bazel",
                              "//third_party/absl:system.absl.time.BUILD": "absl/time/BUILD.bazel",
                              "//third_party/absl:system.absl.types.BUILD": "absl/types/BUILD.bazel",
                              "//third_party/absl:system.absl.utility.BUILD": "absl/utility/BUILD.bazel"
                         }
                    },
                    "output_tree_hash": "1f1d336018ccfd5c8ab6403e4af8d5009138b13113888a9cbe657e6ee2e66e79"
               }
          ]
     },
     {
          "original_rule_class": "//third_party:repo.bzl%_tf_http_archive",
          "definition_information": "Repository robin_map instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:46:15: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace2.bzl:171:28: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace2.bzl:29:14: in _initialize_third_party\n  /usr/local/google/home/kotlaja/bzl_mod/xla/third_party/robin_map/workspace.bzl:6:20: in repo\n  /usr/local/google/home/kotlaja/bzl_mod/xla/third_party/repo.bzl:138:21: in tf_http_archive\nRepository rule _tf_http_archive defined at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/third_party/repo.bzl:89:35: in <toplevel>\n",
          "original_attributes": {
               "name": "robin_map",
               "generator_name": "robin_map",
               "generator_function": "workspace",
               "generator_location": None,
               "sha256": "a8424ad3b0affd4c57ed26f0f3d8a29604f0e1f2ef2089f497f614b1c94c7236",
               "urls": [
                    "https://storage.googleapis.com/mirror.tensorflow.org/github.com/Tessil/robin-map/archive/refs/tags/v1.3.0.tar.gz",
                    "https://github.com/Tessil/robin-map/archive/refs/tags/v1.3.0.tar.gz"
               ],
               "strip_prefix": "robin-map-1.3.0",
               "build_file": "//third_party/robin_map:robin_map.BUILD"
          },
          "repositories": [
               {
                    "rule_class": "//third_party:repo.bzl%_tf_http_archive",
                    "attributes": {
                         "name": "robin_map",
                         "generator_name": "robin_map",
                         "generator_function": "workspace",
                         "generator_location": None,
                         "sha256": "a8424ad3b0affd4c57ed26f0f3d8a29604f0e1f2ef2089f497f614b1c94c7236",
                         "urls": [
                              "https://storage.googleapis.com/mirror.tensorflow.org/github.com/Tessil/robin-map/archive/refs/tags/v1.3.0.tar.gz",
                              "https://github.com/Tessil/robin-map/archive/refs/tags/v1.3.0.tar.gz"
                         ],
                         "strip_prefix": "robin-map-1.3.0",
                         "build_file": "//third_party/robin_map:robin_map.BUILD"
                    },
                    "output_tree_hash": "e7383e634937c565cd3288430b6517d610d88e39680b338f6e7ebc1106107679"
               }
          ]
     },
     {
          "original_rule_class": "//third_party:repo.bzl%_tf_http_archive",
          "definition_information": "Repository shardy instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:46:15: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace2.bzl:171:28: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace2.bzl:30:11: in _initialize_third_party\n  /usr/local/google/home/kotlaja/bzl_mod/xla/third_party/shardy/workspace.bzl:9:20: in repo\n  /usr/local/google/home/kotlaja/bzl_mod/xla/third_party/repo.bzl:138:21: in tf_http_archive\nRepository rule _tf_http_archive defined at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/third_party/repo.bzl:89:35: in <toplevel>\n",
          "original_attributes": {
               "name": "shardy",
               "generator_name": "shardy",
               "generator_function": "workspace",
               "generator_location": None,
               "sha256": "d8b224526ad73217fb32631a068c7887139a7538d71f96fd7a728ccccd907cd6",
               "urls": [
                    "https://storage.googleapis.com/mirror.tensorflow.org/github.com/openxla/shardy/archive/021f440d65b5d6cefb1bbd37627acf3983476255.zip",
                    "https://github.com/openxla/shardy/archive/021f440d65b5d6cefb1bbd37627acf3983476255.zip"
               ],
               "strip_prefix": "shardy-021f440d65b5d6cefb1bbd37627acf3983476255",
               "patch_file": [
                    "//third_party/shardy:temporary.patch"
               ]
          },
          "repositories": [
               {
                    "rule_class": "//third_party:repo.bzl%_tf_http_archive",
                    "attributes": {
                         "name": "shardy",
                         "generator_name": "shardy",
                         "generator_function": "workspace",
                         "generator_location": None,
                         "sha256": "d8b224526ad73217fb32631a068c7887139a7538d71f96fd7a728ccccd907cd6",
                         "urls": [
                              "https://storage.googleapis.com/mirror.tensorflow.org/github.com/openxla/shardy/archive/021f440d65b5d6cefb1bbd37627acf3983476255.zip",
                              "https://github.com/openxla/shardy/archive/021f440d65b5d6cefb1bbd37627acf3983476255.zip"
                         ],
                         "strip_prefix": "shardy-021f440d65b5d6cefb1bbd37627acf3983476255",
                         "patch_file": [
                              "//third_party/shardy:temporary.patch"
                         ]
                    },
                    "output_tree_hash": "5b26257aca89fe44865060cb7b4cff4f93a0561b13244cbb6316b8f5d693e148"
               }
          ]
     },
     {
          "original_rule_class": "@@tsl//third_party:repo.bzl%_tf_http_archive",
          "definition_information": "Repository snappy instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:46:15: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace2.bzl:164:19: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:604:21: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:381:20: in _tf_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/repo.bzl:136:21: in tf_http_archive\nRepository rule _tf_http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/repo.bzl:89:35: in <toplevel>\n",
          "original_attributes": {
               "name": "snappy",
               "generator_name": "snappy",
               "generator_function": "workspace",
               "generator_location": None,
               "sha256": "2e458b7017cd58dcf1469ab315389e85e7f445bd035188f2983f81fb19ecfb29",
               "urls": [
                    "https://storage.googleapis.com/mirror.tensorflow.org/github.com/google/snappy/archive/984b191f0fefdeb17050b42a90b7625999c13b8d.tar.gz",
                    "https://github.com/google/snappy/archive/984b191f0fefdeb17050b42a90b7625999c13b8d.tar.gz"
               ],
               "strip_prefix": "snappy-984b191f0fefdeb17050b42a90b7625999c13b8d",
               "build_file": "//third_party:snappy.BUILD",
               "system_build_file": "@tsl//third_party/systemlibs:snappy.BUILD"
          },
          "repositories": [
               {
                    "rule_class": "@@tsl//third_party:repo.bzl%_tf_http_archive",
                    "attributes": {
                         "name": "snappy",
                         "generator_name": "snappy",
                         "generator_function": "workspace",
                         "generator_location": None,
                         "sha256": "2e458b7017cd58dcf1469ab315389e85e7f445bd035188f2983f81fb19ecfb29",
                         "urls": [
                              "https://storage.googleapis.com/mirror.tensorflow.org/github.com/google/snappy/archive/984b191f0fefdeb17050b42a90b7625999c13b8d.tar.gz",
                              "https://github.com/google/snappy/archive/984b191f0fefdeb17050b42a90b7625999c13b8d.tar.gz"
                         ],
                         "strip_prefix": "snappy-984b191f0fefdeb17050b42a90b7625999c13b8d",
                         "build_file": "//third_party:snappy.BUILD",
                         "system_build_file": "@tsl//third_party/systemlibs:snappy.BUILD"
                    },
                    "output_tree_hash": "3bfa0d3999130dc5dce9a52483848fce4cb12ceabc8ca7b503fc90d74eb96287"
               }
          ]
     },
     {
          "original_rule_class": "@@tsl//third_party:repo.bzl%_tf_http_archive",
          "definition_information": "Repository ducc instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:46:15: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace2.bzl:164:19: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:597:28: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:45:9: in _initialize_third_party\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/ducc/workspace.bzl:8:20: in repo\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/repo.bzl:136:21: in tf_http_archive\nRepository rule _tf_http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/repo.bzl:89:35: in <toplevel>\n",
          "original_attributes": {
               "name": "ducc",
               "generator_name": "ducc",
               "generator_function": "workspace",
               "generator_location": None,
               "sha256": "077cf4bd0bd7eddaa6649a024285fff96e2662c5e6f2fb6ed5c5771f9de093f3",
               "urls": [
                    "https://storage.googleapis.com/mirror.tensorflow.org/gitlab.mpcdf.mpg.de/mtr/ducc/-/archive/aa46a4c21e440b3d416c16eca3c96df19c74f316/ducc-aa46a4c21e440b3d416c16eca3c96df19c74f316.tar.gz",
                    "https://gitlab.mpcdf.mpg.de/mtr/ducc/-/archive/aa46a4c21e440b3d416c16eca3c96df19c74f316/ducc-aa46a4c21e440b3d416c16eca3c96df19c74f316.tar.gz"
               ],
               "strip_prefix": "ducc-aa46a4c21e440b3d416c16eca3c96df19c74f316",
               "build_file": "//third_party/ducc:ducc.BUILD",
               "link_files": {
                    "//third_party/ducc:ducc0_custom_lowlevel_threading.h": "google/ducc0_custom_lowlevel_threading.h",
                    "//third_party/ducc:fft.h": "google/fft.h",
                    "//third_party/ducc:fft.cc": "google/fft.cc",
                    "//third_party/ducc:threading.cc": "google/threading.cc",
                    "//third_party/ducc:threading.h": "google/threading.h"
               }
          },
          "repositories": [
               {
                    "rule_class": "@@tsl//third_party:repo.bzl%_tf_http_archive",
                    "attributes": {
                         "name": "ducc",
                         "generator_name": "ducc",
                         "generator_function": "workspace",
                         "generator_location": None,
                         "sha256": "077cf4bd0bd7eddaa6649a024285fff96e2662c5e6f2fb6ed5c5771f9de093f3",
                         "urls": [
                              "https://storage.googleapis.com/mirror.tensorflow.org/gitlab.mpcdf.mpg.de/mtr/ducc/-/archive/aa46a4c21e440b3d416c16eca3c96df19c74f316/ducc-aa46a4c21e440b3d416c16eca3c96df19c74f316.tar.gz",
                              "https://gitlab.mpcdf.mpg.de/mtr/ducc/-/archive/aa46a4c21e440b3d416c16eca3c96df19c74f316/ducc-aa46a4c21e440b3d416c16eca3c96df19c74f316.tar.gz"
                         ],
                         "strip_prefix": "ducc-aa46a4c21e440b3d416c16eca3c96df19c74f316",
                         "build_file": "//third_party/ducc:ducc.BUILD",
                         "link_files": {
                              "//third_party/ducc:ducc0_custom_lowlevel_threading.h": "google/ducc0_custom_lowlevel_threading.h",
                              "//third_party/ducc:fft.h": "google/fft.h",
                              "//third_party/ducc:fft.cc": "google/fft.cc",
                              "//third_party/ducc:threading.cc": "google/threading.cc",
                              "//third_party/ducc:threading.h": "google/threading.h"
                         }
                    },
                    "output_tree_hash": "019d714911799250049d23eb6f703293d4fb626cf8463a71dd9c3cbc380ab999"
               }
          ]
     },
     {
          "original_rule_class": "@@tsl//third_party:repo.bzl%_tf_http_archive",
          "definition_information": "Repository farmhash_archive instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:46:15: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace2.bzl:164:19: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:597:28: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:47:13: in _initialize_third_party\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/farmhash/workspace.bzl:14:20: in repo\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/repo.bzl:136:21: in tf_http_archive\nRepository rule _tf_http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/repo.bzl:89:35: in <toplevel>\n",
          "original_attributes": {
               "name": "farmhash_archive",
               "generator_name": "farmhash_archive",
               "generator_function": "workspace",
               "generator_location": None,
               "sha256": "18392cf0736e1d62ecbb8d695c31496b6507859e8c75541d7ad0ba092dc52115",
               "urls": [
                    "https://storage.googleapis.com/mirror.tensorflow.org/github.com/google/farmhash/archive/0d859a811870d10f53a594927d0d0b97573ad06d.tar.gz",
                    "https://github.com/google/farmhash/archive/0d859a811870d10f53a594927d0d0b97573ad06d.tar.gz"
               ],
               "strip_prefix": "farmhash-0d859a811870d10f53a594927d0d0b97573ad06d",
               "build_file": "@tsl//third_party/farmhash:farmhash.BUILD"
          },
          "repositories": [
               {
                    "rule_class": "@@tsl//third_party:repo.bzl%_tf_http_archive",
                    "attributes": {
                         "name": "farmhash_archive",
                         "generator_name": "farmhash_archive",
                         "generator_function": "workspace",
                         "generator_location": None,
                         "sha256": "18392cf0736e1d62ecbb8d695c31496b6507859e8c75541d7ad0ba092dc52115",
                         "urls": [
                              "https://storage.googleapis.com/mirror.tensorflow.org/github.com/google/farmhash/archive/0d859a811870d10f53a594927d0d0b97573ad06d.tar.gz",
                              "https://github.com/google/farmhash/archive/0d859a811870d10f53a594927d0d0b97573ad06d.tar.gz"
                         ],
                         "strip_prefix": "farmhash-0d859a811870d10f53a594927d0d0b97573ad06d",
                         "build_file": "@tsl//third_party/farmhash:farmhash.BUILD"
                    },
                    "output_tree_hash": "0f55692e1dbb2720c3c3fbc3c302b29ce3ffdb1350e996e56158ea120483b27c"
               }
          ]
     },
     {
          "original_rule_class": "@@tsl//third_party:repo.bzl%_tf_http_archive",
          "definition_information": "Repository zlib instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:46:15: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace2.bzl:164:19: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:604:21: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:372:20: in _tf_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/repo.bzl:136:21: in tf_http_archive\nRepository rule _tf_http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/repo.bzl:89:35: in <toplevel>\n",
          "original_attributes": {
               "name": "zlib",
               "generator_name": "zlib",
               "generator_function": "workspace",
               "generator_location": None,
               "sha256": "9a93b2b7dfdac77ceba5a558a580e74667dd6fede4585b91eefb60f03b72df23",
               "urls": [
                    "https://storage.googleapis.com/mirror.tensorflow.org/zlib.net/zlib-1.3.1.tar.gz",
                    "https://zlib.net/zlib-1.3.1.tar.gz"
               ],
               "strip_prefix": "zlib-1.3.1",
               "build_file": "//third_party:zlib.BUILD",
               "system_build_file": "@tsl//third_party/systemlibs:zlib.BUILD"
          },
          "repositories": [
               {
                    "rule_class": "@@tsl//third_party:repo.bzl%_tf_http_archive",
                    "attributes": {
                         "name": "zlib",
                         "generator_name": "zlib",
                         "generator_function": "workspace",
                         "generator_location": None,
                         "sha256": "9a93b2b7dfdac77ceba5a558a580e74667dd6fede4585b91eefb60f03b72df23",
                         "urls": [
                              "https://storage.googleapis.com/mirror.tensorflow.org/zlib.net/zlib-1.3.1.tar.gz",
                              "https://zlib.net/zlib-1.3.1.tar.gz"
                         ],
                         "strip_prefix": "zlib-1.3.1",
                         "build_file": "//third_party:zlib.BUILD",
                         "system_build_file": "@tsl//third_party/systemlibs:zlib.BUILD"
                    },
                    "output_tree_hash": "972bef9bc8e47f329e12a12425c7439c38c9b4e19c33635f3dfb2b805ae94d5e"
               }
          ]
     },
     {
          "original_rule_class": "//third_party:repo.bzl%_tf_http_archive",
          "definition_information": "Repository pybind11_protobuf instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:46:15: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace2.bzl:178:21: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace2.bzl:154:20: in _tf_repositories\n  /usr/local/google/home/kotlaja/bzl_mod/xla/third_party/repo.bzl:138:21: in tf_http_archive\nRepository rule _tf_http_archive defined at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/third_party/repo.bzl:89:35: in <toplevel>\n",
          "original_attributes": {
               "name": "pybind11_protobuf",
               "generator_name": "pybind11_protobuf",
               "generator_function": "workspace",
               "generator_location": None,
               "sha256": "c7ab64b1ccf9a678694a89035a8c865a693e4e872803778f91f0965c2f281d78",
               "urls": [
                    "https://storage.googleapis.com/mirror.tensorflow.org/github.com/pybind/pybind11_protobuf/archive/80f3440cd8fee124e077e2e47a8a17b78b451363.zip",
                    "https://github.com/pybind/pybind11_protobuf/archive/80f3440cd8fee124e077e2e47a8a17b78b451363.zip"
               ],
               "strip_prefix": "pybind11_protobuf-80f3440cd8fee124e077e2e47a8a17b78b451363"
          },
          "repositories": [
               {
                    "rule_class": "//third_party:repo.bzl%_tf_http_archive",
                    "attributes": {
                         "name": "pybind11_protobuf",
                         "generator_name": "pybind11_protobuf",
                         "generator_function": "workspace",
                         "generator_location": None,
                         "sha256": "c7ab64b1ccf9a678694a89035a8c865a693e4e872803778f91f0965c2f281d78",
                         "urls": [
                              "https://storage.googleapis.com/mirror.tensorflow.org/github.com/pybind/pybind11_protobuf/archive/80f3440cd8fee124e077e2e47a8a17b78b451363.zip",
                              "https://github.com/pybind/pybind11_protobuf/archive/80f3440cd8fee124e077e2e47a8a17b78b451363.zip"
                         ],
                         "strip_prefix": "pybind11_protobuf-80f3440cd8fee124e077e2e47a8a17b78b451363"
                    },
                    "output_tree_hash": "c0f5fb4f56161997e636c6a6177d161e80ea57f68b671a2d5eb4e6cfa857f84e"
               }
          ]
     },
     {
          "original_rule_class": "@@tsl//third_party:repo.bzl%_tf_http_archive",
          "definition_information": "Repository pybind11_abseil instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:46:15: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace2.bzl:164:19: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:597:28: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:53:20: in _initialize_third_party\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/pybind11_abseil/workspace.bzl:13:20: in repo\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/repo.bzl:136:21: in tf_http_archive\nRepository rule _tf_http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/repo.bzl:89:35: in <toplevel>\n",
          "original_attributes": {
               "name": "pybind11_abseil",
               "generator_name": "pybind11_abseil",
               "generator_function": "workspace",
               "generator_location": None,
               "sha256": "0223b647b8cc817336a51e787980ebc299c8d5e64c069829bf34b69d72337449",
               "urls": [
                    "https://storage.googleapis.com/mirror.tensorflow.org/github.com/pybind/pybind11_abseil/archive/2c4932ed6f6204f1656e245838f4f5eae69d2e29.tar.gz",
                    "https://github.com/pybind/pybind11_abseil/archive/2c4932ed6f6204f1656e245838f4f5eae69d2e29.tar.gz"
               ],
               "strip_prefix": "pybind11_abseil-2c4932ed6f6204f1656e245838f4f5eae69d2e29",
               "patch_file": [
                    "//third_party/pybind11_abseil:remove_license.patch"
               ],
               "build_file": "//third_party/pybind11_abseil:BUILD"
          },
          "repositories": [
               {
                    "rule_class": "@@tsl//third_party:repo.bzl%_tf_http_archive",
                    "attributes": {
                         "name": "pybind11_abseil",
                         "generator_name": "pybind11_abseil",
                         "generator_function": "workspace",
                         "generator_location": None,
                         "sha256": "0223b647b8cc817336a51e787980ebc299c8d5e64c069829bf34b69d72337449",
                         "urls": [
                              "https://storage.googleapis.com/mirror.tensorflow.org/github.com/pybind/pybind11_abseil/archive/2c4932ed6f6204f1656e245838f4f5eae69d2e29.tar.gz",
                              "https://github.com/pybind/pybind11_abseil/archive/2c4932ed6f6204f1656e245838f4f5eae69d2e29.tar.gz"
                         ],
                         "strip_prefix": "pybind11_abseil-2c4932ed6f6204f1656e245838f4f5eae69d2e29",
                         "patch_file": [
                              "//third_party/pybind11_abseil:remove_license.patch"
                         ],
                         "build_file": "//third_party/pybind11_abseil:BUILD"
                    },
                    "output_tree_hash": "a0eccb236b2a24766632f6244e32f2979d4e42eab0bf399e63cfeb9db9cc37b8"
               }
          ]
     },
     {
          "original_rule_class": "@@tsl//third_party:repo.bzl%_tf_http_archive",
          "definition_information": "Repository implib_so instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:46:15: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace2.bzl:164:19: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:597:28: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:50:14: in _initialize_third_party\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/implib_so/workspace.bzl:7:20: in repo\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/repo.bzl:136:21: in tf_http_archive\nRepository rule _tf_http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/repo.bzl:89:35: in <toplevel>\n",
          "original_attributes": {
               "name": "implib_so",
               "generator_name": "implib_so",
               "generator_function": "workspace",
               "generator_location": None,
               "sha256": "4ef3089969d57a5b60bb41b8212c478eaa15c56941f86d4bf5e7f98a3afd24e8",
               "urls": [
                    "https://storage.googleapis.com/mirror.tensorflow.org/github.com/yugr/Implib.so/archive/2cce6cab8ff2c15f9da858ea0b68646a8d62aef2.tar.gz",
                    "https://github.com/yugr/Implib.so/archive/2cce6cab8ff2c15f9da858ea0b68646a8d62aef2.tar.gz"
               ],
               "strip_prefix": "Implib.so-2cce6cab8ff2c15f9da858ea0b68646a8d62aef2",
               "build_file": "//third_party/implib_so:implib_so.BUILD"
          },
          "repositories": [
               {
                    "rule_class": "@@tsl//third_party:repo.bzl%_tf_http_archive",
                    "attributes": {
                         "name": "implib_so",
                         "generator_name": "implib_so",
                         "generator_function": "workspace",
                         "generator_location": None,
                         "sha256": "4ef3089969d57a5b60bb41b8212c478eaa15c56941f86d4bf5e7f98a3afd24e8",
                         "urls": [
                              "https://storage.googleapis.com/mirror.tensorflow.org/github.com/yugr/Implib.so/archive/2cce6cab8ff2c15f9da858ea0b68646a8d62aef2.tar.gz",
                              "https://github.com/yugr/Implib.so/archive/2cce6cab8ff2c15f9da858ea0b68646a8d62aef2.tar.gz"
                         ],
                         "strip_prefix": "Implib.so-2cce6cab8ff2c15f9da858ea0b68646a8d62aef2",
                         "build_file": "//third_party/implib_so:implib_so.BUILD"
                    },
                    "output_tree_hash": "e3ff4694ce739ee99e64b1fbd45c965fb36996a8a59153ac8439cbb860ec77c6"
               }
          ]
     },
     {
          "original_rule_class": "@@tsl//third_party:repo.bzl%_tf_http_archive",
          "definition_information": "Repository curl instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:46:15: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace2.bzl:164:19: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:604:21: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:321:20: in _tf_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/repo.bzl:136:21: in tf_http_archive\nRepository rule _tf_http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/repo.bzl:89:35: in <toplevel>\n",
          "original_attributes": {
               "name": "curl",
               "generator_name": "curl",
               "generator_function": "workspace",
               "generator_location": None,
               "sha256": "264537d90e58d2b09dddc50944baf3c38e7089151c8986715e2aaeaaf2b8118f",
               "urls": [
                    "https://storage.googleapis.com/mirror.tensorflow.org/curl.se/download/curl-8.11.0.tar.gz",
                    "https://curl.se/download/curl-8.11.0.tar.gz"
               ],
               "strip_prefix": "curl-8.11.0",
               "build_file": "//third_party:curl.BUILD",
               "system_build_file": "@tsl//third_party/systemlibs:curl.BUILD"
          },
          "repositories": [
               {
                    "rule_class": "@@tsl//third_party:repo.bzl%_tf_http_archive",
                    "attributes": {
                         "name": "curl",
                         "generator_name": "curl",
                         "generator_function": "workspace",
                         "generator_location": None,
                         "sha256": "264537d90e58d2b09dddc50944baf3c38e7089151c8986715e2aaeaaf2b8118f",
                         "urls": [
                              "https://storage.googleapis.com/mirror.tensorflow.org/curl.se/download/curl-8.11.0.tar.gz",
                              "https://curl.se/download/curl-8.11.0.tar.gz"
                         ],
                         "strip_prefix": "curl-8.11.0",
                         "build_file": "//third_party:curl.BUILD",
                         "system_build_file": "@tsl//third_party/systemlibs:curl.BUILD"
                    },
                    "output_tree_hash": "49e2e586ade5ae40eae07cbcd65f031b4c60d03a46f490eef502da2baa5536e9"
               }
          ]
     },
     {
          "original_rule_class": "@@tsl//third_party:repo.bzl%_tf_http_archive",
          "definition_information": "Repository hwloc instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:46:15: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace2.bzl:164:19: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:597:28: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:49:10: in _initialize_third_party\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/hwloc/workspace.bzl:6:20: in repo\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/repo.bzl:136:21: in tf_http_archive\nRepository rule _tf_http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/repo.bzl:89:35: in <toplevel>\n",
          "original_attributes": {
               "name": "hwloc",
               "generator_name": "hwloc",
               "generator_function": "workspace",
               "generator_location": None,
               "sha256": "4cb0a781ed980b03ad8c48beb57407aa67c4b908e45722954b9730379bc7f6d5",
               "urls": [
                    "https://storage.googleapis.com/mirror.tensorflow.org/download.open-mpi.org/release/hwloc/v2.7/hwloc-2.7.1.tar.gz",
                    "https://download.open-mpi.org/release/hwloc/v2.7/hwloc-2.7.1.tar.gz"
               ],
               "strip_prefix": "hwloc-2.7.1",
               "build_file": "//third_party/hwloc:hwloc.BUILD",
               "system_build_file": "//third_party/hwloc:BUILD.system"
          },
          "repositories": [
               {
                    "rule_class": "@@tsl//third_party:repo.bzl%_tf_http_archive",
                    "attributes": {
                         "name": "hwloc",
                         "generator_name": "hwloc",
                         "generator_function": "workspace",
                         "generator_location": None,
                         "sha256": "4cb0a781ed980b03ad8c48beb57407aa67c4b908e45722954b9730379bc7f6d5",
                         "urls": [
                              "https://storage.googleapis.com/mirror.tensorflow.org/download.open-mpi.org/release/hwloc/v2.7/hwloc-2.7.1.tar.gz",
                              "https://download.open-mpi.org/release/hwloc/v2.7/hwloc-2.7.1.tar.gz"
                         ],
                         "strip_prefix": "hwloc-2.7.1",
                         "build_file": "//third_party/hwloc:hwloc.BUILD",
                         "system_build_file": "//third_party/hwloc:BUILD.system"
                    },
                    "output_tree_hash": "30e99c4faeb2d434b9c5b833d2f739f37cec6ec2af98fc0ff1967d117fb9adc9"
               }
          ]
     },
     {
          "original_rule_class": "@@tsl//third_party:repo.bzl%_tf_http_archive",
          "definition_information": "Repository eigen_archive instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:46:15: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace2.bzl:164:19: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:597:28: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:46:11: in _initialize_third_party\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/eigen3/workspace.bzl:14:20: in repo\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/repo.bzl:136:21: in tf_http_archive\nRepository rule _tf_http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/repo.bzl:89:35: in <toplevel>\n",
          "original_attributes": {
               "name": "eigen_archive",
               "generator_name": "eigen_archive",
               "generator_function": "workspace",
               "generator_location": None,
               "sha256": "1a432ccbd597ea7b9faa1557b1752328d6adc1a3db8969f6fe793ff704be3bf0",
               "urls": [
                    "https://storage.googleapis.com/mirror.tensorflow.org/gitlab.com/libeigen/eigen/-/archive/4c38131a16803130b66266a912029504f2cf23cd/eigen-4c38131a16803130b66266a912029504f2cf23cd.tar.gz",
                    "https://gitlab.com/libeigen/eigen/-/archive/4c38131a16803130b66266a912029504f2cf23cd/eigen-4c38131a16803130b66266a912029504f2cf23cd.tar.gz"
               ],
               "strip_prefix": "eigen-4c38131a16803130b66266a912029504f2cf23cd",
               "build_file": "@tsl//third_party/eigen3:eigen_archive.BUILD"
          },
          "repositories": [
               {
                    "rule_class": "@@tsl//third_party:repo.bzl%_tf_http_archive",
                    "attributes": {
                         "name": "eigen_archive",
                         "generator_name": "eigen_archive",
                         "generator_function": "workspace",
                         "generator_location": None,
                         "sha256": "1a432ccbd597ea7b9faa1557b1752328d6adc1a3db8969f6fe793ff704be3bf0",
                         "urls": [
                              "https://storage.googleapis.com/mirror.tensorflow.org/gitlab.com/libeigen/eigen/-/archive/4c38131a16803130b66266a912029504f2cf23cd/eigen-4c38131a16803130b66266a912029504f2cf23cd.tar.gz",
                              "https://gitlab.com/libeigen/eigen/-/archive/4c38131a16803130b66266a912029504f2cf23cd/eigen-4c38131a16803130b66266a912029504f2cf23cd.tar.gz"
                         ],
                         "strip_prefix": "eigen-4c38131a16803130b66266a912029504f2cf23cd",
                         "build_file": "@tsl//third_party/eigen3:eigen_archive.BUILD"
                    },
                    "output_tree_hash": "d73488451876e2ee74b167c74ae2f8424e8df1d9c7419b0c81e8dd864b43c458"
               }
          ]
     },
     {
          "original_rule_class": "@@tsl//third_party:repo.bzl%_tf_http_archive",
          "definition_information": "Repository FXdiv instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:46:15: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace2.bzl:164:19: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:604:21: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:120:20: in _tf_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/repo.bzl:136:21: in tf_http_archive\nRepository rule _tf_http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/repo.bzl:89:35: in <toplevel>\n",
          "original_attributes": {
               "name": "FXdiv",
               "generator_name": "FXdiv",
               "generator_function": "workspace",
               "generator_location": None,
               "sha256": "3d7b0e9c4c658a84376a1086126be02f9b7f753caa95e009d9ac38d11da444db",
               "urls": [
                    "https://storage.googleapis.com/mirror.tensorflow.org/github.com/Maratyszcza/FXdiv/archive/63058eff77e11aa15bf531df5dd34395ec3017c8.zip",
                    "https://github.com/Maratyszcza/FXdiv/archive/63058eff77e11aa15bf531df5dd34395ec3017c8.zip"
               ],
               "strip_prefix": "FXdiv-63058eff77e11aa15bf531df5dd34395ec3017c8"
          },
          "repositories": [
               {
                    "rule_class": "@@tsl//third_party:repo.bzl%_tf_http_archive",
                    "attributes": {
                         "name": "FXdiv",
                         "generator_name": "FXdiv",
                         "generator_function": "workspace",
                         "generator_location": None,
                         "sha256": "3d7b0e9c4c658a84376a1086126be02f9b7f753caa95e009d9ac38d11da444db",
                         "urls": [
                              "https://storage.googleapis.com/mirror.tensorflow.org/github.com/Maratyszcza/FXdiv/archive/63058eff77e11aa15bf531df5dd34395ec3017c8.zip",
                              "https://github.com/Maratyszcza/FXdiv/archive/63058eff77e11aa15bf531df5dd34395ec3017c8.zip"
                         ],
                         "strip_prefix": "FXdiv-63058eff77e11aa15bf531df5dd34395ec3017c8"
                    },
                    "output_tree_hash": "a04d0907bb060d82ef39b6cb5a60b17daf226ec272d47a88c95815719ec08794"
               }
          ]
     },
     {
          "original_rule_class": "//third_party:repo.bzl%_tf_http_archive",
          "definition_information": "Repository boringssl instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:46:15: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace2.bzl:178:21: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace2.bzl:107:20: in _tf_repositories\n  /usr/local/google/home/kotlaja/bzl_mod/xla/third_party/repo.bzl:138:21: in tf_http_archive\nRepository rule _tf_http_archive defined at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/third_party/repo.bzl:89:35: in <toplevel>\n",
          "original_attributes": {
               "name": "boringssl",
               "generator_name": "boringssl",
               "generator_function": "workspace",
               "generator_location": None,
               "sha256": "9dc53f851107eaf87b391136d13b815df97ec8f76dadb487b58b2fc45e624d2c",
               "urls": [
                    "https://storage.googleapis.com/mirror.tensorflow.org/github.com/google/boringssl/archive/c00d7ca810e93780bd0c8ee4eea28f4f2ea4bcdc.tar.gz",
                    "https://github.com/google/boringssl/archive/c00d7ca810e93780bd0c8ee4eea28f4f2ea4bcdc.tar.gz"
               ],
               "strip_prefix": "boringssl-c00d7ca810e93780bd0c8ee4eea28f4f2ea4bcdc",
               "system_build_file": "//third_party/systemlibs:boringssl.BUILD"
          },
          "repositories": [
               {
                    "rule_class": "//third_party:repo.bzl%_tf_http_archive",
                    "attributes": {
                         "name": "boringssl",
                         "generator_name": "boringssl",
                         "generator_function": "workspace",
                         "generator_location": None,
                         "sha256": "9dc53f851107eaf87b391136d13b815df97ec8f76dadb487b58b2fc45e624d2c",
                         "urls": [
                              "https://storage.googleapis.com/mirror.tensorflow.org/github.com/google/boringssl/archive/c00d7ca810e93780bd0c8ee4eea28f4f2ea4bcdc.tar.gz",
                              "https://github.com/google/boringssl/archive/c00d7ca810e93780bd0c8ee4eea28f4f2ea4bcdc.tar.gz"
                         ],
                         "strip_prefix": "boringssl-c00d7ca810e93780bd0c8ee4eea28f4f2ea4bcdc",
                         "system_build_file": "//third_party/systemlibs:boringssl.BUILD"
                    },
                    "output_tree_hash": "9c275b3dcb5cf9e75aa209113d94d70e61cba83ca513e9a3b715c8654f9572ed"
               }
          ]
     },
     {
          "original_rule_class": "//third_party:repo.bzl%_tf_http_archive",
          "definition_information": "Repository com_google_ortools instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:46:15: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace2.bzl:178:21: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace2.bzl:115:20: in _tf_repositories\n  /usr/local/google/home/kotlaja/bzl_mod/xla/third_party/repo.bzl:138:21: in tf_http_archive\nRepository rule _tf_http_archive defined at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/third_party/repo.bzl:89:35: in <toplevel>\n",
          "original_attributes": {
               "name": "com_google_ortools",
               "generator_name": "com_google_ortools",
               "generator_function": "workspace",
               "generator_location": None,
               "sha256": "bc4b07dc9c23f0cca43b1f5c889f08a59c8f2515836b03d4cc7e0f8f2c879234",
               "urls": [
                    "https://storage.googleapis.com/mirror.tensorflow.org/github.com/google/or-tools/archive/v9.6.tar.gz",
                    "https://github.com/google/or-tools/archive/v9.6.tar.gz"
               ],
               "strip_prefix": "or-tools-9.6",
               "patch_file": [
                    "//third_party/ortools:ortools.patch"
               ]
          },
          "repositories": [
               {
                    "rule_class": "//third_party:repo.bzl%_tf_http_archive",
                    "attributes": {
                         "name": "com_google_ortools",
                         "generator_name": "com_google_ortools",
                         "generator_function": "workspace",
                         "generator_location": None,
                         "sha256": "bc4b07dc9c23f0cca43b1f5c889f08a59c8f2515836b03d4cc7e0f8f2c879234",
                         "urls": [
                              "https://storage.googleapis.com/mirror.tensorflow.org/github.com/google/or-tools/archive/v9.6.tar.gz",
                              "https://github.com/google/or-tools/archive/v9.6.tar.gz"
                         ],
                         "strip_prefix": "or-tools-9.6",
                         "patch_file": [
                              "//third_party/ortools:ortools.patch"
                         ]
                    },
                    "output_tree_hash": "50b9cb52c0fe398121dfaa01ddabf03feeaab758ad6cd865617c45e3c90570b2"
               }
          ]
     },
     {
          "original_rule_class": "@@tsl//third_party:repo.bzl%_tf_http_archive",
          "definition_information": "Repository onednn instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:46:15: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace2.bzl:164:19: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:604:21: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:149:20: in _tf_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/repo.bzl:136:21: in tf_http_archive\nRepository rule _tf_http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/repo.bzl:89:35: in <toplevel>\n",
          "original_attributes": {
               "name": "onednn",
               "generator_name": "onednn",
               "generator_function": "workspace",
               "generator_location": None,
               "sha256": "8356aa9befde4d4ff93f1b016ac4310730b2de0cc0b8c6c7ce306690bc0d7b43",
               "urls": [
                    "https://storage.googleapis.com/mirror.tensorflow.org/github.com/oneapi-src/oneDNN/archive/refs/tags/v3.5.tar.gz",
                    "https://github.com/oneapi-src/oneDNN/archive/refs/tags/v3.5.tar.gz"
               ],
               "strip_prefix": "oneDNN-3.5",
               "build_file": "@tsl//third_party/mkl_dnn:mkldnn_v1.BUILD"
          },
          "repositories": [
               {
                    "rule_class": "@@tsl//third_party:repo.bzl%_tf_http_archive",
                    "attributes": {
                         "name": "onednn",
                         "generator_name": "onednn",
                         "generator_function": "workspace",
                         "generator_location": None,
                         "sha256": "8356aa9befde4d4ff93f1b016ac4310730b2de0cc0b8c6c7ce306690bc0d7b43",
                         "urls": [
                              "https://storage.googleapis.com/mirror.tensorflow.org/github.com/oneapi-src/oneDNN/archive/refs/tags/v3.5.tar.gz",
                              "https://github.com/oneapi-src/oneDNN/archive/refs/tags/v3.5.tar.gz"
                         ],
                         "strip_prefix": "oneDNN-3.5",
                         "build_file": "@tsl//third_party/mkl_dnn:mkldnn_v1.BUILD"
                    },
                    "output_tree_hash": "5e2d4384bf49521a153479d5fdd19fc745f8ae736a8763d9d174bb8b03bba87d"
               }
          ]
     },
     {
          "original_rule_class": "//third_party:repo.bzl%_tf_http_archive",
          "definition_information": "Repository scip instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:46:15: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace2.bzl:178:21: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace2.bzl:137:20: in _tf_repositories\n  /usr/local/google/home/kotlaja/bzl_mod/xla/third_party/repo.bzl:138:21: in tf_http_archive\nRepository rule _tf_http_archive defined at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/third_party/repo.bzl:89:35: in <toplevel>\n",
          "original_attributes": {
               "name": "scip",
               "generator_name": "scip",
               "generator_function": "workspace",
               "generator_location": None,
               "sha256": "fe7636f8165a8c9298ff55ed3220d084d4ea31ba9b69d2733beec53e0e4335d6",
               "urls": [
                    "https://storage.googleapis.com/mirror.tensorflow.org/github.com/scipopt/scip/archive/refs/tags/v803.tar.gz",
                    "https://github.com/scipopt/scip/archive/refs/tags/v803.tar.gz"
               ],
               "strip_prefix": "scip-803",
               "patch_file": [
                    "//third_party/ortools:scip.patch"
               ],
               "build_file": "//third_party/ortools:scip.BUILD"
          },
          "repositories": [
               {
                    "rule_class": "//third_party:repo.bzl%_tf_http_archive",
                    "attributes": {
                         "name": "scip",
                         "generator_name": "scip",
                         "generator_function": "workspace",
                         "generator_location": None,
                         "sha256": "fe7636f8165a8c9298ff55ed3220d084d4ea31ba9b69d2733beec53e0e4335d6",
                         "urls": [
                              "https://storage.googleapis.com/mirror.tensorflow.org/github.com/scipopt/scip/archive/refs/tags/v803.tar.gz",
                              "https://github.com/scipopt/scip/archive/refs/tags/v803.tar.gz"
                         ],
                         "strip_prefix": "scip-803",
                         "patch_file": [
                              "//third_party/ortools:scip.patch"
                         ],
                         "build_file": "//third_party/ortools:scip.BUILD"
                    },
                    "output_tree_hash": "30779f24cdbe61862c75089f5bb31362e74394658ab421b9835cb71eaf3b07fe"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/cpp:cc_configure.bzl%cc_autoconf",
          "definition_information": "Repository local_config_cc instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:181:13: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/cpp/cc_configure.bzl:149:16: in cc_configure\nRepository rule cc_autoconf defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/cpp/cc_configure.bzl:109:30: in <toplevel>\n",
          "original_attributes": {
               "name": "local_config_cc",
               "generator_name": "local_config_cc",
               "generator_function": "cc_configure",
               "generator_location": None
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/cpp:cc_configure.bzl%cc_autoconf",
                    "attributes": {
                         "name": "local_config_cc",
                         "generator_name": "local_config_cc",
                         "generator_function": "cc_configure",
                         "generator_location": None
                    },
                    "output_tree_hash": "46f512d703a35e88c83869199242aec8809d2901ec56420c652b793c67bf1cf3"
               }
          ]
     },
     {
          "original_rule_class": "@@tsl//third_party:repo.bzl%_tf_http_archive",
          "definition_information": "Repository XNNPACK instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:46:15: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace2.bzl:164:19: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:604:21: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:112:20: in _tf_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/repo.bzl:136:21: in tf_http_archive\nRepository rule _tf_http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/repo.bzl:89:35: in <toplevel>\n",
          "original_attributes": {
               "name": "XNNPACK",
               "generator_name": "XNNPACK",
               "generator_function": "workspace",
               "generator_location": None,
               "sha256": "face04056299ca22e2dbbf122a27aef289443dc7b1ad7e33a52714d6acc084eb",
               "urls": [
                    "https://storage.googleapis.com/mirror.tensorflow.org/github.com/google/XNNPACK/archive/e55b3998cadb320188759aaada27328cbacc3253.zip",
                    "https://github.com/google/XNNPACK/archive/e55b3998cadb320188759aaada27328cbacc3253.zip"
               ],
               "strip_prefix": "XNNPACK-e55b3998cadb320188759aaada27328cbacc3253"
          },
          "repositories": [
               {
                    "rule_class": "@@tsl//third_party:repo.bzl%_tf_http_archive",
                    "attributes": {
                         "name": "XNNPACK",
                         "generator_name": "XNNPACK",
                         "generator_function": "workspace",
                         "generator_location": None,
                         "sha256": "face04056299ca22e2dbbf122a27aef289443dc7b1ad7e33a52714d6acc084eb",
                         "urls": [
                              "https://storage.googleapis.com/mirror.tensorflow.org/github.com/google/XNNPACK/archive/e55b3998cadb320188759aaada27328cbacc3253.zip",
                              "https://github.com/google/XNNPACK/archive/e55b3998cadb320188759aaada27328cbacc3253.zip"
                         ],
                         "strip_prefix": "XNNPACK-e55b3998cadb320188759aaada27328cbacc3253"
                    },
                    "output_tree_hash": "149f0100ce0b79fad6059fa1fb5cdac5c9bf8b28158a033d9f0f5fb1ac0016fe"
               }
          ]
     },
     {
          "original_rule_class": "//third_party:repo.bzl%_tf_http_archive",
          "definition_information": "Repository bliss instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:46:15: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace2.bzl:178:21: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace2.bzl:146:20: in _tf_repositories\n  /usr/local/google/home/kotlaja/bzl_mod/xla/third_party/repo.bzl:138:21: in tf_http_archive\nRepository rule _tf_http_archive defined at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/third_party/repo.bzl:89:35: in <toplevel>\n",
          "original_attributes": {
               "name": "bliss",
               "generator_name": "bliss",
               "generator_function": "workspace",
               "generator_location": None,
               "sha256": "f57bf32804140cad58b1240b804e0dbd68f7e6bf67eba8e0c0fa3a62fd7f0f84",
               "urls": [
                    "https://storage.googleapis.com/mirror.tensorflow.org/github.com/google/or-tools/releases/download/v9.0/bliss-0.73.zip",
                    "https://github.com/google/or-tools/releases/download/v9.0/bliss-0.73.zip"
               ],
               "build_file": "//third_party/ortools:bliss.BUILD"
          },
          "repositories": [
               {
                    "rule_class": "//third_party:repo.bzl%_tf_http_archive",
                    "attributes": {
                         "name": "bliss",
                         "generator_name": "bliss",
                         "generator_function": "workspace",
                         "generator_location": None,
                         "sha256": "f57bf32804140cad58b1240b804e0dbd68f7e6bf67eba8e0c0fa3a62fd7f0f84",
                         "urls": [
                              "https://storage.googleapis.com/mirror.tensorflow.org/github.com/google/or-tools/releases/download/v9.0/bliss-0.73.zip",
                              "https://github.com/google/or-tools/releases/download/v9.0/bliss-0.73.zip"
                         ],
                         "build_file": "//third_party/ortools:bliss.BUILD"
                    },
                    "output_tree_hash": "beb0e849fec4af9ac972a3f88f41d1ae0c3503b16082dd06331c6d1bbe0fefc5"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/osx:xcode_configure.bzl%xcode_autoconf",
          "definition_information": "Repository local_config_xcode instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:184:16: in <toplevel>\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/osx/xcode_configure.bzl:312:19: in xcode_configure\nRepository rule xcode_autoconf defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/bazel_tools/tools/osx/xcode_configure.bzl:297:33: in <toplevel>\n",
          "original_attributes": {
               "name": "local_config_xcode",
               "generator_name": "local_config_xcode",
               "generator_function": "xcode_configure",
               "generator_location": None,
               "xcode_locator": "@bazel_tools//tools/osx:xcode_locator.m"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/osx:xcode_configure.bzl%xcode_autoconf",
                    "attributes": {
                         "name": "local_config_xcode",
                         "generator_name": "local_config_xcode",
                         "generator_function": "xcode_configure",
                         "generator_location": None,
                         "xcode_locator": "@bazel_tools//tools/osx:xcode_locator.m"
                    },
                    "output_tree_hash": "ec026961157bb71cf68d1b568815ad68147ed16f318161bc0da40f6f3d7d79fd"
               }
          ]
     },
     {
          "original_rule_class": "@@tsl//third_party:repo.bzl%_tf_http_archive",
          "definition_information": "Repository cpuinfo instantiated at:\n  /usr/local/google/home/kotlaja/bzl_mod/xla/WORKSPACE:46:15: in <toplevel>\n  /usr/local/google/home/kotlaja/bzl_mod/xla/workspace2.bzl:164:19: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:604:21: in workspace\n  /usr/local/google/home/kotlaja/bzl_mod/xla/tsl_workspace2.bzl:134:20: in _tf_repositories\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/repo.bzl:136:21: in tf_http_archive\nRepository rule _tf_http_archive defined at:\n  /usr/local/google/home/kotlaja/.cache/bazel/_bazel_kotlaja/bf563bc3155929aa8f95908b12484cfd/external/tsl/third_party/repo.bzl:89:35: in <toplevel>\n",
          "original_attributes": {
               "name": "cpuinfo",
               "generator_name": "cpuinfo",
               "generator_function": "workspace",
               "generator_location": None,
               "sha256": "52e0ffd7998d8cb3a927d8a6e1145763744d866d2be09c4eccea27fc157b6bb0",
               "urls": [
                    "https://storage.googleapis.com/mirror.tensorflow.org/github.com/pytorch/cpuinfo/archive/cebb0933058d7f181c979afd50601dc311e1bf8c.zip",
                    "https://github.com/pytorch/cpuinfo/archive/cebb0933058d7f181c979afd50601dc311e1bf8c.zip"
               ],
               "strip_prefix": "cpuinfo-cebb0933058d7f181c979afd50601dc311e1bf8c"
          },
          "repositories": [
               {
                    "rule_class": "@@tsl//third_party:repo.bzl%_tf_http_archive",
                    "attributes": {
                         "name": "cpuinfo",
                         "generator_name": "cpuinfo",
                         "generator_function": "workspace",
                         "generator_location": None,
                         "sha256": "52e0ffd7998d8cb3a927d8a6e1145763744d866d2be09c4eccea27fc157b6bb0",
                         "urls": [
                              "https://storage.googleapis.com/mirror.tensorflow.org/github.com/pytorch/cpuinfo/archive/cebb0933058d7f181c979afd50601dc311e1bf8c.zip",
                              "https://github.com/pytorch/cpuinfo/archive/cebb0933058d7f181c979afd50601dc311e1bf8c.zip"
                         ],
                         "strip_prefix": "cpuinfo-cebb0933058d7f181c979afd50601dc311e1bf8c"
                    },
                    "output_tree_hash": "62f4af4e67ed3f6dcdebd280bc1f1c3b64e8822b0bcfe90a5c2af96c0b00c3ff"
               }
          ]
     }
]