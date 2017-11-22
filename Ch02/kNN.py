# -*- coding: utf-8 -*- 
'''
Created on Aug 21, 2017
kNN: k Nearest Neighbors

Input:      inX: vector to compare to existing dataset (1xN)
            dataSet: size m data set of known vectors (NxM)
            labels: data set labels (1xM vector)
            k: number of neighbors to use for comparison (should be an odd number)         
Output:     the most popular class label

@author: pbharrin
'''

from numpy import *
import operator

def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group, labels

def classify0(inX,dataSet,labels,k):
    detaSetSize = dataSet.shape[0]
    # 距离计算
    diffMat = tile(inX,(detaSetSize,1)) - dataSet   # 偏差
    sqDiffMat = diffMat**2  # 平方
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()
    # argsort()函数是将distances中的元素从小到大排列，
    # 提取其对应的index(索引)，即顺序号
    
    # 然后赋值到sortedDistIndicies
    classCount = {}
    # 选择距离最小的K个点
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        # 从最近到最远取最近k个
        classCount[voteIlabel] = classCount.get(voteIlabel,0)+1
    sortedClassCount = sorted(classCount.iteritems(),
    key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]

def file2matrix(filename):
    fr = open(filename)
    arrayOlines = fr.readlines()
    numberOflines = len(arrayOlines)    # 得到文件行数
    returnMat = zeros((numberOflines,3))    # 返回矩阵
    classLabelVector = []
    index = 0
    # 解析数据
    for line in arrayOlines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat,classLabelVector

def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m,1))
    # the NumPy tile() function 
    #tile(originData,RepeatSize)
    # to create a matrix the same size as our input matrix 
    #and filled with copies of minVals
    normDataSet = normDataSet/tile(ranges, (m,1)) #element-wise division
    #In other numeric software packages, 
    # the / operator can be used for matrix division, 
    # but in NumPy you need to use linalg.solve(matA,matB) for matrix division.
    return normDataSet, ranges, minVals

