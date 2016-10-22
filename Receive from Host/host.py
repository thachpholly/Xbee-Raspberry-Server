import socket
import time
#from sendToAirduino import send_command
import imp
config = imp.load_source('module.name', "..\\config.py")
import thread
import threading

def valid_command(command):
	command = command.strip()
	#to do something

def secsion(conn, adrr):
	#print thread.getName()
	
	#print 'connected: ' , adrr
	result = ''
	while 1:
		data = conn.recv(1024)
		if not data: break
		#if not data: break
		#data.strip()
		result += data
		#print "recieved: " , data, '.'
	conn.close()
	#print 'disconnected: ' , adrr
	return result

def hh(s):
	for x in xrange(1,10):
		print x, s
def rasp_listen(HOST, PORT):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((HOST, PORT))
	s.listen(1)
	try:
		while 1:
			conn, adrr = s.accept()
			#print adrr.adr
			print 'recieved: ', secsion(conn, adrr)
	except KeyboardInterrupt, e:
		print e

#print 'hello', config.HOST, config.PORT
thread1 = threading.Thread(target=rasp_listen, args=(config.HOST,config.PORT,))
thread1.start()

print 'completed', config.HOST, config.PORT
#rasp_listen(config.HOST, config.PORT)
