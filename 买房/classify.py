# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 17:13:37 2018

@author: Se
"""

import openpyxl

if __name__ == '__main__':
    
    wb = openpyxl.reader.excel.load_workbook('江山汇总.xlsx')
    sheetnames = wb.get_sheet_names()  
    ws = wb.get_sheet_by_name(sheetnames[0])

    # 获取表头
    colnames = []
    for cell in list(ws.rows)[0]:
        colnames.append(cell.value)

    # 获取所有数据
    nrows = ws.max_row #行数 
    city = []  
    for rownum in range(1, nrows):  
        app = {} 
        index = 0
        for cell in list(ws.rows)[rownum]:
            app[colnames[index]] = cell.value
            index += 1
        city.append(app)
    
    daoli = []
    nangang = []
    daowai = []
    xiangfang = []
    pingfang = []
    taiping = []
    songbei = []
    kaifa = []
    wuchang = []
    binxian = []
    tonghe = []
    yanshou = []
    binzhou = []
    yilan = []
    shuangcheng = []
    binxi = []
    other = []
    shangzhi = []
    dongli = []
    acheng = []
    hulan = []
    
    
    for i in city:
        temp = i['地点']
        if '道里' in temp:
            daoli.append(i)
        elif '南岗' in temp:
            nangang.append(i)
        elif '道外' in temp:
            daowai.append(i)
        elif '香坊' in temp:
            xiangfang.append(i)
        elif '平房' in temp:
            pingfang.append(i)
        elif '太平' in temp:
            taiping.append(i)
        elif '松北' in temp:
            songbei.append(i)
        elif '开发' in temp:
            kaifa.append(i)
        elif '五常' in temp:
            wuchang.append(i)
        elif '宾县' in temp:
            binxian.append(i)
        elif '通河' in temp:
            tonghe.append(i)
        elif '延寿' in temp:
            yanshou.append(i)
        elif '宾州' in temp:
            binzhou.append(i)
        elif '依兰' in temp:
            yilan.append(i)
        elif '双城' in temp:
            shuangcheng.append(i)
        elif '宾西' in temp:
            binxi.append(i)
        elif '尚志' in temp:
            shangzhi.append(i)
        elif '动力' in temp:
            dongli.append(i)
        elif '阿城' in temp:
            acheng.append(i)
        elif '呼兰' in temp:
            hulan.append(i)
        else:
            other.append(i)

        

