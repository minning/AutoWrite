#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Jupiter on 2016/11/7
'''
    代码目的：

'''
from __init__ import timeDecor


@timeDecor
def reduceMat(f,newF):
    '''
    读取文件f，将f中的数据剪切后放入newF中
    :param f:
    :param newF:
    :return:
    '''
    with open(f,'r') as myFile:
        newFile = open(newF,'w')
        lineNum = 0
        for line in myFile:
            lineList = line.split()
            reduLine = '\t'.join(lineList[:10])
            if "type" in line:
                newFile.write(reduLine+"\n")
                lineNum = 0
            if lineNum<10:
                if "type" not in line:
                    newFile.write(reduLine+'\n')
                    lineNum += 1
            if "#" in line:
                newFile.write(reduLine + "\n")

f1 = r'StructMatrix.txt'
newF1 = r'ReduStructMatrix.txt'
reduceMat(f1,newF1)

f2 = r"TestStructMatrix.txt"
newF2 = r"ReduTestStructMatrix.txt"
reduceMat(f2,newF2)


















































    
    
    
    
    
    