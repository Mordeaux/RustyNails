import os
from ctypes import cdll
from sys import platform

DIRECTORY = os.path.dirname(os.path.abspath(__file__))

if platform == "darwin":
    ext = "dylib"
else:
    ext = "so"

rust_lib_path = os.path.join(
        DIRECTORY,
        os.pardir,
        'rust',
        'rusty_nails',
        'target',
        'release',
        'librusty_nails.{}').format(ext)

rusty_nails = cdll.LoadLibrary(rust_lib_path)
