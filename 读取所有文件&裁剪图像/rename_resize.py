# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 09:30:44 2018

@author: Se
"""

import os
import cv2

def rename(data_dir):
    
    index = 1
    list_dir = os.listdir(data_dir)
    num = len(list_dir)
    length = len(str(num))
    
    for file in list_dir:    #os.listdir('.')遍历文件夹内的每个文件名，并返回一个包含文件名的list
        file_names = file.split('.')
        new_name = str(index).zfill(length) + '.' + file_names[-1]
        os.rename(data_dir + file, data_dir + new_name)
        index += 1    
          
def delete_file_folder(src):
    '''delete files and folders'''
    if os.path.isfile(src):
        try:
            os.remove(src)
        except:
            pass
    elif os.path.isdir(src):
        for item in os.listdir(src):
            itemsrc=os.path.join(src,item)
            delete_file_folder(itemsrc)


def resizeImg(in_dir, out_dir, width = 480, height = 300):
    for file in os.listdir(in_dir):
        name = in_dir + file
        image = cv2.imread(name)
        if image.shape[1]/image.shape[0] > width/height:
            t_width = int(image.shape[1] / image.shape[0] * height)
            temp = cv2.resize(image, (t_width, height), interpolation = cv2.INTER_CUBIC)
            dest = temp[0:height, int(t_width/2 - width/2):int(t_width/2 - width/2) + width]
            cv2.imwrite(out_dir + file, dest)
        else:
            t_height = int(image.shape[0] / image.shape[1] * width)
            temp = cv2.resize(image, (width, t_height), interpolation = cv2.INTER_CUBIC)
            dest = temp[int(t_height/2 - height/2):int(t_height/2 - height/2) + height, 0: width]
            cv2.imwrite(out_dir + file, dest)            
                

if __name__ == '__main__':
    
    data_dir = './destold/'
    dest_dir = './1/'
    
    #rename(data_dir)
    delete_file_folder(dest_dir) 
    resizeImg(data_dir, dest_dir)
    

        

