# numpy包的学习
# 向量运算
import numpy as np
a = np.array([1,2])
b = np.array([3,4])

print("a+b={}".format(np.add(a,b)))
print("a*b={}".format(np.multiply(a,b)))
print("a==b {}".format(np.equal(a,b)))
print("a<<2={}".format(np.left_shift(a,2)))

c = np.array([5,7])
c.shape = 2,1
print("a+c={}".format(np.add(a,c)))