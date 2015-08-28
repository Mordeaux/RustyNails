import os
from ctypes import cdll
from sys import platform

# Get the absolute path of the current directory so this file can be
# called from outside its home directory.
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

if platform == "darwin":
    ext = "dylib"
else:
    ext = "so"

rust_lib_path = os.path.join(DIRECTORY, 'target/release/librusty_nails.{}').format(ext)

lib = cdll.LoadLibrary(rust_lib_path)
lib.process()

print("Python is done!")
