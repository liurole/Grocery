# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 22:03:08 2018

@author: Se

实现了公积金贷款房子的查找
新增利用pandas来保存表格

下载chromedrive驱动 
使用Selenium需要选择一个调用的浏览器并下载好对应的驱动，本文使用chrome浏览器，当然也可以用FireFox等
http://www.seleniumhq.org/download/ 找到Google Chrome Driver链接
对应驱动放在python目录下面的scripts目录中，例如C:\ProgramData\Anaconda3\envs\python35\Scripts
"""
import requests
import re
import urllib
import pandas as pd
from bs4 import BeautifulSoup

# 利用request，导入cookies，header进行关键词网页搜索，选择第二栏
def check(url):
    headers = {
    'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'
    }
    try:
        response = requests.get(url, headers = headers)
        if response.status_code == 200:
            return response.text
        return None
    except ConnectionError:
        print('Error occurred')
        return None

# 获取所有搜索结果链接
def get_all_urls(html):    
    names = []
    urls = []
    soup = BeautifulSoup(html, 'lxml')
    result = soup.select('.fontSize3 a')
    if len(result) == 0:
        return names, urls
    else:
        for i in result:
            temp = i.get('href')
            urls.append(temp)
            temp = i.get_text()
            names.append(temp)
        return names, urls

# 保存所有页面
def search_all_urls(url):
    response = check(url)
    # 得到标题，段落，图片
    soup = BeautifulSoup(response, 'lxml')
    title = soup.select('.tylm_pagejgjs_title')
    title = title[0].get_text()    
    
    try:
        dfs = pd.read_html(response, header=0)
    except:
        print(url + '\t找不到表格，开始查找图片')
    else:
        file = re.sub('[^\d]', '', title) + '.xlsx'
        writer = pd.ExcelWriter(file)
        name = re.sub('[^\d]', '', title)
        dfs[0].to_excel(writer, name)
        writer.save()
        print(url + '------Done!')
        return
    
    content = soup.select('.tylm_pagejgjs_text img')
    if len(content) != 0:
        temp = content[0]
        pic = re.findall('src="(.*?)" ', str(temp))
        if len(pic) == 0:
            print(url + '\t图片格式有误')
            return            
        else:
            temp = pic[0].split('.')[-1]
            file = re.sub('[^\d]', '', title) + '.' + temp
            pic = 'http://hrbgjj.org.cn' + pic[0]
            try:
                urllib.request.urlretrieve(pic, file)
                print(url + '\t图片保存成功')
            except:
                print(url + '\t图片保存失败')
              

if __name__ == '__main__':
    

#    url_temp = 'http://hrbgjj.org.cn/lpcx/index_1.jhtml' 
#    html = check(url_temp)
#    names, urls = get_all_urls(html)
        
    url_a = 'http://hrbgjj.org.cn/lpcx/index_'    
    for i in range(1, 6):
        url = url_a + str(i) + '.jhtml'
        html = check(url)
        names, urls = get_all_urls(html)
        for j in urls:
            search_all_urls(j)

    
    