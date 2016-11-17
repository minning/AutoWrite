#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Jupiter on 2016/10/31
'''
    代码目的：

'''
import time


def timeDecor(func):

    def innerDef(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        t = t2 - t1
        print "{0}函数部分运行时间 ：{1}s".format(str(func.__name__),t)
        return result
    return innerDef




























































    
    
    
    
    
    