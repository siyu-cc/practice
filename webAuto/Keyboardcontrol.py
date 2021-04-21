# 1、删除按钮
#   Keys.BACK_SPACE
# 2、空格按钮
#  Keys.SPACE
# 3、回车enter键
#  Keys.ENTER
# 4、全选（Ctrl+A）、复制（Ctrl+C）、剪切（Ctrl+X）、粘贴（Ctrl+V）
#  Keys.CONTROL,'a' 'c' 'x' 'v'
# 5、Tab键
#  Keys.TAB
# 6、回退键(Esc)
#  Keys.ESCAPE
# 7、F1···F12
#  Keys.F1····Keys.F12

# -*- coding:utf-8 -*-
from selenium import webdriver as wb
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

urls = 'https://www.baidu.com/'
b = wb.Chrome()  #使用谷歌浏览器
b.get(urls)      #打开百度页面并获取页面所有信息

b.find_element_by_id("kw").send_keys('2952900732@qq.com') #在输入框输入内容
b.maximize_window()
time.sleep(2)
b.find_element(By.ID,'kw').send_keys(Keys.BACK_SPACE*4)  #删除后面四个字符
time.sleep(2)
b.find_element_by_id('kw').send_keys(Keys.SPACE*3)  #输入3个空格
time.sleep(2)
b.find_element_by_id('kw').send_keys('python Auottest')
time.sleep(2)
b.find_element(By.ID,'kw').send_keys(Keys.ENTER) #回车
# b.find_element(By.ID,'kw').submit()   #回车
time.sleep(2)
b.find_element_by_id('kw').send_keys(Keys.CONTROL,'a') #ctrl+a  全选
b.find_element_by_id('kw').send_keys(Keys.CONTROL,'x') #ctrl+x  剪切
time.sleep(2)
b.find_element_by_id('kw').send_keys(Keys.CONTROL,'v')  #ctrl+v  粘贴
b.find_element_by_id('kw').submit()   #回车




