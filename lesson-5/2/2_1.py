#! /usr/bin/env python

import cffi

if __name__ == "__main__":
    ffi = cffi.FFI()
    lib = ffi.dlopen('./lib2.so')

    ffi.cdef('''
    int sum(int *arr, int len);
    ''')

    ffi.set_source('_sample', r"""
    int sum(int *arr, int len)
    {
        int res = 0;
        for (int i = 0; i < len; ++i)
        {
            res += arr[i];
        }
        return res;
    }
    """)
    ffi.compile()
