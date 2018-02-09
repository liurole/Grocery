import requests
from bs4 import BeautifulSoup
import time
import xlrd 

def open_excel(file):  
    data = xlrd.open_workbook(file)  
    return data

def excel_table_byindex(file, colnameindex = 0, by_index = 0):  
    data = open_excel(file)  
    table = data.sheets()[by_index]  
    nrows = table.nrows #行数   
    colnames = table.row_values(colnameindex) #某一行数据  
    list = []  
    for rownum in range(1,nrows):  
        row = table.row_values(rownum)#以列表格式输出  
        if row:  
            app = {}  
            for i in range(len(colnames)):  
                app[colnames[i]] = row[i]  
            list.append(app)#向列表中插入字典类型的数据  
    return list  

#查询是否注册
def check(domain):
    url = "http://panda.www.net.cn/cgi-bin/check.cgi?area_domain=%s"%domain
    html = requests.get(url)
    bsj = BeautifulSoup(html.text,"lxml")
    onum = bsj.find("original")
    if onum != None:
        num = onum.get_text()[:3]
        if num == '210':
            print("%s可以注册"%domain)
        elif num == "213":
            print("查询超时，请重新查询")
        elif num == "211":
            print("%s域名已注册"%domain)
        else:
            print("出现未知问题")
        return num
    else:
        print("让我哭一会，ip可能被封了")
        return None

#保存可注册域名
def domain(names):
    oklist = []
    for name in names:
        domain = name+'.com' 
        time.sleep(1)
        num = check(domain)
        if num != None:
            if num == '210':
                oklist.append(domain)
        else:
            break
    with open('oklist.txt','w+') as ok:
        for k in oklist:
            s = k+'\n'
            ok.write(s)
    return oklist

# 组成name
def domainlist(parts):
    names = []
    for i in range(len(parts)):
        for j in range(i + 1, len(parts)):
            temp1 = parts[i]['部件'] + parts[j]['部件']
            temp2 = parts[j]['部件'] + parts[i]['部件']
            names.append(temp1)
            names.append(temp2)
    return names
    
    
if __name__ == '__main__':
    
    parts = excel_table_byindex('域名.xlsx') 
    names = domainlist(parts)
    oklist = domain(names)