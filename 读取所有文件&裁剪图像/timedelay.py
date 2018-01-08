# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 12:29:34 2018

@author: Se

延时测试程序
"""

import time

if __name__ == '__main__':
    
    index = 0
    for i in range(500):
        time.sleep(2)
        print(index)
        index += 1