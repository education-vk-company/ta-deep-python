#! /usr/bin/env python

import ctypes

if __name__ == "__main__":
    lib = ctypes.CDLL('./lib1.so')
    print("Check out simple function...")
    for _ in range(10):
        print(lib.simple_function())

    print("Check out change_string...")
    original_string = 'Hello, world!'
    mutable_string = ctypes.create_string_buffer(str.encode(original_string))
    print(f"Before call func [{mutable_string.value}]")
    lib.change_string(mutable_string)
    print(f"After call func [{mutable_string.value}]")

    print("Check out allocate and free functions...")
    alloc_func = lib.alloc_str
    dir(alloc_func)
    alloc_func.restype = ctypes.POINTER(ctypes.c_char);

    allocated_str = alloc_func()
    phrase = ctypes.c_char_p.from_buffer(allocated_str)
    print(f"Allocated text: {phrase.value}")

    free_func = lib.free_str
    free_func.argtypes = [ctypes.POINTER(ctypes.c_char)]
    free_func(allocated_str)
