#！/usr/bin/env python
#！@Author：lgx
#！@时间：2019-01-18 13:53
#!@Filename:抓取验证码素材.py

import selenium.webdriver
import time
from PIL import Image,ImageEnhance
import pytesseract
for i in range(1):
    driver=selenium.webdriver.Chrome()
    url='http://192.168.20.57:9081/zzs_kpfw_manager/login.htm'
    driver.get(url)
    save_pic_path="C:/Users/xiao/Desktop/picture/pic.png"
    driver.implicitly_wait(1)
    driver.save_screenshot(save_pic_path)
    location=driver.find_element_by_id('gencode').location
    size=driver.find_element_by_id('gencode').size

    time.sleep(1)
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
    img.save("C:/Users/xiao/Desktop/picture/pic1.png")
    print("获得%d张验证码素材"%i)