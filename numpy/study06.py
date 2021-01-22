# numpy包的学习
# 对角线
import numpy as np
a = np.array([1,2,3,4,5,6,7,8,9])
a.shape = 3,3
print("a的对角线元素{}".format(a.diagonal()))
print("a的对角线元素右移一位{}".format(a.diagonal(offset=1)))

# 数组转字符串
b = np.array([1,2,3,4],dtype=np.uint8)
b = b.tostring()
print(b)
# 从字符串读取相应数据类型数据
b = np.fromstring(b,dtype=np.uint8)
print(b)