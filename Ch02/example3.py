# -*- coding: utf-8 -*- 

from numpy import array
import kNN
datingDataMat,datingLabels = kNN.file2matrix('E:\VSCode\mymachinelearning\Ch02\datingTestSet2.txt') 
#写完整路径可以F5运行，不完整时只能用命令行python example2.py运行
import matplotlib
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
#add_subplot(111)又写作add_subplot(1,1,1),即add_subplot(i,j,n)表示把figure分为i行，j列的小方块，把图像画在第n块的地方。
ax.axis([-5000,100000,-2,25])
#axis调整坐标轴范围
ax.scatter(datingDataMat[:,0],datingDataMat[:,1],15.0*array(datingLabels),15.0*array(datingLabels),'o',alpha=0.5)
#scatter个性化设置 利用变量datingLabels存储的分类标签属性
#scatter(xData,yData,color,size,marker)
#alpha透明度
plt.show()
