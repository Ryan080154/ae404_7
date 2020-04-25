from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
chorm_options =Options()
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