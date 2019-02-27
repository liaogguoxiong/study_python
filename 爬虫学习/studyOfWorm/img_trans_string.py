#时间：    2019/1/17 23:33
#作者：    lgx
#文件名：  img_trans_string
from PIL import Image,ImageEnhance
import pytesseract
import urllib
img_path="D:\\Users\\lgx\\Desktop\\code_imge\\screenImg.jpg"
img=Image.open(img_path)#.crop((left,top,right,bottom))
img=img.convert('L')
img=ImageEnhance.Contrast(img)
img=img.enhance(2.0)
img.save(img_path)

img=Image.open(img_path)
code=pytesseract.image_to_string(img)
print(code.strip())