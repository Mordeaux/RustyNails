from ctypes import cdll

lib = cdll.LoadLibrary("target/release/librusty_nails.dylib")

lib.process()

print("done!")
