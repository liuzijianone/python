from numpy import *
import  matplotlib
import  matplotlib.pyplot as plt
import operator

def createDataSet():
    group=array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels=['A','A','B','B']
    return group,labels

# group,label=createDataSet()
# print(group,label)

def file2matrix(filename):
    fr=open(filename)
    arrayOLines=fr.readlines()
    numberOLines=len(arrayOLines)
    returnMat=zeros((numberOLines,3))
    classLabelVector=[]
    index=0
    for line in arrayOLines:
        line=line.strip()
        listFromLine=line.split('\t')
        returnMat[index,:]=listFromLine[0:3]
        classLabelVector.append(listFromLine[-1])
        index+=1
    return returnMat,classLabelVector

# datingDataMat,datingLabels=file2matrix('datingTestSet.txt')
# print(datingDataMat)
# print(datingLabels)

# fig=plt.figure()
# ax=fig.add_subplot(111)
# ax.scatter(datingDataMat[:,1],datingDataMat[:,2])
# plt.show()

def autoNorm(dataSet):
    minVals=dataSet.min(0)
    maxVals=dataSet.max(0)
    ranges=maxVals-minVals
    normDataSet=zeros(shape(dataSet))
    m=dataSet.shape[0]
    normDataSet=dataSet-tile(minVals,(m,1))
    normDataSet=normDataSet/tile(ranges,(m,1))
    return normDataSet,ranges,minVals