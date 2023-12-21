import numpy as np
import ctypes as ct

_libmycamera = ct.cdll['/Users/lorenzospera/Desktop/libmycamera.so'] 
#_libmycamera = np.ctypeslib.load_library('libmycamera','.') 

_libmycamera.read_camera.argtypes = [ct.c_char_p]
_libmycamera.read_camera.restype = ct.c_int

#a = ct.create_string_buffer(1536*1024*2)

def read():
    a = ct.create_string_buffer(1536*1024*2)
    _libmycamera.read_camera(a)
    return a
    

