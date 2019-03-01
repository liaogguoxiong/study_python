#时间：    2018/12/14 22:29
#作者：    lgx
#文件名：  面向对象实例
'''
定义4个类,学校类,学校成员类
老师类,学生类.老师学生类继承与
学校成员类
'''
class School(object):
    def __init__(self,name,addr):
        self.name=name
        self.addr=addr
        self.students=[]
        self.staffs=[]

    def enroll(self,stu_obj):
        print("学生%s在%s注册"%(stu_obj.name,self.name))
        self.students.append(stu_obj)
    def hire(self,tea_obj):
        print("%s雇佣了%s老师"%(self.name,tea_obj.name))
        self.staffs.append(tea_obj)
class SchoolMember(object):
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def tell(self):
        pass

class Teacher(SchoolMember):
    def __init__(self,name,age,sex,salary,course):
        super(Teacher,self).__init__(name,age,sex)
        self.salary=salary
        self.course=course
    def tell(self):
        print("""
        the information of teacher:%s
        name:%s
        age:%d
        sex:%s
        salary:%f
        course:%s
    """%(self.name,self.name,self.age,self.sex,self.salary,self.course))
    def teach(self):
        print("%s老师教%s"%(self.name,self.course))

class Student(SchoolMember):
    def __init__(self,name,age,sex,stu_id,stu_grade):
        super(Student,self).__init__(name,age,sex)
        self.stu_id=stu_id
        self.stu_grade=stu_grade
    def tell(self):
        print("""
        the information of student:%s
        name:%s
        age:%d
        sex:%s
        stu_id:%d
        stu_grade:%s
    """ % (self.name,self.name, self.age, self.sex, self.stu_id, self.stu_grade))
    def payTuition(self,amount):
        print("%s交了%s学费"%(self.name,amount))
school1=School("国雄学校","大门度")
t1=Teacher('lgx',22,"男",8000,"python")
t2=Teacher('zsy',21,"女",10000.0,"linux")
s1=Student("dakuxiong",18,"男",1400360117,14003601)
# t1.tell()
# s1.tell()
school1.enroll(s1)
school1.hire(t2)
school1.staffs[0].teach()
school1.students[0].payTuition(5000)