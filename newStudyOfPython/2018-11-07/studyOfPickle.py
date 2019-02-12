#！/usr/bin/env python
#！@Author：lgx
#！@时间：2018-11-07 10:12
#!@Filename:studyOfPickle.py

#学习用于可序列化的二个模块的pickle模块
"""
pickle，用于python特有的类型 和 python的数据类型间进行转换
pickle模块提供了四个功能：dumps、dump、loads、load
"""
import pickle
data ={ "p1":123,"p2":"hello"}
p_str=pickle.dumps(data)#pickle.dumps将数据通过特殊的形式转为只有python语言认识的字符串
print(p_str)
# with open('D:/result.pk','w') as fp:
#     pickle.dump(data,fp)
f=open("D:/test.txt","w",encoding="utf-8")
f.write(p_str.decode("utf-8"))
f.close()

