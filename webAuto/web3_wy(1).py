# -*- coding: utf-8 -*-
from selenium import webdriver as wb
import time

from selenium.webdriver.support.wait import WebDriverWait

urls = 'https://www.baidu.com/'
b = ""
#region  打开浏览器
def openBrowser(url):
    global  b        #声明一个全局变量
    b = wb.Chrome()  #使用谷歌浏览器
    b.get(urls)      #打开百度页面并获取页面所有信息
    b.maximize_window()    #窗口最大化
    b.implicitly_wait(10)  #隐式等待
#endregion

#region  登录163邮箱
def login163():
    #在输入框中输入qq邮箱
    b.find_element_by_xpath('//*[@id="kw"]').send_keys('网易邮箱')
    #单击百度一下
    b.find_element_by_xpath('//*[@id="su"]').click()
    #单击qq邮箱官网
    b.find_element_by_xpath('//*[@id="1"]/h3/a[1]').click()

    #切换页面  从百度切换到网易邮箱
    windods_1 = b.current_window_handle   #当前浏览器窗口句柄 ： 是网易邮箱页面
    print(windods_1)
    windows  = b.window_handles           #打开过的所有浏览器句柄 :  百度和网易邮箱 网页
    print(windows)
    for current_window in windows:
        if current_window != windows:
            b.switch_to.window(current_window)      #切换到网易邮箱页面

    #切换iframe
    b.switch_to.frame(b.find_element_by_css_selector("div.loginUrs>iframe"))

    account_input = b.find_element_by_css_selector('.j-inputtext.dlemail')
    passed_input = b.find_element_by_css_selector('.j-inputtext.dlpwd')
    account_input.click()

    #输入163邮箱号
    account_input.send_keys('siyu_cheng10309')

    #输入密码
    passed_input.send_keys('@1234abc')

    #单击登录按钮
    b.find_element_by_xpath('//*[@id="dologin"]').click()

    #离开 login_frame
    b.switch_to.parent_frame()
    b.switch_to.default_content()
#endregion

#region 进入邮箱并发送邮件
def enter163andSendemail():
    #单击写信按钮
    b.find_element_by_xpath('//*[@id="_mail_component_134_134"]/span[2]').click()
    time.sleep(2)
    #输入收件人  1016508075@qq.com
    sjr = b.find_element_by_xpath('//input[@class="nui-editableAddr-ipt"]')
    sjr.send_keys('2952900732@qq.com')
    #输入主题
    zt = b.find_element_by_xpath('//div[@class="bz0"]/div/input[@class="nui-ipt-input"]')
    zt.send_keys('python test')
    #利用xpath获取frame 再switch_to
    frame = b.find_element_by_xpath("//iframe[@class='APP-editor-iframe']")
    b.switch_to.frame(frame)
    time.sleep(2)
    # 输入正文内容
    bd = b.find_element_by_xpath('//body[@class="nui-scroll"]')

    #从文件中读取 写入到邮件正文中
    f = open(r'D:\csy\webauto\111.txt','r',encoding='utf-8')
    fj = f.read()
    f.close()
    bd.send_keys(fj)

    # 返回主页面后，需要等待一下，否则可能定位不到元素
    b.switch_to.default_content()
    time.sleep(2)
    # 随便选择一个发送按钮，点击发送
    fs = b.find_elements_by_xpath(
        '//span[@class="nui-btn-text"]/parent::div[contains(@class,"nui-btn-hasIcon nui-mainBtn-hasIcon")]')
    print('fs len is ', len(fs))
    # fs[0].click()  # 发送
    fs[1].click()  # 发送
    print('发送成功')
    WebDriverWait(5)
    b.quit()

#endregion

if __name__ == '__main__':
    openBrowser(urls)
    login163()
    enter163andSendemail()