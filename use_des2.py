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