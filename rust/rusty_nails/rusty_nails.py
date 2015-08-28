from ctypes import cdll
from sys import platform

if platform == "darwin":
    ext = "dylib"
else:
    ext = "so"

lib = cdll.LoadLibrary('target/release/librusty_nails.' + ext)
lib.process()

print("Python is done!")
