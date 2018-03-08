# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 17:43:40 2018

@author: Se
"""

import time
import requests
import json
from selenium import webdriver
import pickle
 
if __name__ == '__main__':
    
    # 打开chorme
    bolgurl = 'https://www.51lkh.com/game/'
    browser = webdriver.Chrome()
    browser.get(bolgurl)
    
    name = browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div/input')
    name.send_keys('15244608508')
    
    password = browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/input')
    password.send_keys('liu875288')
    
    
    time.sleep(10)

    button = browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/button/div/div')
    button.click()
    
    time.sleep(6)
    button = browser.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/button/div/div')
    button.click()
    
    time.sleep(10)
    cookies = browser.get_cookies()
    pickle.dump( cookies , open("cookies.pkl","wb"))







url = 'https://www.51lkh.com/game/'
r = requests.get(url, cookies=cookies)
print(r.status_code)


request = requests.Session()


for cookie in cookies:
    request.cookies.set(cookie['name'], cookie['value'])

# 加载cookies后登录网站
wbdata = request.get("https://www.51lkh.com/game/").text

data = json.loads(wbdata)


cookie = {
"at":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMTYzMTQ0MCIsImlzcyI6ImNvaW5jb2xhLmNvbSIsImV4cCI6MTUxNzkwODc5MiwiaWF0IjoxNTE3MzAzOTkyLCJkZXZpY2UiOiJXRUIiLCJqdGkiOiI2ZTEwZGVlZi00MTIxLTRhNDUtYTE5OS1kMzk2ZTU1NTc4MjkifQ.AUdtEOq1oIiH7UzY-j3SxFm-mVTgTBcrdkYHrVqXo7w",          
"name":"liurole",          
"hpp":"true",     
"ccy":"OSC",       
"ctc":"ETH_BTC"
}
 
url = 'https://www.51lkh.com/game/fox/19756'
wbdata = requests.get(url,cookies=cookie).text

 
data = json.loads(wbdata)
news = data['data']['pc_feed_focus']
 
for n in news:    
  title = n['title']    
  img_url = n['image_url']    
  url = n['media_url']    
  print(url,title,img_url)
  
  
  
  

# coding:utf-8
import requests
from bs4 import BeautifulSoup
 

 
header = {    
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',    
'Connection': 'keep-alive',       
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',  
'Cookie': cookie}
 
url = 'https://kankandou.com/book/view/22353.html'
wbdata = requests.get(url,headers=header).text
soup = BeautifulSoup(wbdata,'lxml')
print(soup)