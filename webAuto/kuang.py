from selenium import webdriver as wb
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time

urls = 'http://www.asjdkl.xyz:81/'
b = wb.Chrome()  #使用谷歌浏览器
b.get(urls)      #打开百度页面并获取页面所有信息


# region 下拉框  定位方式
# s = b.find_element_by_xpath('/html/body/select')   #通过元素定位
# print('定位下拉框')

# d1 = ActionChains(b)
# d1.click(s).perform()
# print('左击下拉框')
# time.sleep(1)

# a1 = Select(s).select_by_visible_text('上海')  #取消对应文本选项
# a1 = Select(s).select_by_index(3)  #通过索引定位
# a1 =Select(s).select_by_value('opel') #通过value值定位
# time.sleep(2)
# a1 =Select(s).all_selected_options()  #返回所有的选项
# a1 =Select(s).deselect_all()   #取消所有选项
# a1 =Select(s).deselect_by_index()  #取消

#鼠标选中下拉框中的某一项
# s = b.find_element_by_xpath('/html/body/select')   #通过元素定位
# print('定位下拉框')
# d1 = ActionChains(b)
# d1.click(s).perform()
# print('左击下拉框')
# time.sleep(1)
# a1 = Select(s).select_by_visible_text('上海')
# d1 = ActionChains(b)
# d1.double_click(a1).perform()
# print('选中某一个选项')
# time.sleep(1)
# s.click() #收回下拉框
# time.sleep(5)
# b.close()
# print('关闭浏览器')

#鼠标移动  与上面效果一样
# s = b.find_element_by_xpath('/html/body/select')
# s.click()
# time.sleep(2)
# ActionChains(b).move_to_element(s).perform()
# time.sleep(2)
# e2 = Select(s).select_by_index(2)
# ActionChains(b).double_click(e2).perform()
# s.click()
# time.sleep(5)
# b.close()
# print('关闭浏览器')


# Select(s).first_selected_option()  #返回第一个选项
# d1.click(s)
# print('选中其中一个选项')
# time.sleep(2)



#endregion