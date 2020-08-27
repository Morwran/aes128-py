## Шифрование файлов с помощью симметричного алгоритма AES-128
### Состав:
##### * 	aes_lib.py: Библиотека, содержащая методы шифрования
##### * 	test.py: Тест работы библиотеки
##### * 	crypto.py: запуск утилиты шифрования файлов

### Запуск:
	* 	./crypto.py -arg path_srec

	* 	-arg - аргументы запуска шифрования (-с - зашифровать файл, -d - дешифровать файл)
	* 	path_srec - путь к образу .srec
	* 	Ключ шифрования прописан как глобальная переменная в crypto.py

###	Примеры:
#### Шифрование:
	 	./crypto.py -c /home/kvb/prj/py_prj/crypto/aes/embed_ethe.srec 
#### Дешифровка:
	 	./crypto.py -d /home/kvb/prj/py_prj/crypto/aes/crypted_embed_ethe.srec  	




## File encryption using symmetric AES-128 algorithm
### Composition:
##### * aes_lib.py: Library containing encryption methods
##### * test.py: Test the library
##### * crypto.py: start the file encryption utility

### Run:
* ./crypto.py -arg path_srec

* -arg - encryption startup arguments (-c - encrypt the file, -d - decrypt the file)
* path_srec - path to the .srec image
* The encryption key is registered as a global variable in crypto.py

### Examples:
#### Encryption:
./crypto.py -c /home/kvb/prj/py_prj/crypto/aes/embed_ethe.srec
#### Decryption:
./crypto.py -d /home/kvb/prj/py_prj/crypto/aes/crypted_embed_ethe.srec