# define main program

#import serial
import imp
import time
import socket
import threading
import config
import mechanize
import Tkinter as tk



#Xbee_device = serial.serial('/dev/ttyUSB0', 9600)

def main_thread(root):
    # init program
    config = imp.load_source('module.name', "config.py")
    module_data_manager = imp.load_source('data_manager', "Storage/Storage.py")
    module_receivefromWebservice = imp.load_source('host', "Receive from Webservice/Receive.py")
    module_senttoWebservice = imp.load_source('host', "Send to Webservice/sent.py")
    module_Gui = imp.load_source('gui', "Display/Gui.py")
    dat = module_data_manager.data_manager()
    gui = module_Gui.App_Gui(root, config)
    Receive_WebService = module_receivefromWebservice.Rasp_Receive(mechanize, config.WEBSERVICE_IP, config.WEBSERVICE_PORT, config.FORM_SEND_PATH, dat)
    senttoWebservice = module_senttoWebservice.Client(mechanize, config.WEBSERVICE_IP, config.WEBSERVICE_PORT, config.FORM_INPUT_PATH, dat)


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

root = tk.Tk()
root.attributes("-fullscreen",True)



thread2 = threading.Thread(target=main_thread, args=(root,))
thread2.start()
root.mainloop()
