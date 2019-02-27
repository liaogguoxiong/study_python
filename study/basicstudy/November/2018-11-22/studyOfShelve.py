#时间：    2018/11/22 22:56
#作者：    lgx
#文件名：  studyOfShelve

import shelve

'''
shelve模块是一种持久化技术,
'''
d=shelve.open('testOfShelve')#持久化技术
'''
shelve的写操作
'''
# _list=[1,2,3,4,5,6,7]
# _dir={'name':'lgx','age':22,'sex':"man"}
# d['list']=_list#其中['list']为key,_list为值
# d['dir']=_dir
# d['date']=datetime.datetime.now()
# d.close()

'''
shelve的读操作
'''
print(d.get('list'))
print(d.get('dir')['name'])
print(d.get('date'))