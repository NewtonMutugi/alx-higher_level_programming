#!/usr/bin/python3 -u

import ctypes

lib = ctypes.CDLL('./libPython.so')
lib.print_python_list.argtypes = [ctypes.py_object]
lib.print_python_bytes.argtypes = [ctypes.py_object]
lib.print_python_float.argtypes = [ctypes.py_object]
s = b"Hello"
lib.print_python_bytes(s)
b = b'\xff\xf8\x00\x00\x00\x00\x00\x00'
lib.print_python_bytes(b)
b = b'What does the \'b\' character do in front of a string literal?'
lib.print_python_bytes(b)
list = [b'Hello', b'World']
lib.print_python_list(list)
del list[1]
lib.print_python_list(list)
list = list + [4, 5, 6.0, (9, 8), [9, 8, 1024], b"School", "Betty"]
lib.print_python_list(list)
list = []
lib.print_python_list(list)
list.append(0)
lib.print_python_list(list)
list.append(1)
list.append(2)
list.append(3)
list.append(4)
lib.print_python_list(list)
list.pop()
lib.print_python_list(list)
list = ["School"]
lib.print_python_list(list)
lib.print_python_bytes(list)
f = 3.14
lib.print_python_float(f)
list = [
    -1.0, -0.1, 0.0, 1.0, 3.14, 3.14159, 3.14159265, 3.14159265356]
print(list)
lib.print_python_list(list)
lib.print_python_float(list)
lib.print_python_list(f)
