#时间：    2019/1/8 22:55
#作者：    lgx
#文件名：  企业名片授权

import selenium.webdriver
import time
dir={

    '91440300715256261T':'56261T',
    '91440300797991357U':'91357U',
    '91440300797962599H':'62599H',
    '9144030006387969XE':'7969XE',
    '91440300557171501C':'71501C',
    '914403005571508822':'508822'


}
#输出字典的key和values
for k,v in dir.items():
    driver=selenium.webdriver.Chrome()
    url='https://open.jss.com.cn/authorize?client_id=184607B0132642A3&response_type=code&redirect_uri=http://efp.szhtxx.cn/apiv3/applyToken/companyinfo/callback&appKey=yRB4b7No'
    driver.get(url)
    driver.find_element_by_id('username').click()
    driver.find_element_by_id('username').send_keys(k)
    driver.find_element_by_id('password').click()
    driver.find_element_by_id('password').send_keys(v)
    driver.find_element_by_id('oauthLogin').click()
    time.sleep(1)
    print("%s已经授权成功!!!"%k)
    driver.quit()


