import socket
import time

import imp
config = imp.load_source('config', "..\\config.py")
data_manager = imp.load_source('data_manager', "..\\Storage\\Storage.py")

def create_connect():
	print (config.SERVER, config.PORT)
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((config.SERVER, config.PORT))
	return s

def Sent_to_host(data):
	socket_name = create_connect()
	socket_name.sendall(data)
	socket_name.close()
	dat = data_manager.data_manager()
	dat.sent_Host(data)

def sendToHost(filename, socket_name):
	f = open(filename)
	#print f.readline()
	chuoi = f.readline()
	while chuoi != '':
		socket_name.sendall(chuoi)
		print 
		time.sleep(2)
		chuoi = f.readline()
	f.close()
	socket_name.close()

#s = create_connect('localhost',3129)
Sent_to_host("hello")
#sendToHost("D:\\demo.txt", s)
