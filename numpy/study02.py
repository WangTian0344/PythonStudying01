# numpy包的学习
# 复数
import numpy as np
a = np.array([1+2j,3,5,6])
print(a)
print(a.real)
print(a.imag)
a.imag = [2,3,4,5]

print("a内部数据类型{}".format(a.dtype))

print("a的共轭复数{}".format(a.conj()))

b = np.array([2,6,8,3],dtype=np.int8)
print("b内部数据类型{}".format(b.dtype))
# asarray
c = np.asarray(b,dtype=np.float32)
print(c)
number = 10
d = np.asarray(number,dtype=np.int16)
print(d)
# astype
print(c.astype(np.float64))
# view 按照类型进行解析
print(c.view(np.uint8))
