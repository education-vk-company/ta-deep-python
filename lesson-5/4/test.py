#! /usr/bin/env python

def test(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

if __name__ == "__main__":
    for i in range(1, 5):
        print("n! = {}".format(test(i)))
