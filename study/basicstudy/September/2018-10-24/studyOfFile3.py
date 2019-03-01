#今天还是来学习文件
'''
#模式为读写模式,可以边读边写,但是写入的内容只能够追加在后面，
从硬盘的存储来理解，前面的磁盘空间已经被用了，如果插入前面的磁盘空间，
则前面的内容需要往后移，不太现实，所以插入的内容只能够在后面
f=open("study","r+",encoding="utf-8")
print(f.readline())
print(f.readline())
print(f.readline())
f.write("测试下能够进行边读边写\n".strip())
print(f.readline())
f.write("hello,i do a test of r+")

#写读模式，没什么用处
f=open("study","w+",encoding="utf-8")
print(f.tell())
print(f.readline())#之所以没有读出来是因为新创建了一个文件,光标为0
f.write("郑诗雨是个大粑粑\n")#写入一个文件就相当于创建一个文件，之前的内容会被覆盖
f.write("郑诗雨是个大粑粑\n")
f.write("郑诗雨是个大粑粑\n")
f.write("郑诗雨是个大粑粑\n")
f.write("郑诗雨是个大粑粑\n")
print(f.tell())
f.seek(9)
print(f.readline())
f.write("===我想当第二行===")

#追加读模式,之前追加模式(a模式)不支持读，现在此模式支持
f=open("study","a+",encoding="utf-8")



#二进制读模式,不需要encoding参数了
f=open("study","rb")#二进制模式，字符转二进制需要编码encode
print(f.readline())
print(f.readline())
print(f.readline())

#二进制写模式
f=open("study",'wb')
f.write("boombommmm".encode())#输入的字符，需要转化为二进制才可写入,文件就变成了二进制文件
f.write("boombommmm".encode())
f.write("boombommmm".encode())
f.write("boombommmm".encode())
f.write("boombommmm".encode())

f=open("study2","r",encoding="utf-8")
f_new=open("study_new","w",encoding="utf-8")
for line in f:
    if "詹姆斯·马蒂斯" in line:
        line=line.replace("詹姆斯·马蒂斯","国雄粑粑")
    f_new.write(line)



f.close()
'''
#为了避免打开文件后忘记关闭，可以通过管理上下文
#即 with open('filename','model',encoding="utf-8") as f
with open('study_new','r',encoding="utf-8") as f:
    for line in f:
        print(line)
#同时打开多个文件
with open("study_new",'r',encoding="utf-8") as f,\
    open("study",'r',encoding='utf-8') as f2:
    pass
    

