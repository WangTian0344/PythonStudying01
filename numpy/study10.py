# numpy包的学习
# 文本中读取数组
import numpy as np
# 空格或制表符分隔的文本文档
data = []
with open("text01.txt") as f:
    for line in f:
        fileds = line.split()
        row_data = [float(x) for x in fileds]
        data.append(row_data)
data = np.array(data)
print(data)

data2 = np.loadtxt("text01.txt")
print(data2)

data3 = np.loadtxt('text02.txt',
                  skiprows=1,         # 忽略第一行
                  dtype=np.int,      # 数组类型
                  delimiter=',',     # 逗号分割
                  usecols=(0,1,2,4), # 指定使用哪几列数据
                  comments='%'       # 百分号为注释符
                 )
print(data3)

data4 = np.array([1,2],[3,4])
np.savetxt("text03.txt",data4,fmt="%.4f",delimiter=",")