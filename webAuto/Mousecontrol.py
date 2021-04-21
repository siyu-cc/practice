# 1、单击鼠标左键
# click(on_element=None)
# 2、点击鼠标左键，不松开
# click_and_hold(on_element=None)
# 3、点击鼠标右键
# context_click(on_element=None)
# 4、双击鼠标左键
# double_click(on_element=None)
# 5、拖拽到某个元素然后松开
# drag_and_drop(source, target)
# 6、拖拽到某个坐标然后松开
# drag_and_drop_by_offset(source, xoffset, yoffset)
# 7、按下某个键盘上的键
# key_down(value, element=None)
# 8、松开某个键
# key_up(value, element=None)
# 9、鼠标从当前位置移动到某个坐标
# move_by_offset(xoffset, yoffset)
# 10、鼠标移动到某个元素
# move_to_element(to_element)
# 11、移动到距某个元素（左上角坐标）多少距离的位置
# move_to_element_with_offset(to_element, xoffset, yoffset)
# 12、在某个元素位置松开鼠标左键
# release(on_element=None)
# 13、发送某个键到当前焦点的元素
# send_keys(*keys_to_send)
# 14、发送某个键到指定元素
# send_keys_to_element(element, *keys_to_send)


#  ======特殊======
#  执行链中的所有动作
#   perform()

# -*- coding:utf-8 -*-
from selenium import webdriver as wb
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import UnexpectedAlertPresentException

urls = 'https://translate.google.cn/'  #谷歌翻译 网址
# b = wb.Chrome()  #使用谷歌浏览器
# b.get(urls)      #打开百度页面并获取页面所有信息

# b.implicitly_wait(10)
#在左边输入框中输入  hello
# b.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/span/span/div/textarea').send_keys('hello')

#单击右边框中的
# a1 = b.find_element_by_xpath('//*[@id="i13"]/span[3]')  #
# a2 = b.find_element_by_xpath('//*[@id="i12"]/span[3]')
# time.sleep(2)
# ActionChains(b).context_click(a1).perform()  #鼠标右击
# time.sleep(2)
# ActionChains(b).click(a1).perform()    #鼠标单击
#
# ActionChains(b).click_and_hold(a2).perform()  #鼠标左击，不松开
# ActionChains(b).double_click(a2).perform()    #鼠标左击
# time.sleep(5)


url_2 = "https://mail.qq.com/"
b = wb.Chrome()  #使用谷歌浏览器
b.get(url_2)      #打开百度页面并获取页面所有信息
b.implicitly_wait(10)
b.maximize_window()

#找到iframe
find_frame = b.find_element_by_id('login_frame')
#切入到表单
b.switch_to.frame(find_frame)

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
time.sleep(2)

#拖拽
# p1 = b.find_element_by_id('draggable')
# p2 = b.find_element_by_id('droppable')
# ActionChains(b).drag_and_drop(p1,p2)

#拖动某个坐标
d = b.find_element_by_id('tcaptcha_drag_button')

d1 = ActionChains(b)
d1.click_and_hold(d).perform()

try:
    d1.drag_and_drop_by_offset(d,500,0).perform()
except UnexpectedAlertPresentException:
    print('移动失败')

time.sleep(2)

# 7、按下某个键盘上的键
#离开表单
b.switch_to.default_content()
time.sleep(5)
b.quit()



