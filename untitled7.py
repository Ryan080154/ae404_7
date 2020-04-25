# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 11:09:39 2020

@author: Home
"""

import requests
pageNumber=1

while pageNumber <6:
    res = requests.get("https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=cat&page={}&sort=sale/dc".format(pageNumber))
    pageNumber+=1
    res = res.json()['prods']
    for eachProduct in res:
        productName = eachProduct['name']
        productPrice = eachProduct['price']
        print(productName,productPrice)