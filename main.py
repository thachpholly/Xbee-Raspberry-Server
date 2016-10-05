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
    module_receivefromWebservice = imp.load_source('host', "Receive from Webservice/host.py")
    module_senttoWebservice = imp.load_source('host', "Send to Webservice/sent.py")
    module_Gui = imp.load_source('gui', "Display/Gui.py")
    dat = module_data_manager.data_manager()
    gui = module_Gui.App_Gui(root)
    senttoWebservice = module_senttoWebservice.Client(mechanize, config.WEBSERVICE_IP, config.WEBSERVICE_PORT, config.FORM_INPUT_PATH)

    t = 0
    while 1:
            time.sleep(4)
            senttoWebservice.sent_data('hello ' + str(t))
            t = t + 1
    #thread1 = threading.Thread(target=re_host.rasp_listen, args=('192.168.0.106',config.PORT, dat, gui))
    #thread1.start()


root = tk.Tk()
root.attributes("-fullscreen",True)

thread2 = threading.Thread(target=main_thread, args=(root,))
thread2.start()
root.mainloop()
