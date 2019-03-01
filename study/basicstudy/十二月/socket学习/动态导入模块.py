#时间：    2019/1/4 21:26
#作者：    lgx
#文件名：  动态导入模块
import importlib
#参数写的是路径,路径的书写方法为:所属目录.导入模块
aa=importlib.import_module("socket练习.aa")
print(aa.C().name)