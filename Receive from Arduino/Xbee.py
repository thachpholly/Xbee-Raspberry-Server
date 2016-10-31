#import imp
import threading
#import serial
#data_manager = imp.load_source('data_manager', "../Storage/Storage.py")
#storage = data_manager.data_manager()

class Xbee:
        """docstring for Xbee"""
        
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
                        #self.storage.sent_arduino("Ok" + " " + charIdControl + data)
                        return True    
                        

        def listen_from_node(self, send_webservice, STATION_ID, STATION_PASS, nodetype, gui, root):
                while 1:
                        data = ''
                        data = self.receive_data(data)
                        if data != '#':
                                print 'Received from node: ' , data #for debugging
                                gui.displaynode(root, data)
                                #thread1 = threading.Thread(target=send_webservice.sent_data, args=(data, nodetype))
                                #thread1.start()
                                #send_webservice.sent_data(data, nodetype)
                                
        def receive_data(self, data):
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
                        
                        return data
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

