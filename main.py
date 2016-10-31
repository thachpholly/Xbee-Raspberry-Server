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



#Xbee_device = serial.serial('/dev/ttyUSB0', 9600)

def main_thread(root):
    # init program
    config = imp.load_source('module.name', "config.py")
    module_data_manager = imp.load_source('data_manager', "Storage/Sensor_data.py")
    module_receivefromWebservice = imp.load_source('host', "Receive from Webservice/Receive.py")
    module_senttoWebservice = imp.load_source('host', "Send to Webservice/sent_v1.py")
    module_Xbee = imp.load_source('xbee', "Receive from Arduino/Xbee.py")
    module_Gui = imp.load_source('gui', "Display/Gui.py")
    #Xbee_device = serial.Serial('/dev/ttyUSB1', 9600, timeout = 1)
    gui = module_Gui.App_Gui(root, config)
    Receive_WebService = module_receivefromWebservice.Rasp_Receive(mechanize, config.WEBSERVICE_IP, config.WEBSERVICE_PORT, config.FORM_SEND_PATH, module_data_manager)
    senttoWebservice = module_senttoWebservice.Client(mechanize, config.WEBSERVICE_IP, config.WEBSERVICE_PORT, config.FORM_INPUT_PATH, module_data_manager)
    #Xbee = module_Xbee.Xbee(Xbee_device, dat)
    Xbee = None

    thread1 = threading.Thread(target=Receive_WebService.rasp_listen, args=(config.STATION_ID, config.STATION_PASS, Xbee))
    thread1.start()
    #Xbee.listen_from_node(senttoWebservice, config.STATION_ID, config.STATION_PASS, config.NODE_TYPE1, gui, root)
    
    #sen.save()
    #sen.get_data()
    #sen = module_data_manager.Sensor_data('(10:12:59,1,12,23,34)',config, config.NODE_TYPE2)
    #sen.save()
    #while 1:
        
    gui.displaynode(root, '(10:12:59,00,12,23,34,45,55)')
    gui.displaynode(root, '(10:12:59,02,12,23,34,45,56)')
    #gui.displaynode(root, '(10:12:59,04,34,23,34,45,56)')
    #gui.displaynode(root, '(10:12:59,07,12,23,34,45,56)')
    gui.update_sensor_1(root, '(10:12:5,2,14,23,24)')
    while 1:
        sen = module_data_manager.Sensor_data('('+str(random.randint(0,23))+':'+str(random.randint(0,50))+':'+str(random.randint(0,50))+',01,'+str(random.randint(0,50))+','+str(random.randint(0,99))+','+str(random.randint(0,50))+','+str(random.randint(0,99))+','+str(random.randint(0,150))+')',config, config.NODE_TYPE1)
        thread3 = threading.Thread(target=senttoWebservice.sent_data, args=(sen, config.NODE_TYPE1))    
        thread3.start()
        gui.displaynode(root, sen.get_data())
        time.sleep(5)


root = tk.Tk()
root.attributes("-fullscreen",True)



thread2 = threading.Thread(target=main_thread, args=(root,))
thread2.start()
root.mainloop()
