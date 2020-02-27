import gc
import ctypes
import weakref


class PyObject(ctypes.Structure):
    _fields_ = [("refcnt", ctypes.c_long)]


gc.disable()

class A:
    def __init__(self, b):
        self.b = b

    def __del__(self):
        print('del a')


class B:
    def __init__(self, a):
        self.a = a

    def __del__(self):
        print('del b')


a = A(None)
b = B(None)
a.b = b
b.a = a


def del_obj():
    print('finalize obj')

ref_b = weakref.finalize(b, del_obj)

a_id = id(a)
b_id = id(b)

print('before del a:', PyObject.from_address(a_id).refcnt)
print('before del b:', PyObject.from_address(b_id).refcnt)

del a
del b

print('after del a:', PyObject.from_address(a_id).refcnt)
print('after del b:', PyObject.from_address(b_id).refcnt)

print('collect')
gc.collect()
print('after collect')

print('after collect a:', PyObject.from_address(a_id).refcnt)
print('after collect b:', PyObject.from_address(b_id).refcnt)
