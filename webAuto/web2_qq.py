from selenium import webdriver as wb
import time
from selenium.webdriver.common.by import By

urls = 'https://www.baidu.com/'
# b = wb.Edge(r'D:\software\python3.9.4\msedgedriver.exe')
b = wb.Chrome()
b.get(urls)   #打开Edge浏览器

b.maximize_window()    #窗口最大化
time.sleep(2)

#在输入框中输入qq邮箱
b.find_element_by_xpath('//*[@id="kw"]').send_keys('qq邮箱')
time.sleep(2)
#单击百度一下
b.find_element_by_xpath('//*[@id="su"]').click()
time.sleep(2)
#单击qq邮箱官网
b.find_element_by_xpath('//*[@id="1"]/h3/a[1]').click()
time.sleep(2)

#切换页面
windods_1 = b.current_window_handle
print(windods_1)

windows  = b.window_handles
print(windows)

for current_window in windows:
    # if current_window != windods_1:
    b.switch_to.window(current_window)

#切换为qq登录
# b.find_element_by_id('qqLoginTab')
# time.sleep(2)

#切换iframe
b.switch_to.frame(b.find_element_by_id("login_frame"))
time.sleep(1)

#输入qq号
# b.find_elements_by_id('u').clear()     # 定位到账号输入处并清空账号
b.find_element_by_xpath('//*[@id="u"]').send_keys('2952900732')
time.sleep(1)

#输入密码
# b.find_elements_by_id('p').clear()     # 定位到密码输入处并清空密码
b.find_element_by_xpath('//*[@id="p"]').send_keys('@1234abc')
time.sleep(1)

#单击登录按钮
b.find_element_by_xpath('//*[@id="login_button"]').click()
time.sleep(10)

#离开 login_frame
b.switch_to.parent_frame()
b.switch_to.default_content()
time.sleep(1)


