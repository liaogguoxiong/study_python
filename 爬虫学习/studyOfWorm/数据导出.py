#时间：    2019/1/19 17:02
#作者：    lgx
#文件名：  数据导出

'''
登录c48导出开票数据和月度统计
'''
import selenium.webdriver
import time

url='http://192.168.20.57:9081/zzs_kpfw_manager'
driver=selenium.webdriver.Chrome()
driver.get(url)

driver.find_element_by_id('user_account').send_keys("admin")
driver.find_element_by_id('password').send_keys('admin')
code=input("请输入验证码>>:")
driver.find_element_by_id("validCode").send_keys(code)
driver.find_element_by_class_name("button_login").click()
#driver.find_element_by_class_name("l-body l-selected").get_attribute('span').click()
driver.find_element_by_xpath("//*[text()='发票查询']").click()
#driver.find_element_by_name("search_kprq_start").send_keys('2019-01-30 17:15:56')

time.sleep(3)
driver.close()


