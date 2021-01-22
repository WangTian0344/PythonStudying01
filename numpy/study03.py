# numpy包的学习
# numpy方法
import numpy as np
import numpy.random as rand
a = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
print("a数组和为{}".format(np.sum(a)))
print("a数组第0维和{},第1维和{}".format(np.sum(a,axis=0),np.sum(a,axis=1)))
print("a数组积为{}".format(np.prod(a)))
print("a数组第0维积{},第1维积{}".format(np.prod(a,axis=0),np.prod(a,axis=1)))

print("a数组最小值{}".format(np.min(a)))
print("a数组第0维最小值{}".format(np.min(a,axis=0)))
# max方法同min

print("a数组最小值位置{}".format(np.argmin(a)))
print("a数组第0维最小值位置{}".format(np.argmin(a,axis=0)))
# argmax方法同argmin

print("a数组均值{}".format(np.mean(a)))
print("a数组第1维均值{}".format(np.mean(a,axis=1)))

# axis确定维数
print("a数组的标准差{}".format(np.std(a)))
print("a数组的方差{}".format(np.var(a)))

print("a数组最大值与最小值之差{}".format(np.ptp(a)))

# 随机数组
b = rand.rand(3,3)
print(b)
# 近似1位 四舍五入
print(np.round(b,decimals=1))
