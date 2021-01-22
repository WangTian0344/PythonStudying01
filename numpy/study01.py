# numpy包的学习
import numpy as np

b = np.array([1,2,3,4])
# 类型
print(b)
print("b的属性{}".format(type(b)))
print("b内部数据的属性{}".format(b.dtype))
print("b的形状{}".format(np.shape(b)))
print("b的尺寸{}".format(np.size(b)))
print("b内部数据的空间大小{}字节".format(b.nbytes))
print("b数组维数{}".format(b.ndim))
# numpy中的array可以实现自加一
b = b + 1
print(b)
# 索引
print(b[0])
print(b[1:3])
# 设定值
b.fill(3)
print(b)

# 多维数组
a=np.array([[1,2,3],
            [4,5,6],
            [7,8,9]])
print(a)

# 多维数组索引是浅拷贝机制，该表引用值即改变原值
a[0,2]=33
print(a)

c=np.array([0,4,-6,3,-8])
print(c>0)
print(np.where(c>0))