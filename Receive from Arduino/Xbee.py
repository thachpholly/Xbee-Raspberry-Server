<<<<<<< HEAD
#import imp
import threading
#import serial
#data_manager = imp.load_source('data_manager', "../Storage/Storage.py")
#storage = data_manager.data_manager()
=======
import imp
import time
import serial
data_manager = imp.load_source('data_manager', "../Storage/Storage.py")
storage = data_manager.data_manager()
>>>>>>> origin/master

class Xbee:
        """docstring for Xbee"""
        
<<<<<<< HEAD
        def __init__(self, ser, storage):
                self.ser = ser
                self.storage = storage
        def send_data(self, data, charIdControl):
                data += '#'
                #countValue = 0
                while True:
                        # send 10 times if arduino is not respond
                        #if countValue == 1:
                                #write file
                                #self.storage.sent_arduino("Fail" + " " + charIdControl + data)
                                #return False
                        
                        for i in charIdControl:
                                self.ser.write(i)
                        for i in data:
                                self.ser.write(i)
                        print 'Sent to node: ' + data #for debugging
                        self.storage.sent_arduino("Ok" + " " + charIdControl + data)
                        return True    
                        

        def listen_from_node(self, send_webservice, STATION_ID, STATION_PASS, nodetype, gui, root):
                while 1:
                        data = ''
                        data = self.receive_data(data)
                        if data != '#':
                                print 'Received from node: ' , data #for debugging
                                gui.displaynode(root, data)
                                thread1 = threading.Thread(target=send_webservice.sent_data, args=(data, nodetype))
                                thread1.start()
                                #send_webservice.sent_data(data, nodetype)
                                
        def receive_data(self, data):
                #print 'd'
                data = ''
                if str(self.ser.read()) == str('('):
                        
=======
        def __init__(self, ser):
                self.ser = ser
                
        def send_data(self, data, charIdControl):
                countValue = 0
                while True:
                        # send 10 times if arduino is not respond
<<<<<<< HEAD
                        if countValue == 3:
=======
                        if countValue == 10:
>>>>>>> origin/master
                                #write file
                                storage.sent_arduino("Fail" + " " + charIdControl + data)
                                return False
                        
                        for i in charIdControl:
                                self.ser.write(i)
                                
                        print charIdControl #for debugging
                        time.sleep(2)
                                
                        if str(self.ser.read()) == str('O'):
                                for i in data:
                                        self.ser.write(i)
                                print data #for debugging
                                storage.sent_arduino("Ok" + " " + charIdControl + data)
                                return True
                        countValue += 1

        def receive_data(self, data):
                if str(self.ser.read()) == str('('):
>>>>>>> origin/master
                        charReceive = ' '
                        while str(charReceive) != str(')'):
                                charReceive = self.ser.read()
                                if str(charReceive) != str(')'):
                                        data += charReceive
<<<<<<< HEAD
                        #print 'Received from node--: ' , data #for debugging
                        #write file
                        data = '(' + data + ')'
                        self.storage.receive_arduino(data)
                        
                        return data
                return '#'
=======
                        #write file
                        storage.receive_arduino(data)
                        return data
>>>>>>> origin/master

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

