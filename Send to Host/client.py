import socket
import time

def create_connect(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))
	return s


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

s = create_connect('localhost',3129)

sendToHost("D:\\demo.txt", s)
