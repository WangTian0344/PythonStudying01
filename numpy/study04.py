# numpy包的学习
# 排序
import numpy as np
import numpy.random as rand
names = np.array(["bob","cliena","deva","allen"])
weights = np.array([65.5,84.4,96.1,60.2])

# sort从小到大排序且不会改变原数组
print("names数组从小到大排序{}".format(np.sort(names)))
# argsort 从小到大排序后的位置
print("names数组从小到大排序位置{}".format(np.argsort(names)))
print("names从小到大排序后，weights数组对应{}".format(weights[np.argsort(names)]))

b = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

print("b二维数组排序,默认按行排序\n{}".format(np.sort(b)))

c = np.sort(np.round(rand.rand(5),decimals=1))
d = np.round(rand.rand(5),decimals=1)
print(c)
print(d)
print("将d数组插入已经排序好的c数组中的位置\n{}".format(np.searchsorted(c,d)))
print(c)
