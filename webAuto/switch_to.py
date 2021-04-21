from selenium import webdriver as wb
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# 切换页面  从百度切换到bilibili官网首页
def switchWindows():
    windods_1 = b.current_window_handle  # 当前浏览器窗口句柄 ： 是bilibili官网页面
    windows = b.window_handles  # 打开过的所有浏览器句柄 :  百度和bilibili官网 网页
    for current_window in windows:
        if current_window != windows:
            b.switch_to.window(current_window)  # 切换到bilibili官网

url_2 = "https://www.baidu.com/"
b = wb.Chrome()  #使用谷歌浏览器
b.get(url_2)      #打开百度页面并获取页面所有信息
b.implicitly_wait(10)
b.maximize_window()

b.find_element_by_id('kw').send_keys('bilibili官网')  #输入bilibili官网
b.find_element_by_id('kw').submit()   #回车
b.find_element_by_xpath('//*[@id="1"]/h3/a[1]').click()  #单击bilibili官网
time.sleep(2)

switchWindows()

time.sleep(2)
b.find_element_by_xpath('//*[@id="nav_searchform"]/input').send_keys('python自动化')
b.find_element_by_xpath('//*[@id="nav_searchform"]/input').submit()
time.sleep(2)

switchWindows()
b.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[1]/div[2]/ul/li[5]/div/div[1]/a').click()

switchWindows()
b.find_element_by_xpath('//*[@id="bilibiliPlayer"]/div[1]/div[1]/div[11]/div[2]/div[2]/div[1]/div[1]/button/span').click()

time.sleep(2)