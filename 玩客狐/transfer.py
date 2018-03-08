# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 20:31:24 2018

@author: Se
"""

import sys
import getopt

# 喂食函数
def feed(num, first, last):
    result = {}
    result['0.1'] = int((num + last) * first * 2)
    result['0.6'] = int((num + last) * first)
    result['0.3'] = int((num + last) * first * 0.5)
    return result

if __name__ == '__main__':
    opts, args = getopt.getopt(sys.argv[1:], 'hf:s:l:', [ 'help', 'first =', 'second =', 'last =' ])

    first = 10
    second = 10
    last = str(1234)
    
    for key, value in opts:

        if key in ['-h', '--help']:
            print('狐狸化丹分析')
            print('参数定义：')
            print('-h, --help\t显示帮助')
            print('-f, --first\t成长值')
            print('-s, --second\t生育值')
            print('-l, --last\t编号')
            sys.exit(0)
        if key in ['-f', '--first']:
            first = int(value)
        if key in ['-s', '--second']:
            second = int(value)
        if key in ['-l', '--last']:
            last = value 
    
    # 逆序
    last = last[::-1]
    last = float(last) / (10**len(last))
    
    
    