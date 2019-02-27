#时间：    2018/12/16 23:54
#作者：    lgx
#文件名：  爬虫练习2
import requests
def getHtmlText(url):
    try:
        r=requests.get(url,timeout=10)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        print(r.text[1000:5000])

    except:
        print("无法获取到信息!")
if __name__ == "__main__":
    url="https://www.amazon.cn/dp/B07HJ2SJQV/458-9303107-7736161?_encoding=UTF8&_encoding=UTF8&ref_=pc_cxrd_658390051_recTab_658390051_t_1&pf_rd_m=A1AJ19PSB66TGU&pf_rd_s=merchandised-search-4&pf_rd_r=SASG31314PY96RD9T7C5&pf_rd_r=SASG31314PY96RD9T7C5&pf_rd_t=101&pf_rd_p=f2343f1e-08a9-4fd5-9b55-21aa22c7a812&pf_rd_p=f2343f1e-08a9-4fd5-9b55-21aa22c7a812&pf_rd_i=658390051"
    getHtmlText(url)
