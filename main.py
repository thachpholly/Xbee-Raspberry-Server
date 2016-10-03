# define main program

#import serial
import imp
import time
import socket
import threading
import config
import mechanize

config = imp.load_source('module.name', "config.py")
module_data_manager = imp.load_source('data_manager', "Storage/Storage.py")
module_receivefromWebservice = imp.load_source('host', "Receive from Webservice/host.py")
module_senttoWebservice = imp.load_source('host', "Send to Webservice/sent.py")
module_Gui = imp.load_source('gui', "Display/Gui.py")

#Xbee_device = serial.serial('/dev/ttyUSB0', 9600)

dat = module_data_manager.data_manager()
gui = module_Gui.Gui()
senttoWebservice = module_senttoWebservice.Client(mechanize, config.WEBSERVICE_IP, config.WEBSERVICE_PORT, config.FORM_INPUT_PATH)

#thread1 = threading.Thread(target=re_host.rasp_listen, args=('192.168.0.106',config.PORT, dat, gui))
#thread1.start()
t  = 1
while 1:
	time.sleep(3)
	gui.change_soil_moisture(str(t))
	gui.change_soil_temperature(str(t))
	gui.change_air_humidity(str(t))
	gui.change_Tem(str(t))
	gui.change_Ligth(str(t))
	t = t + 1
