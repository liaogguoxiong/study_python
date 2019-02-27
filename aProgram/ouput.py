#！/usr/bin/env python
#！@Author：lgx
#！@时间：2019-01-17 13:41
#!@Filename:ouput.py
import time

import pytesseract
import selenium.webdriver
from PIL import Image, ImageEnhance

driver=selenium.webdriver.Chrome()
url='http://192.168.20.57:9081/zzs_kpfw_manager/login.htm'
driver.get(url)
save_pic_path="C:/Users/xiao/Desktop/picture/pic1.png"
driver.implicitly_wait(1)
driver.save_screenshot(save_pic_path)
location=driver.find_element_by_id('gencode').location
size=driver.find_element_by_id('gencode').size

time.sleep(3)
driver.close()

left=location['x']
top=location['y']
right=location['x'] + size['width']
bottom=location['y'] + size['height']
left=int(left)
top=int(top)
right=int(right)
bottom=int(bottom)

img=Image.open(save_pic_path).crop((left,top,right,bottom))
img=img.convert('L')
img=ImageEnhance.Contrast(img)
img=img.enhance(2.0)
img.save("C:/Users/xiao/Desktop/picture/pic2.png")

img=Image.open('6.jpg')
code=pytesseract.image_to_string(img)
print(code)
print("over")


