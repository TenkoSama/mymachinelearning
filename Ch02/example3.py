# -*- coding: utf-8 -*- 

from numpy import array
import kNN
datingDataMat,datingLabels = kNN.file2matrix('E:\VSCode\machinelearning\CH2\datingTestSet2.txt') 
#写完整路径可以F5运行，不完整时只能用命令行python example2.py运行
import matplotlib
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
ax.axis([-5000,100000,-2,25])
ax.scatter(datingDataMat[:,0],datingDataMat[:,1],15.0*array(datingLabels),15.0*array(datingLabels))
plt.show()
