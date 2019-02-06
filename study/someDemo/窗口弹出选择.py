#时间：    2019/1/16 0:01
#作者：    lgx
#文件名：  窗口弹出选择
'''
输入文件或者目录的时候,可以弹出窗口
'''
import os
import tkinter.filedialog

# 文件对话框：也可以使用\转义符
default_dir = r"文件路径"

fname = tkinter.filedialog.askopenfilename(title=u'选择文件',
            initialdir=(os.path.expanduser((default_dir))))