# numpy包的学习
# 矩阵
import numpy as np
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
A = np.mat(a)
print("A矩阵\n{}".format(A))
B = np.mat("9,8,7;6,5,4;3,2,1")
print("B矩阵\n{}".format(B))

x = np.array([[2],[4],[5]])
print("矩阵A和向量x的乘积\n{}".format(A*x))

print("矩阵A和其逆矩阵的乘积\n{}".format(A*A.I))

print("矩阵A连乘4次\n{}".format(A**4))