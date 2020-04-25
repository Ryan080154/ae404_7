# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 11:36:18 2020

@author: Home
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import time
chrome = webdriver.Chrome()
chrome.get("https://ecshweb.pchome.com.tw/search/v3.3/?g=apple")
time.sleep(3)

for i in range(2):
    chrome.execute_script('window.scrolllTo(0,document.body.scrollHeight);')
    time.sleep(1)
    
soup = BeautifulSoup(chrome.page_source,"html.parser")

for each_prod in soup.find_all('h5',class_="prod+name"):
    productName = each_prod.text
    print(productName)
chrome.close()