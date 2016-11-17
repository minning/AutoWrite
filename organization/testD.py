#coding:utf-8
#!/usr/bin/env python
#PyCharm Python2.7
# Created by jupiter on 17/11/2016

'''
    代码目的：

'''
from __init__ import timeDecor

import time


@timeDecor
def sayTime():
    for i in range(3):
        print i
        time.sleep(2)


sayTime()











































































