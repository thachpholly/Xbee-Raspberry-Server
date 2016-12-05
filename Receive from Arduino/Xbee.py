#! /usr/bin/python


##data_manager = imp.load_source('data_manager', "./Storage/Storage.py")
##storage = data_manager.data_manager()

"""
Xbee.py
By Nhut Tan Nguyen Dang, 2010

Demonstrates reading the low-order address bits from an XBee Series 1
device over a serial port (USB) in API-mode.
"""
class Xbee(XBee):
    """docstring for Xbee"""
        
    def __init__(self, ser, dat, config):
        super(Xbee, self).__init__(ser)
        self.flag=True
        self.dat = dat
        self.config = config


    def wait_read_Packet(self, start_byte):
        """
        wait_read_Packet: None -> binary data

        wait_read_Packet will read from the serial port until a valid
        API frame arrives. It will then return the binary data
        contained within the frame.

        If this method is called as a separate thread
        and self.thread_continue is set to False, the thread will
        exit by raising a ThreadQuitException.
        """
        frame = APIFrame(escaped=self._escaped)
        frame.fill(start_byte)
        while True:
                if self._callback and not self._thread_continue:
                    raise ThreadQuitException
                if self.serial.inWaiting() == 0:
                    time.sleep(.01)
                    continue

                byte = self.serial.read()

                # Save all following bytes, if they are not empty
                if len(byte) == 1:
                    frame.fill(byte)

                while(frame.remaining_bytes() > 0):
                    byte = self.serial.read()

                    if len(byte) == 1:
                        frame.fill(byte)

                try:
                    # Try to parse and return result
                    frame.parse()

                    # Ignore empty frames
                    if len(frame.data) == 0:
                        frame = APIFrame()
                        continue

                    return frame
                except ValueError:
                    # Bad frame, so restart
                    frame = APIFrame(escaped=self._escaped)
                    
    def readPacket(self):
        """
        readPacket: None -> frame info dictionary

        readPacket calls Xbee.readPacket() and waits until a
        valid frame appears on the serial port. Once it receives a frame,
        wait_read_frame attempts to parse the data contained within it
        and returns the resulting dictionary
        """
        while self.flag==True:
            self.flag=False
            while True:
                byte = ser.read()
                #print byte  #debug
                if byte == APIFrame.START_BYTE:
                    frame = self.wait_read_Packet(byte)
                    self.flag=True
                    return self._split_response(frame.data)['rf_data']

    def listen_from_node(self, send_webservice, STATION_ID, STATION_PASS, nodetype, gui, root):
        while self.flag==True:
                self.flag==False
                while True:
                        self.flag==False
                        data = self.readPacket()
                        if data != '':
                                print 'Received from node: ' , data #for debugging
                                gui.displaynode(root, data)
                                sen = self.dat.Sensor_data(data, self.config, self.config.NODE_TYPE1)
                                thread1 = threading.Thread(target=send_webservice.sent_data, args=(sen, STATION_ID, STATION_PASS))
                                thread1.start()
                                #send_webservice.sent_data(data, nodetype)
                        self.flag = True
                self.flag = True
                break
        
    def send_command(self, addr, command):
        while self.flag==True:
            self.flag=False
            countValue=0
            while True:
                if countValue==3:
                    #write file
                    #storage.sent_arduino("Fail" + " " + charIdControl + data)
                    print "Write error"
                    self.flag = True
                    return
                
                self.send('tx', dest_addr=addr, data=command)
                
                self.flag=True
                confirm = self.readPacket()
                self.flag=False
                if confirm == '0':
                    print "Success"
                    #storage.sent_arduino("Ok" + " " + charIdControl + data)
                    self.flag = True
                    break
                countValue += 1
            self.flag=True
            break
    
##PORT = '/dev/ttyUSB0'
##BAUD_RATE = 9600
##ser = serial.Serial(PORT, BAUD_RATE, timeout=1)
##
###-------send
##data = "000:1"
##addr = "\x12\x34"
##xb = Xbee(ser)
##while True:
##    print xb.readPacket()

##def main():
##   
##    ##while True:
##    ##    print xb.readPacket()
##    thread1 = threading.Thread(target=xb.readPacket, args=())
##    thread1.start()
##
##thread2 = threading.Thread(target=main, args=())
##thread2.start()

"""xb = Xbee(ser)
xb.send_command(addr, data)"""
