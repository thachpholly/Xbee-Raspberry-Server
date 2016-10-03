import socket
import time
#from sendToAirduino import send_command
#import imp
#config = imp.load_source('module.name', "../config.py")
#data_manager = imp.load_source('data_manager', "../Storage/Storage.py")
import thread
import threading

def valid_command(command):
	command = command.strip()
	#to do something

def secsion(conn, adrr):
	result = ''
	while 1:
		data = conn.recv(1024)
		if not data: break
		result += data
		#print "recieved: " , data, '.'
	conn.close()
	return result

def hh(s):
	for x in xrange(1,10):
		print x, s
def rasp_listen(HOST, PORT, da_ma, gui):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((HOST, PORT))
	s.listen(1)
	while 1:
		conn, adrr = s.accept()
		data = secsion(conn, adrr)
		print 'recieved: ', data
		gui.change_Tem(data[0:len(data)-1])
		#da_ma = data_manager.data_manager()
		#da_ma.receive_Host('OK' + data)
	
#thread1 = threading.Thread(target=rasp_listen, args=(config.HOST,config.PORT,))
#thread1.start()

#print 'completed', config.HOST, config.PORT
#rasp_listen(config.HOST, config.PORT)