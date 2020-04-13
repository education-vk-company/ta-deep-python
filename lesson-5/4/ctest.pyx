
cpdef test(int n):
    cdef int res = 1
    cdef int i
    for i in range(1, n+1):
        res *= i
    return res
