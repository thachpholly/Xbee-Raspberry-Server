# define main program

#import serial
import imp
import time
import socket
import threading
import config


config = imp.load_source('module.name', "config.py")
data_manager = imp.load_source('data_manager', "Storage/Storage.py")
re_host = imp.load_source('host', "Receive from Host/host.py")
se_host = imp.load_source('host', "Send to Host/client.py")
Xbee_device = serial.serial('/dev/ttyUSB0', 9600)
dat = data_manager.data_manager()


print config.HOST, config.PORT

thread1 = threading.Thread(target=re_host.rasp_listen, args=('localhost',config.PORT, dat))
thread1.start()


while 1:
	se_host.Sent_to_host("123", dat)
	time.sleep(1)