import gc
import ctypes


class PyObject(ctypes.Structure):
    _fields_ = [("refcnt", ctypes.c_long)]


gc.disable()


lst = []
lst.append(lst)

lst_id = id(lst)
del lst

obj1 = {}
obj2 = {}
obj1['obj2'] = obj2
obj2['obj1'] = obj1

obj1_id = id(obj1)
del obj1, obj2

print('lst ref_cnt:', PyObject.from_address(lst_id).refcnt)
print('obj1 ref_cnt:', PyObject.from_address(obj1_id).refcnt)

print('collect', gc.collect())

print("--- after gc.collect() ----")
print('lst ref_cnt:', PyObject.from_address(lst_id).refcnt)
print('obj1 ref_cnt:', PyObject.from_address(obj1_id).refcnt)
