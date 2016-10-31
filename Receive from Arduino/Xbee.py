import time
import imp
import threading
#import serial
#data_manager = imp.load_source('data_manager', "./Storage/Storage.py")
#storage = data_manager.data_manager()

class Xbee:
        """docstring for Xbee"""
        
        def __init__(self, ser, storage, config):
                self.ser = ser
                self.storage = storage
                self.flag=True
                self.config = config

        def send_data(self, data, charIdControl):
                while self.flag==True:
                        print self.flag
                        self.flag = False
                        data += "#"
                        countValue = 0
                        while True:
                                # send 10 times if arduino is not respond
                                confirm = ""
                                if countValue == 10:
                                        #write file
                                        #self.storage.sent_arduino("Fail" + " " + charIdControl + data)
                                        self.flag = True
                                        return
                                
                                for i in charIdControl:
                                        self.ser.write(i)    
                                print charIdControl #for debugging

                                for j in data:
                                        self.ser.write(j)
                                print data #for debugging
                                
                                
                                confirm = self.ser.read()
                                if confirm == 'O':
                                        print "Success---------"
                                        #self.storage.sent_arduino("Ok" + " " + charIdControl + data)
                                        self.flag = True
                                        return True
                                countValue += 1
                        self.flag = True
                        break

        def listen_from_node(self, send_webservice, STATION_ID, STATION_PASS, nodetype, gui, root):
                while self.flag==True:
                        self.flag==False
                        while 1:
                                self.flag==False
                                data = ''
                                data = self.receive_data(data)
                                if data != '#':
                                        print 'Received from node: ' , data #for debugging
                                        gui.displaynode(root, data)
                                        sen = self.storage.Sensor_data(data, self.config, self.config.NODE_TYPE1)
                                        thread1 = threading.Thread(target=send_webservice.sent_data, args=(sen, self.config.NODE_TYPE1))
                                        thread1.start()
                                        #send_webservice.sent_data(data, nodetype)
                                self.flag = True
                        self.flag = True
                        break
                                
        def receive_data(self, data):
                while self.flag==True:
                        self.flag==False
                        #print 'd'
                        data = ''
                        if str(self.ser.read()) == str('('):
                                
                                charReceive = ' '
                                while str(charReceive) != str(')'):
                                        charReceive = self.ser.read()
                                        if str(charReceive) != str(')'):
                                                data += charReceive
                                #print 'Received from node--: ' , data #for debugging
                                #write file
                                data = '(' + data + ')'
                                #self.storage.receive_arduino(data)
                                self.flag==True
                                return data
                        self.flag==True
                        return '#'
                        

"""PORT = '/dev/ttyUSB0'
BAUD_RATE = 9600
ser = serial.Serial(PORT, BAUD_RATE, timeout = 3)

-------send
data = "Successly#"
charIdControl = "40F1ED40#"
xbObj = Xbee(ser)
xbObj.send_data(data, charIdControl)

----receive
recedata = ""
xbObj = Xbee(ser)
while True:
        xbObj.receive_data(recedata)"""

