# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 12:05:16 2018

@author: Se

玩客狐相关计算
"""

#run fox -x 12 -y 11 -z 16 -i 6 -e 104 -t 3.8002 -s 3

import sys
import getopt

if __name__ == '__main__':
    opts, args = getopt.getopt(sys.argv[1:], 'hx:y:z:i:e:t:s:', [ 'help', 'index=', 'x_p =', 'y_p =', 'z_p =', 'i_p =', 'e_p =', 't_p =', 's_p =' ])
    
    x = 0
    y = 0
    z = 0
    i = 0
    e = 0
    t = 0
    s = 0
    
    # 入口函数，不明白怎么调用参数的可以看下
    for key, value in opts:
        if key in ['-h', '--help']:
            print('参数定义：')
            print('-x, --x_p\t第一个属性')
            print('-y, --y_p\t第二个属性')
            print('-z, --z_p\t第三个属性')
            print('-i, --i_p\t代数')
            print('-e, --e_p\t能量')
            print('-t, --t_p\t今日能量')
            print('-s, --s_p\t已生育次数')
            sys.exit(0)
        if key in ['-x', '--x_p']:
            x = float(value)
        if key in ['-y', '--y_p']:
            y = float(value)
        if key in ['-z', '--z_p']:
            z = float(value)
        if key in ['-i', '--i_p']:
            i = float(value)
        if key in ['-e', '--e_p']:
            e = float(value)
        if key in ['-t', '--t_p']:
            t = float(value)
        if key in ['-s', '--s_p']:
            s = float(value)
    
    score = e * z * t / i
    print(score)
    
    time = 1.42**s*i/(1+y**2/1000)
    print(time)
    
    
    