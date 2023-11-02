# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 15:50:32 2023

@author: Tom
"""
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad,unpad

def encrypt(data, key):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_data = pad(data, DES.block_size, style='pkcs7')
    return cipher.encrypt(padded_data)

def decrypt(ciphertext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_data = cipher.decrypt(ciphertext)
    return unpad(padded_data, DES.block_size, style='pkcs7')

data = b'This is a secret message'
key = b'secret_k'
ciphertext = encrypt(data, key)
print("ciphered:", ciphertext)
plaintext = decrypt(ciphertext, key)
print("deciphered:", plaintext)

# 1. PKCS7
# PKCS7是一种广泛使用的填充模式，它会在数据的末尾添加字节，这些字节的值等于需要填充的字节数。例如，如果数据长度为8字节，但加密算法要求是16字节的倍数，那么需要添加8个字节的填充，每个字节的值为8。解密时，只需要读取数据的最后一个字节，就能知道需要去除多少个字节的填充。

# 2. Zero Padding
# Zero Padding是一种简单的填充模式，它会在数据的末尾添加一定数量的零字节。解密时，只需要读取数据的最后一个字节，就能知道需要去除多少个字节的填充。

# 3. ANSI X.923
# ANSI X.923是一种填充模式，它会在数据的末尾添加一定数量的零字节，并在最后一个字节的前面添加一个字节，该字节的值为需要填充的字节数。

# 4. ISO 10126
# ISO 10126是一种填充模式，它会在数据的末尾添加一定数量的随机字节，并在最后一个字节的前面添加一个字节，该字节的值为需要填充的字节数。
# -----------------------------------
# ©著作权归作者所有：来自51CTO博客作者mob649e815c3b9e的原创作品，请联系作者获取转载授权，否则将追究法律责任
# python中加密填充模式没有 PAD_PKCS7
# https://blog.51cto.com/u_16175466/7057306