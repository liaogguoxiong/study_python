#时间：    2018/12/20 23:53
#作者：    lgx
#文件名：  静态方法的例子
'''
本程序提供航空公司航机状态,比如到达,晚点,没起飞之类的
'''
class airplaneStatus(object):
    def __init__(self,name):
        self.name=name
        self.__status=None
    def seekStatus(self):
        status=1
        print("根据航空公司的api接口,得到%s飞机的状态为晚点"%self.name)
        return status
    @property
    def status(self):
        airstatus=self.seekStatus()
        if airstatus == 1:
            print("%s晚点了!!!!"%self.name)
        if airplaneS == 0:
            print("%s到达了!!!!" % self.name)
    #给静态方法赋值的话需要定义私有方法,否则出错
    @status.setter
    def status(self,s):
        print("%s的状态为到达"%self.name)
        self.__status=s
    @status.deleter
    def status(self):
        del self.name




airplaneS=airplaneStatus("38hao")
airplaneS.status=0
del airplaneS.status
airplaneS.status