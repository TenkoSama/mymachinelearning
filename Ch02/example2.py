# -*- coding: utf-8 -*- 

from numpy import array
import kNN
datingDataMat,datingLabels = kNN.file2matrix('E:\VSCode\mymachinelearning\Ch02\datingTestSet2.txt') 
#写完整路径可以F5运行，不完整时只能用命令行python example2.py运行
import matplotlib
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(datingDataMat[:,1],datingDataMat[:,2],15.0*array(datingLabels),15.0*array(datingLabels))
plt.show()
