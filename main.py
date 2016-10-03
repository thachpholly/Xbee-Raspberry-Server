# define main program

#import serial
import imp
import time
import socket
import threading
import config


config = imp.load_source('module.name', "config.py")
data_manager = imp.load_source('data_manager', "Storage/Storage.py")
re_host = imp.load_source('host', "Receive from Webservice/host.py")
se_host = imp.load_source('host', "Send to Webservice/client.py")
Gui = imp.load_source('gui', "Display/Gui.py")
#Xbee_device = serial.serial('/dev/ttyUSB0', 9600)
dat = data_manager.data_manager()
gui = Gui.Gui()
#time.sleep(3)

print 'aa',config.HOST, config.PORT

thread1 = threading.Thread(target=re_host.rasp_listen, args=('192.168.0.106',config.PORT, dat, gui))
thread1.start()

t = 10
while 1:
	se_host.Sent_to_host(str(t), dat)
	time.sleep(10)
	#gui.change_Tem(str(t))
	t = t + 1