#! /usr/bin/env python

import cffi

if __name__ == "__main__":
    ffi = cffi.FFI()
    lib = ffi.dlopen('./lib2.so')

    ffi.cdef('''
    struct Point
    {
        int x;
        int y;
    };
    int area(struct Point *p1, struct Point *p2);
    ''')

    #arr = [1,2,3,4]
    #print("Res of sum is {}".format(lib.sum(arr, len(arr))))

    p1 = ffi.new('struct Point *')
    p2 = ffi.new('struct Point *')

    p1.x, p1.y = (10, 10)
    p2.x, p2.y = (0, 0)

    area = lib.area(p1, p2)
    print(f"Area of two points is {area}")
