#!/usr/bin/python

# define main program
import sys
import serial
import imp
import time
import serial
import threading
import time
import socket
import threading
import config
import mechanize
import random
import Tkinter as tk
import json
from xbee import ZigBee
from xbee.frame import APIFrame


def main_thread(root):
    # init program
    module_data_manager = imp.load_source('data_manager', "Storage/Sensor_data.py")
    module_receivefromWebservice = imp.load_source('host', "Receive from Webservice/Receive_v1.py")
    module_senttoWebservice = imp.load_source('host', "Send to Webservice/sent_v1.py")
    module_Xbee = imp.load_source('xbee', "Receive from Arduino/Zigbee.py")
    module_Gui = imp.load_source('gui', "Display/Gui.py")
    Xbee_device = serial.Serial(config.xbee_drive, 9600, timeout = 1)
    Xbee = module_Xbee.Zigbee(Xbee_device, module_data_manager, config)
    #Xbee = None
    gui = module_Gui.App_Gui(root, config, Xbee)
    Receive_WebService = module_receivefromWebservice.Rasp_Receive(config, config.WEBSERVICE_IP, config.WEBSERVICE_PORT, config.FORM_SEND_PATH, module_data_manager)
    senttoWebservice = module_senttoWebservice.Client(config)
    print 'init complete'
    thread3 = threading.Thread(target= Xbee.listen_from_node, args=(senttoWebservice, None, None, gui, root))
    thread3.start()
    thread1 = threading.Thread(target= Receive_WebService.rasp_listen, args=(None, None, Xbee, config, gui))
    thread1.start()

    print 'init complete'


root = tk.Tk()
root.attributes("-fullscreen",True)

thread2 = threading.Thread(target=main_thread, args=(root,))
thread2.start()
root.mainloop()
