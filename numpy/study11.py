# numpy包的学习
# 结构化数组
import numpy as np
mydtype = np.dtype([("name","S10"),("age","int")])
people = np.empty((2,2),mydtype)
people["name"]=[["bob","hao"],["allen","clin"]]
people["age"]=[[12,32],[43,23]]
print(people)

