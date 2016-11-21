# define main program

#import serial
import imp
import time
import socket
import threading
import config
import mechanize
import random
import Tkinter as tk
import json

def main_thread(root):
    # init program
    config = imp.load_source('module.name', "config.py")
    module_data_manager = imp.load_source('data_manager', "Storage/Sensor_data.py")
    module_receivefromWebservice = imp.load_source('host', "Receive from Webservice/Receive_v1.py")
    module_senttoWebservice = imp.load_source('host', "Send to Webservice/sent_v1.py")
    #module_Xbee = imp.load_source('xbee', "Receive from Arduino/Xbee.py")
    module_Gui = imp.load_source('gui', "Display/Gui.py")
    #Xbee_device = serial.Serial('/dev/ttyUSB0', 9600, timeout = 1)
    #Xbee = module_Xbee.Xbee(Xbee_device, module_data_manager, config)
    Xbee = None
    gui = module_Gui.App_Gui(root, config, Xbee)
    Receive_WebService = module_receivefromWebservice.Rasp_Receive(mechanize, config.WEBSERVICE_IP, config.WEBSERVICE_PORT, config.FORM_SEND_PATH, module_data_manager)
    senttoWebservice = module_senttoWebservice.Client(config)
    

    #thread1 = threading.Thread(target=Receive_WebService.rasp_listen, args=(config.STATION_ID, config.STATION_PASS, Xbee, config))
    #thread1.start()
    
    #Xbee.listen_from_node(senttoWebservice, config.STATION_ID, config.STATION_PASS, config.NODE_TYPE1, gui, root)
    #config.save_config(t, json)
    ##time.sleep(3)
    #print config.ligth_intensity_w
    #sen.save()
    #sen.get_data()
    #sen = module_data_manager.Sensor_data('(10:12:59,1,12,23,34)',config, config.NODE_TYPE2)
    #sen.save()
   # while 1:
        #time.sleep(2)

    
    gui.displaynode(root, '(10:12:59,00,12,23,34,45,55)')
    gui.displaynode(root, '(10:12:59,01,11,22,33,44,55)')
    #gui.displaynode(root, '(10:12:59,02,11,22,33,44,55)')
    
    
    #gui.update_sensor_1(root, '(10:12:59,04,33,45,56)')
    #time.sleep(3)
    #gui.update_sensor_1(root, '(10:12:59,04,35,22,57)')
    #gui.displaynode(root, '(10:12:59,07,12,23,34,45,56)')
    #gui.update_sensor_1(root, '(10:12:5,2,14,23,24)')
    while 1:
        #print '2'
        sen = module_data_manager.Sensor_data('('+str(random.randint(0,23))+':'+str(random.randint(0,50))+':'+str(random.randint(0,50))+',01,'+str(random.randint(0,50))+','+str(random.randint(0,99))+','+str(random.randint(0,50))+','+str(random.randint(0,99))+','+str(random.randint(0,150))+')',config, config.NODE_TYPE1)
        #thread3 = threading.Thread(target=senttoWebservice.sent_data, args=(sen, config.NODE_TYPE1))    
       # thread3.start()
        #print '1'
        gui.displaynode(root, sen.get_data())
        print gui.get()
        #gui.make_message('123', root, 2)
        time.sleep(5)


root = tk.Tk()
root.attributes("-fullscreen",True)



thread2 = threading.Thread(target=main_thread, args=(root,))
thread2.start()
root.mainloop()
