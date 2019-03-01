#！/usr/bin/env python
#！@Author：lgx
#！@时间：2018-11-22 14:43
#!@Filename:studyOfHashlib.py

import hashlib
'''
用于加密相关的操作，代替了md5模块和sha模块，主要提供 SHA1, SHA224, SHA256, SHA384, SHA512 ，MD5 算法
'''
# ######## md5 ########
hash=hashlib.md5()
hash.update('admin'.encode())
print(hash.hexdigest())

# ######## sha1 ########
hash=hashlib.sha1()
hash.update('admin'.encode())
print(hash.hexdigest)

# ######## sha256 ########
hash=hashlib.sha256()
hash.update('admin'.encode())
print(hash.hexdigest)

# ######## sha384 ########

hash = hashlib.sha384()
hash.update('admin'.encode())
print(hash.hexdigest())


# ######## sha512 ########

hash = hashlib.sha512()
hash.update('admin'.encode())
print(hash.hexdigest())

'''
以上加密算法虽然依然非常厉害，但时候存在缺陷，即：通过撞库可以反解。
所以，有必要对加密算法中添加自定义key再来做加密。
'''
print('==============================')
hash=hashlib.md5('898oaFs09f'.encode())
hash.update('admin'.encode())
print(hash.hexdigest)

'''
还不够吊？python 还有一个 hmac 模块，
它内部对我们创建 key 和 内容 再进行处理然后再加密
'''

import hmac
h=hmac.new('liaoguoxiong'.encode())
h.update('hello'.encode())
print(h.hexdigest())
