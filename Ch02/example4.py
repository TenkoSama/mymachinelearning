# -*- coding: utf-8 -*- 
from numpy import array
import kNN


def datingClassTest():
    hoRatio = 0.10
    #take 10% for testing
    datingDataMat, datingLabels = kNN.file2matrix('datingTestSet2.txt')
    normMat, ranges, minVals = kNN.autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m*hoRatio)
    #总数据量的10%，取整
    errorCount = 0.0
    for i in range(numTestVecs):
        #\换行
        classifierResult = kNN.classify0(normMat[i,:], normMat[numTestVecs:m,:],\
        datingLabels[numTestVecs:m], 3)
        print "the classifier came back with: %d, the real answer is: %d" \
        % (classifierResult,datingLabels[i])
        if (classifierResult != datingLabels[i]):
            errorCount += 1.0
    print "the total error rate is: %f" % (errorCount/float(numTestVecs)) 
        

