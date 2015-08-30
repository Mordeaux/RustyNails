from ctypes import Structure, c_wchar_p, c_int
from ctypes import byref, c_void_p, c_uint
from ctypes import POINTER

from config import rusty_nails


class LinearRegression(Structure):
    """This class should contain methods that allow the user to
    configure and process a linear regression algorithm."""
    _fields_ = [
            ('name', c_wchar_p),
            ('input', c_int),
            ('output', c_void_p)]

    def process(self):
        print rusty_nails.process_regression(byref(self))


rusty_nails.init_regression.argtypes = (c_wchar_p, c_uint)
rusty_nails.init_regression.restype = LinearRegression

if __name__ == '__main__':
    linear_regression = rusty_nails.init_regression('mordeaux', 500)
    linear_regression.process()
