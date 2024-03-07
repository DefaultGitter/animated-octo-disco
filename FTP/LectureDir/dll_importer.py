import ctypes

# ctypes.CDLL('c:/PyW/GG13/lib/test_lib.dll')
# ctypes.CDLL('../../lib/test_lib.dll')

# ctypes.CDLL('./lib/test_lib.dll')

my_dll = ctypes.CDLL('../../lib/test_lib.dll')

my_dll.Func_name('parameters')
