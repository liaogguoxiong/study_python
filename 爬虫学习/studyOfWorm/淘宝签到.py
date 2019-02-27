#时间：    2019/1/9 21:50
#作者：    lgx
#文件名：  淘宝签到
import time

from selenium import webdriver

url='https://tieba.baidu.com/index.html#'
driver=webdriver.Chrome()
driver.get(url)
time.sleep(3)
driver.find_element_by_class_name("u_login").click()
driver.find_element_by_class_name('tang-pass-footerBarULogin pass-link').click()
driver.quit()