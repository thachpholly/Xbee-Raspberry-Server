# define main program

import serial
import imp
import time
import socket
import threading
import config
import mechanize
import random
import Tkinter as tk



#Xbee_device = serial.serial('/dev/ttyUSB0', 9600)

def main_thread(root):
    # init program
    config = imp.load_source('module.name', "config.py")
    module_data_manager = imp.load_source('data_manager', "Storage/Storage.py")
    module_receivefromWebservice = imp.load_source('host', "Receive from Webservice/Receive.py")
<<<<<<< HEAD
    module_senttoWebservice = imp.load_source('host', "Send to Webservice/sent_v1.py")
    module_Xbee = imp.load_source('xbee', "Receive from Arduino/Xbee.py")
=======
    module_senttoWebservice = imp.load_source('host', "Send to Webservice/sent.py")
>>>>>>> origin/master
    module_Gui = imp.load_source('gui', "Display/Gui.py")
    Xbee_device = serial.Serial('/dev/ttyUSB1', 9600, timeout = 1)
    dat = module_data_manager.data_manager()
    gui = module_Gui.App_Gui(root, config)
    Receive_WebService = module_receivefromWebservice.Rasp_Receive(mechanize, config.WEBSERVICE_IP, config.WEBSERVICE_PORT, config.FORM_SEND_PATH, dat)
    senttoWebservice = module_senttoWebservice.Client(mechanize, config.WEBSERVICE_IP, config.WEBSERVICE_PORT, config.FORM_INPUT_PATH, dat)
<<<<<<< HEAD
    Xbee = module_Xbee.Xbee(Xbee_device, dat)
    #Xbee = None

    thread1 = threading.Thread(target=Receive_WebService.rasp_listen, args=(config.STATION_ID, config.STATION_PASS, Xbee))
    thread1.start()
    Xbee.listen_from_node(senttoWebservice, config.STATION_ID, config.STATION_PASS, config.NODE_TYPE1, gui, root)
    #while 1:
        
        #gui.displaynode(root, '(10:12:59,00,12,23,34,45,56)')
        #gui.displaynode(root, '(10:12:59,02,12,23,34,45,56)')
        #gui.displaynode(root, '(10:12:59,04,12,23,34,45,56)')
        #gui.displaynode(root, '(10:12:59,07,12,23,34,45,56)')
        #senttoWebservice.sent_data('(10:12:59,1,12,23,34,45,'+str(random.randint(0,50))+')', config.NODE_TYPE1)
        #time.sleep(3)

=======


    thread1 = threading.Thread(target=Receive_WebService.rasp_listen, args=(config.STATION_ID, config.STATION_PASS))
    thread1.start()
    #time.sleep(1)
    
    t = 0
    while 1:
            
            #senttoWebservice.sent_data('(10:21:59, 11, 34, 45, 56, 78, 89)', config.NODE_TYPE1 , config.STATION_ID, config.STATION_PASS)
            gui.displaynode(root, '(10:21:59,'+ str(t) +',34,45,56,78,89)')
            time.sleep(1)
            #gui.displaynode( root, '(15:21:59, 00, 334, 478, 536, 78, 895)')
            #gui.update_Wind(root, '(10:21:59, 00, 34, 45, 56)')
            t = t + 1
            if t == 9:
            	break
    gui.displaynode(root, '(10:21:58,'+ str(2) +',344,32,566,8,89)')
    gui.displaynode(root, '(10:21:55,'+ str(7) +',344,32,566,8,89)')
    gui.displaynode(root, '(10:21:54,'+ str(0) +',344,32,566,8,89)')
>>>>>>> origin/master

root = tk.Tk()
root.attributes("-fullscreen",True)



thread2 = threading.Thread(target=main_thread, args=(root,))
thread2.start()
root.mainloop()
