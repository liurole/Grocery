# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 09:30:44 2018

@author: Se
"""

import os



if __name__ == '__main__':
    
    data_dir = './data/'
    
    index = 1
    list_dir = os.listdir(data_dir)
    num = len(list_dir)
    length = len(str(num))
    
    for file in list_dir:    #os.listdir('.')遍历文件夹内的每个文件名，并返回一个包含文件名的list
        file_names = file.split('.')
        new_name = str(index).zfill(length) + '.' + file_names[-1]
        os.rename(data_dir + file, data_dir + new_name)
        index += 1
        

