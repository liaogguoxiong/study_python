#！/usr/bin/env python
#！@Author：lgx
#！@时间：2019-01-18 11:49
#!@Filename:clear_pic.py

import numpy as np
from PIL import Image

inputfile="C:/Users/xiao/Desktop/picture/pic2.png"

def clearNoise(data):
    height=data.shape[0]
    width=data.shape[1]
    for i in range(height):
        for j in range(width):
            if i==0 or i== height-1 or j==0 or j== width-1:
                data [i][j]=255
                continue
            if data[i][j]==0:
                num=0
                for da in data[i-1:i+2,j-1:j+2]:
                    if da[0]>0 :
                        num+=1
                    if da[1]>0 :
                        num+=1
                    if da[2]>0 :
                        num+=1
                if num>4:
                    data[i][j]=255

img = Image.open(inputfile)
data=img.getdata()
da=np.array(data,np.int32)
da[da<=170]=0
da[da>170]=255
da=da.reshape((30,80))#图片原始尺寸
clearNoise(da)
clearNoise(da)
clearNoise(da)
img1=Image.fromarray(da)
img1=img1.convert('RGB')
img1.save("C:/Users/xiao/Desktop/picture/pic3.png")
