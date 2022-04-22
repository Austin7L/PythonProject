from tracemalloc import stop
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
import time
import sys
import os
import xml.etree.ElementTree as ET



# 文件路徑
# print(__file__)

# 絕對路徑
script_file = os.path.realpath(__file__)
# print(script_file)

# 獲取目錄
dirname = os.path.dirname(script_file)
# print(dirname)
dirname = os.path.join(dirname, 'UserInfo.xml')
# print(dirname)


# 從檔案載入並解析 XML 資料
tree = ET.parse(dirname)
root = tree.getroot()
print(root.tag)

# 從字串中取得並解析 XML 資料
# root = ET.fromstring('UserInfo')
child = root.iter('properties')
print('1',child)

userid = ""
pwd = ""
for child in root.iter('properties'):
    if child.get('account')!=None:
        userid = child.get('account')
    elif child.get('password')!=None:
        pwd = child.get('password')
print(userid)
print(pwd)


browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("http://eip.deanshoes.com/ess")  # 前往EIP網站
 
# browser.implicitly_wait(30)
time.sleep(5)

search_input = browser.find_element_by_id("username")  # 查詢文字框
search_input.send_keys(userid)  # 輸入文字
search_input = browser.find_element_by_id("password")  # 查詢文字框
search_input.send_keys(pwd)  # 輸入文字
time.sleep(3)
dc =browser.find_element_by_xpath('//*[@id="fm1"]/input[4]') #F12找到按鈕後，右鍵>Copy>Copy XPath
ActionChains(browser).click(dc).perform()
time.sleep(5)  # 強制等待20秒


# while 1:
#     #Python 3.8 已移除 clock() 方法 可以使用 time.perf_counter() 或 time.process_time() 方法替代。
#     start = time.process_time()
#     try:
#         companydc = browser.find_element_by_xpath('//*[@id="app"]/div/main/div/div/section/div[2]/div[2]/div[1]/div[2]/div/div[1]/div[3]/div/button')
#         print('Finded element')
#         end=time.process_time()
#     except:
#         print('still searching the element')
# print('spend searching time: ',str(end-start))
# companydc = browser.find_element_by_xpath('//*[@id="app"]/div/main/div/div/section/div[2]/div[2]/div[1]/div[2]/div/div[1]/div[3]/div/button')
# companydc = browser.find_element_by_xpath('//*[@id="yui_patched_v3_11_0_1_1636099801193_520"]')
# ActionChains(browser).click(companydc).perform()
# /html/body/div/div/main/div/div/section/div[2]/div[2]/div[1]/div[2]/div/div[1]/div[3]/div/button
companydc = browser.find_element_by_xpath('//*[@id="breadcrumbs"]/ul/li[1]/a')
ActionChains(browser).click(companydc).perform()

time.sleep(30)  # 強制等待20秒