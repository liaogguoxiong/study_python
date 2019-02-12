#！/usr/bin/env python
#！@Author：lgx
#！@时间：2018-11-29 16:46
#!@Filename:study2.py
'''
学习面向对象的继承
'''
class SchoolMember(object):
    members=0
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def tell(self):
        pass
    def enroll(self):
        '''注册'''
        SchoolMember.members +=1
        print('\033[32;1mnew member [%s] is enrolled,now our SchoolMember has [%d] people. \033[0m '%(self.name,SchoolMember.members))
    def __del__(self):
        """析构方法"""
        SchoolMember.members -= 1
        print("\033[31;1mmember [%s] is dead! now our SchoolMember has [%d] people.\033[0m"%(self.name,SchoolMember.members))

class Teacher(SchoolMember):#继承学校类
    def __init__(self,name,age,course,salary):
        super(Teacher,self).__init__(name,age)
        self.course=course
        self.salary=salary
        self.enroll()
    def tell(self):
        msg='''hi,my name is [%s], works for [%s] as a [%s] teacher !'''%(self.name,'Oldboy', self.course)
        print(msg)
    def teaching(self):
        print("Teacher [%s] is teaching [%s] for class [%s]" % (self.name, self.course, 's12'))

class Student(SchoolMember):
    def __init__(self,name,age,grade,sid):
        super(Student,self).__init__(name,age)
        self.grade=grade
        self.sid=sid
        self.enroll()
    def tell(self):
        msg= '''Hi, my name is [%s], I'm studying [%s] in [%s]!''' %(self.name, self.grade,'Oldboy')
        print(msg)

if __name__ == '__main__':
    t1 = Teacher("Alex", 22, 'Python', 20000)
    t2 = Teacher("TengLan", 29, 'Linux', 3000)
    s1 = Student("Qinghua", 24, "Python S12", 1483)
    s2 = Student("SanJiang", 26, "Python S12", 1484)
    t1.teaching()
    t2.teaching()
    t1.tell()

