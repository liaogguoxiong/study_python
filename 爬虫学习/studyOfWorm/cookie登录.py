#时间：    2019/1/17 20:55
#作者：    lgx
#文件名：  cookie登录

import requests
import selenium.webdriver
import time
from PIL import Image,ImageEnhance
import pytesseract
import urllib


url="http://192.168.20.57:9081/zzs_kpfw_manager/index.htm"
driver=selenium.webdriver.Chrome()
driver.get(url)
# driver.find_element_by_id('user_account').click()
# driver.find_element_by_id('user_account').send_keys('admin')
# driver.find_element_by_id('password').click()
# driver.find_element_by_id('password').send_keys('admin')
img_path="D:\\Users\\lgx\\Desktop\\code_imge\\screenImg.png"
img_src=driver.find_element_by_id('gencode').get_attribute('src')
print(img_src)
urllib.request.urlretrieve(url,filename=img_path)

# respone=requests.get(url)
# print(respone.status_code)
# # print(respone.text)
# print(respone.headers)

# driver.maximize_window()
# driver.save_screenshot(img_path)
# img_location=driver.find_element_by_id("gencode").location
# size=driver.find_element_by_id("gencode").size
# left=img_location['x']
# top=img_location['y']
# right=img_location['x']+size['width']
# bottom=img_location['y']+size['height']
# print(img_location,size,left,top,right,bottom)

img=Image.open(img_path)#.crop((left,top,right,bottom))
img=img.convert('L')
img=ImageEnhance.Contrast(img)
img=img.enhance(2.0)
img.save(img_path)

img=Image.open(img_path)
code=pytesseract.image_to_string(img)
print(code.strip())

time.sleep(3)
driver.close()