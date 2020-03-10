#! /usr/bin/env python

import random
from typing import List

def counting_sort(l: List[int]) -> List[int]:
    res: List[int] = [0] * len(l)
    max_elem = max(l)
    tmp = [0] * (max_elem+1)
    for num in l:
        tmp[num] += 1

    for i in range(1, len(tmp)):
        tmp[i] += tmp[i-1]

    for i in range(len(l)-1, -1, -1):
        pos = tmp[l[i]]-1
        res[pos] = l[i]
        tmp[l[i]] -= 1
    return res

def main():
    l = [random.randint(0, 20) for _ in range(10)]
    print("Before", l)
    print("After", counting_sort(l))

if __name__ == "__main__":
    main()
    
