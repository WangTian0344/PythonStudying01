import matplotlib.pyplot as plt
import numpy as np


"""plt.plot([1,2,4,5],[4,6,2,6],"cv")
# 确定显示范围
plt.axis([0,4,0,7])
plt.show()"""

x = np.linspace(-np.pi,np.pi)
y = np.sin(x)
z = np.cos(x)

plt.plot(x,y,linewidth=2.0,color="red")
plt.plot(x,z,linewidth=2.0,color="green")
plt.show()