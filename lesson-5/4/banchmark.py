#! /usr/bin/env python

import time

import test
import ctest

N = 12

if __name__ == "__main__":
    start_ts = time.time()
    res = test.test(N)
    end_ts = time.time()
    python_ts = end_ts - start_ts
    print(f"Res={res}, time={python_ts}s")

    start_ts = time.time()
    res = ctest.test(N)
    end_ts = time.time()
    cython_ts = end_ts - start_ts
    print(f"Res={res}, time={cython_ts}s")
    print("Delta={}".format(python_ts/cython_ts))
       
