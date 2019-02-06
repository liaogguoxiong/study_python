#时间：    2018/12/16 20:25
#作者：    lgx
#文件名：  爬虫之油站授权
"""
通过税号和税号后六位的密码登录授权,
实现6个税号自动授权
"""
import requests

def getHtmlText(url):
    try:
        ky={"user-agent":"Mozilla/5.0"}
        account={"username":"91440300715256261T",
                 "password":"56261T"}
        r=requests.get(url,headers=ky)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return "异常"
if __name__ == "__main__":
    url="https://open.jss.com.cn/authorize?client_id=184607B0132642A3&response_type=code&redirect_uri=http://efp.szhtxx.cn/apiv3/applyToken/companyinfo/callback&appKey=yRB4b7No"
    print(getHtmlText(url))