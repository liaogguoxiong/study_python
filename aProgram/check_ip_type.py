#！/usr/bin/env python
#！@Author：lgx
#！@时间：2019-01-16 14:15
#!@Filename:check_ip_type.py
'''
根据输入的ip来判断是否合法,已经写入文件中
'''


def check_ip_type(ip):
    '''判断输入的ip是否符合IP规则'''
    ip_seg = ip.split('.')  # 用.来分割ip地址
    if len(ip_seg) != 4:
        return 1
    else:
        for i in ip_seg:
            if i.isdigit() == True:
                if int(i) <= 255 and int(i) >= 0:
                    continue
                else:
                    return 2
                    break
            else:
                return 3
                break

        return 4


def add_con(fpwd, con):
    """把输入IP地址类型正确的加入配置文件中"""
    with open(fpwd, 'a') as f:
        f.write(con)
        f.write("\n")

def cheak_result(ip):
    """由于要判断多个ip的话,重复代码太多,
       所以写了这个方法"""
    res = check_ip_type(ip)
    # 获取check_ip_type()方法的返回值
    res = str(res)
    # print(res)
    # ip地址正确的情况
    if res == "4":
        print(err_list[res])
        # 添加ip地址
        add_con(fPwd, ip)
        print("成功添加ip到%s" % fPwd)
    # ip不对的情况
    else:
        print(err_list[res])



if __name__ == "__main__":
    err_list={"1":"IP字段不为4位",
              "2":"错误的ip地址,大于255或者小于0" ,
              "3":"错误的ip地址,包含字母或者特殊符号",
              "4":"合法的ip地址"
              }
    netmask = "255.255.255.0"
    fPwd = "C:\\Users\\xiao\\Desktop\\1.txt"
    # default_dir="文件路径"
    # fname=tkinter.filedialog.askopenfilename(title=u"选择文件",initialdir=(os.path.expanduser((default_dir))))
    print("====配置IP模式======")
    ip = input("请输入IP地址>>:".strip())
    cheak_result(ip)
    gway=input("请输入网关IP>>:".strip())
    cheak_result(gway)



