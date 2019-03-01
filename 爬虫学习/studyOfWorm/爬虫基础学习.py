#时间：    2018/12/16 19:14
#作者：    lgx
#文件名：  爬虫基础学习

import requests
# url="https://www.baidu.com"
# #response对象包含了爬虫返回的内容
# response=requests.get(url)
"""
或者可以这样写,requests.request(),
其余的六个方法都是在request方法之上编写的
"""
#请求的状态码,如果为200则成功,否则失败
# print(response.status_code)
# #请求应答的头部信息
# #print(response.headers)
# ##从http header中猜测的响应内容编码方式
# #如果header中不存在charset,则认为编码是
# #ISO-8859-1
# print(response.encoding)
# #从内容分析出响应内容的编码方式(备选编码方式)比较准
# print(response.apparent_encoding)
# response.encoding="utf-8"
# #http响应内容的二进制模式
# #print(response.content)
# #http响应内容的字符串形式,即url对应的页面内容
# print(response.text)

"""
爬取网页的通用代码框架
def getHtmlText(url):
    try:
        r=requests.get(url,timeout=30)
        #获取请求状态码,如果不为200.,则异常
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return "异常"
if __name__ == "__main__":
    url="https://www.baidu.com"
    print(getHtmlText(url))
"""
def getHtmlText(url):
    try:
        r=requests.get(url,timeout=5)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return "异常"

if __name__ == "__main__":
        url="https://www.baidu"
        print(getHtmlText(url))