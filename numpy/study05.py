# numpy包学习
# 数组形状
import numpy as np
a = np.arange(6)
print(a)
print("a的形状{}".format(a.shape))

a.shape = 3,2
print(a)
print("a的形状{}".format(a.shape))

a = a.reshape(6)
print(a)
print("a的形状{}".format(a.shape))

b = np.arange(6)
print("b的形状{}".format(b.shape))
b = b[np.newaxis,:]
print("b的形状{}".format(b.shape))
b = b[:,np.newaxis,np.newaxis]
print("b的形状{}".format(b.shape))
# squeeze 去除长度是1的维度
b = np.squeeze(b)
print("b的形状{}".format(b.shape))
# 转置
c = np.arange(6)
c.shape = 2,3
print(c.T)
print(c)
# 数组连接
x = np.array([[1,2,3],
              [4,5,6]])
y = np.array([[7,8,9],
              [10,11,12]])
print("x和y在第0维链接\n{}".format(np.vstack((x,y))))
print("x和y在第1维链接\n{}".format(np.hstack((x,y))))
# dstack在原来的维数上加一
print("x和y在第2维链接\n{}".format(np.dstack((x,y))))

print("将x和y连接成的三维数组转化为一维数组\n{}".format(np.dstack((x,y)).flatten()))

k = np.array([1,2],[3,4])
l = k.ravel()


