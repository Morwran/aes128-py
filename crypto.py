#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from aes_lib import AES
import time, os, sys

key="0123456789abcdef"

def open_im(image_path):
	if(os.path.isfile(image_path)):
		try:
			im = open(image_path, "rb")
			return im
		except IOError as e:
			print(u'не удалось открыть файл образа')
			print e
			return -1

def write_stdout_now(s):
	sys.stdout.write(s)
	sys.stdout.flush()	


def encrypt_file(image_path,crypto):

	with open(image_path, 'rb') as f:
		data = f.read() 	

	if data>0:
		
		crypted_data = []
		temp = []

		cntb=0

		#byte = imf.read(1)

		#while byte:
		for byte in data:
			temp.append(ord(byte))
			if len(temp) == 16:
				
				crypted_part = crypto.encrypt(temp)
				crypted_data.extend(crypted_part)
				del temp[:]	

				cntb+=1
				if not (cntb%100):
					write_stdout_now('.')	

		else:
			
			if 0 < len(temp) < 16:
				empty_spaces = 16 - len(temp)
				for i in range(empty_spaces - 1):
					temp.append(0)
				temp.append(1)
				crypted_part = crypto.encrypt(temp)
				crypted_data.extend(crypted_part)

		print""

		out_path = os.path.join(os.path.dirname(image_path) , 'crypted_' + os.path.basename(image_path))

		# Ounput data
		with open(out_path, 'wb') as ff:
			ff.write(bytes(crypted_data))		


if __name__ == '__main__':
	if len (sys.argv) > 2:
		img_path=str(sys.argv[2])
		if(os.path.isfile(img_path)):
			print img_path
			arg = str(sys.argv[1])
				
			if arg=='-c' or arg=='-d':
				crypto = AES(key)
				if arg=='-c':
					print "encryption process..."
					t1=time.time()
					encrypt_file(img_path,crypto)
					print "Finish! Total time: {} s.".format((time.time()-t1))

				if arg=='-d':
					print "decryption process..."	
					
			else:
				print"Error: invalid arg: ",arg		

		else:
			print "Error: Image path incorrect"	

	else:
		print "Error: invalid args"		