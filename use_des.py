# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 15:27:45 2023

@author: Tom
"""

from Crypto.Cipher import DES

key = b'secret_k'  # 生成8字节的密钥
cipher = DES.new(key, DES.MODE_ECB)  # 使用ECB模式构建DES对象

# 加密数据
message = b'This is a secret message'
ciphertext = cipher.encrypt(message)
print(ciphertext)

# 解密数据
plaintext = cipher.decrypt(ciphertext)
print(plaintext)