# -*- coding: utf-8 -*- 

import numpy
import kNN
datingDataMat,datingLabels = kNN.file2matrix('E:\VSCode\machinelearning\CH2\datingTestSet2.txt')
#写完整路径可以F5运行，不完整时只能用命令行python example1.py运行
#datingDataMat,datingLabels = kNN.file2matrix('datingTestSet2.txt')
import matplotlib
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(datingDataMat[:,1],datingDataMat[:,2])
plt.show()