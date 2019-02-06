#时间：    2018/12/3 23:38
#作者：    lgx
#文件名：  csPlayGame

'''

面向对象的三大特性:封装,,继承,多态

现在说的是封装

'''
#文字版的CS游戏

'''
    定义一个类,角色类,玩家输入名字,
    选择职业,武器,固定的血量和金钱

'''
weapondict={
                'ak47':'5000',
                'b51':'5000',
                'dg':"6000",
                'm71':"500"
}
class Role():

    # 类变量,共有的,如果和实例变量名称相同,先调用实例变量,没有则调用类变量
    name="hello"

    def __init__(self,name,role,weapon,money=15000,lifeValue=100):#初始化方法
        self.name=name
        self.role=role
        self.weapon=weapon
        # 私有属性,只有在类的内部能够访问,外部不可以访问或者修改
        self.__money=money
        self.__lifeValue=lifeValue

    '''
    使用一个方法来展示外部无法访问的私有属性
    '''
    def show_status(self):
        print('''================人物状态====================      
                 ======name=========>>%s
                 ======role=========>>%s
                 ======weapon=======>>%s
                 ======money========>>%d
                 ======lifeValue====>>%d
              '''%(self.name,self.role,self.weapon,self.__money,self.__lifeValue))

    '''
    其实私有方法和私有属性都是一样的,都是在方法或者
    属性前面加__即可成为私有属性或者方法,只能够在类
    的内部中使用,外部无法使用,需要在类的内部暴露一个
    包含它们的方法来供他们使用
    '''
    def __buy_gun(self):
        if self.weapon in weapondict:
            self.__money -=int(weapondict[self.weapon])
        print("%s买了%s,剩余%d."%(self.name,self.weapon,self.__money))

    '''
    #析构函数:在实例释放、销毁的时候自动执行,通常
    用做一些收尾工作,如关闭数据库连接,打开关闭临时文件
    '''
    # def __del__(self):
    #     print("变量不存在了")


r1=Role("lgx",'police','ak47')
r1.buy_gun()
# del r1      #销毁r1
# print(r1)
r1.show_status()


