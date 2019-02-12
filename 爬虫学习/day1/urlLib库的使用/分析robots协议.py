#！/usr/bin/env python
#！@Author：lgx
#！@时间：2019-01-28 11:43
#!@Filename:分析robots协议.py

'''
利用urllib的robotsparser模块,我们
可以实现网站的robots分析
robots协议也称爬虫协议,机器人协议
它的全名叫网络爬虫排除标准,用来告诉你
那些可以爬,那些不可以爬,它通常叫做robots.txt
的文件文件,一般放在网站的根目录

我们可以使用robotparser模块来解析robots.txt
该模块提供了一个类,RobotFileParser,它可以根据某
网站的robots.txt文件来判断爬虫是否有权限来爬取
这个网页.
RobotFileParser类的常用方法
set_url():用来设置robots.txt文件的链接,如果在实例化
RobotFileParser类的时候传入了,那么就不用这个方法设置了

read():读取robots.txt文件并进行分析,该方法执行一个读取和分析操作,
如果不调用这个方法,接下来的判断都会为False,所以一定要调用这个方法,
这个方法不会返回任何内容,但是执行了读操作

parse():用来解析robots.txt文件,传入的参数是robots.txt某些行的内容
,它会按照robots.txt的语法规则来分析这些内容

can_fetch():该方法传入二个参数,第一个是User-agent,第二个是要抓取的url,返回的
内容是该搜索引擎是否可以抓取该url,返回True或者False

mtime():返回的是上次抓取和分析robots.txt的时间,如果需要定期检查来抓取最新的robots.txt会用到

modified():它同样是对长时间分析和抓取的搜索引擎的爬虫很有帮助,将当前
时间设置为上次抓取和分析robots.txt的时间
'''

from urllib.robotparser import RobotFileParser
#实例化RobotFileParser类
rp=RobotFileParser()
rp.set_url('http://www.jianshu.com/robots.txt')
rp.read()
print(rp.can_fetch('*','https://www.jianshu.com/apps?utm_medium=desktop&utm_source=navbar-apps'))
print(rp.can_fetch('*','https://www.jianshu.com/'))
print(rp.mtime())