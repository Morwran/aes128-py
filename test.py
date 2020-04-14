#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from aes_lib import AES
import time, os

key="0123456789abcdef"

word="!text for crypt!"

if __name__ == '__main__':

	crypto = AES(key)

	byte_array=[ord(byte) for byte in word]

	crypto_str=crypto.encrypt(byte_array)

	print"src word: ",word
	print"symb word: ",[hex(h) for h in byte_array]
	print"encrypt: ",[hex(h) for h in crypto_str]

	decrypto_str=crypto.decrypt(crypto_str)

	print"decrypt: ",[hex(h) for h in decrypto_str]

	print "finish"