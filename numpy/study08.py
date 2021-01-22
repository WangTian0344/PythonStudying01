# numpy包的学习
# 向量化函数
import numpy as np
import matplotlib.pyplot as plt

def sinc(x):
    if x == 0.0:
        return 1.0
    else:
        w = np.pi * x
        return np.sin(x)/w
# 函数向量化
vsinc = np.vectorize(sinc)
x = np.linspace(-5,5,101)
plt.plot(x,vsinc(x))
plt.show()