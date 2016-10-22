import imp
import time
import serial
data_manager = imp.load_source('data_manager', "../Storage/Storage.py")
storage = data_manager.data_manager()

class Xbee:
        """docstring for Xbee"""
        
        def __init__(self, ser):
                self.ser = ser
                
        def send_data(self, data, charIdControl):
                countValue = 0
                while True:
                        # send 10 times if arduino is not respond
                        if countValue == 3:
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
                        charReceive = ' '
                        while str(charReceive) != str(')'):
                                charReceive = self.ser.read()
                                if str(charReceive) != str(')'):
                                        data += charReceive
                        #write file
                        storage.receive_arduino(data)
                        return data

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

