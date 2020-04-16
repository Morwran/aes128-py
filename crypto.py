#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from aes_lib import AES
import time, os, sys

key="0123456789abcdef"

def read_imf(image_path):
	if(os.path.isfile(image_path)):
		try:
			with open(image_path, 'rb') as f:
				data = f.read() 
			return data	
		except IOError as e:
			print(u'не удалось открыть файл образа')
			print e
			return -1
	else:
		return -1		

def write_imf(out_path,crypted_data):
	#if(os.path.isfile(out_path)):
		try:
			#i=0
			with open(out_path, 'wb') as ff:
				for byte in crypted_data:
					#print"{} wr: {}".format(i,chr(byte))
					#i+=1
					#ff.write(bytes(crypted_data))	
					ff.write(chr(byte))
			return 1	
		except IOError as e:
			print(u'не удалось открыть файл для записи')
			print e
			return -1
	#else:
	#	return -1			

def write_stdout_now(s):
	sys.stdout.write(s)
	sys.stdout.flush()	


def crypto_file(image_path,crypto,decrypt=False):

	#with open(image_path, 'rb') as f:
	#	data = f.read() 

	data = 	read_imf(image_path)

	if data>0:
		
		if decrypt == False:
			out_path_prefix = 'crypted_'
		else:	
			out_path_prefix = 'decrypted_'

		crypted_data = []
		temp = []

		cntb=0

		print"len data",len(data)

		#byte = imf.read(1)

		#while byte:
		for byte in data:
			temp.append(ord(byte))
			cntb+=1
			if len(temp) == 16:
				if decrypt==False:
					crypted_part = crypto.encrypt(temp)
				else:
					crypted_part = crypto.decrypt(temp)

				crypted_data.extend(crypted_part)
				del temp[:]	

				
				if not (cntb%100):
					write_stdout_now('.')	

		else:
			
			if 0 < len(temp) < 16:
				empty_spaces = 16 - len(temp)
				for i in range(empty_spaces - 1):
					temp.append(0)
					cntb+=1
				temp.append(1)
				cntb+=1
				if decrypt==False:
					crypted_part = crypto.encrypt(temp)
				else:
					crypted_part = crypto.decrypt(temp)

				crypted_data.extend(crypted_part)

		print""

		out_path = os.path.join(os.path.dirname(image_path) , out_path_prefix + os.path.basename(image_path))
		#print"len data ",len(crypted_data) 
		# Ounput data
		#with open(out_path, 'wb') as ff:
		#	ff.write(bytes(crypted_data))	

		write_imf(out_path,crypted_data)

		return 	out_path, cntb

	else:
		return -1, -1		


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
					out_path, cntb = crypto_file(img_path,crypto)
					if cntb>0:
						print "Finish! Total time: {} s. Total size {} B".format((time.time()-t1),cntb)
						print "New file here: ",out_path

				if arg=='-d':
					print "decryption process..."	
					t1=time.time()
					out_path, cntb = crypto_file(img_path,crypto,decrypt=True)
					if cntb>0:
						print "Finish! Total time: {} s. Total size {} B".format((time.time()-t1),cntb)
						print "New file here: ",out_path
			else:
				print"Error: invalid arg: ",arg		

		else:
			print "Error: Image path incorrect"	

	else:
		print "Error: invalid args"		