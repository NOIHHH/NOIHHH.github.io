from config import *

_DEFAULT_ENV = ["LANG=en_US.UTF-8", "LANGUAGE=en_US:en", "LC_ALL=en_US.UTF-8"]

LANGUAGE_SETTINGS = {
    'c': {
        "src_name": "main.c",
        "exe_name": "main",
        "max_memory": 128 * 1024 * 1024,
        "compile_cmd": "/usr/bin/gcc -DONLINE_JUDGE -w -std=c99 {src_path} -lm -o {exe_path}",
        "exe_cmd": "{exe_path}",
        "seccomp_rule": "c_cpp",
        "env": [] + _DEFAULT_ENV
    },
    'cpp': {
        "src_name": "main.cpp",
        "exe_name": "main",
        "max_memory": 128 * 1024 * 1024,
        "compile_cmd": "/usr/bin/g++ -DONLINE_JUDGE -w -fmax-errors=3 -std=c++11 {src_path} -lm -o {exe_path}",
        "exe_cmd": "{exe_path}",
        "seccomp_rule": "c_cpp",
        "env": [] + _DEFAULT_ENV
    },
    'pas': {
        "src_name": "main.pas",
        "exe_name": "main",
        "max_memory": 128 * 1024 * 1024,
        "compile_cmd": "/usr/bin/fpc {src_path}",
        "exe_cmd": "{exe_path}",
        "seccomp_rule": "c_cpp",
        "env": ['/usr/bin'] + _DEFAULT_ENV
    },
    'java': {
        "src_name": "Main.java",
        "exe_name": "Main",
        "max_memory": -1,
        "compile_cmd": "/usr/bin/javac {src_path} -encoding UTF8",
        "exe_cmd": "/usr/bin/java -cp {exe_dir} -Xss1M -XX:MaxPermSize=16M -XX:PermSize=8M -Xms16M -Xmx{max_memory}M "
                   "-Djava.security.manager -Dfile.encoding=UTF-8 -Djava.security.policy==/etc/java_policy -Djava.awt.headless=true {exe_name}",
        "seccomp_rule": None,
        "env": ["MALLOC_ARENA_MAX=1"] + _DEFAULT_ENV
    },
    'python': {
        # A Naive solution of copy
        "src_name": "solution.py",
        "exe_name": "solution.py",  # TODO assign exe_path when compile
        "max_memory": 128 * 1024 * 1024,
        "compile_cmd": "/usr/bin/python3 -m py_compile {src_path}",
        "exe_cmd": "/usr/bin/python3 {exe_path}",
        "seccomp_rule": "general",
        "env": [] + _DEFAULT_ENV
    }
}
