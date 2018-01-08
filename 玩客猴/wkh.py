# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 18:14:18 2018

@author: Se
"""

import re
import csv

if __name__ == '__main__':
    
    index = 0
    s1 = []
    s21 = []
    s22 = []
    s31 = []
    s32 = []
    s33 = []
    s34 = []
    s4 = []
    
    file = open("test.txt")
    for line in file:
        index += 1
        if index % 4 == 1:
            t1 = re.findall(r"\d+\.?\d*",line)
            s1.append(t1[0])
        elif index % 4 == 2:
            t2 = re.findall(r"\d+\.?\d*",line)
            s21.append(t2[0])
            s22.append(t2[1])
        elif index % 4 == 3:
            t3 = re.findall(r"\d+\.?\d*",line)
            s31.append(t3[0])
            s32.append(t3[1])
            s33.append(t3[2])
            s34.append(t3[3])
        else:
            t4 = re.findall(r"\d+\.?\d*",line)
            s4.append(t4[0])

        

    # 存储表头
    with open('price.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for i in range(len(s1)):
            row = []
            row.append(s1[i])
            row.append(s21[i])
            row.append(s22[i])
            row.append(s31[i])
            row.append(s32[i])
            row.append(s33[i])
            row.append(s34[i])
            row.append(s4[i])
            writer.writerow(row)
        f.close()
    
    
    