import matplotlib.pyplot as plt

from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['KaiTi']

# coding=utf-8

squares = [0,1,4,9,16,25,36,49,64]
plt.plot(squares,linewidth = 5)

#设置图表标题，并给坐标轴加上标签
plt.title("平方图",fontsize = 20)
plt.xlabel("x",fontsize = 14)
plt.ylabel("y",fontsize = 15)

#设置刻度标记的大小
plt.tick_params(axis='both',labelsize = 14)
plt.show()