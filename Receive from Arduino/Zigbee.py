#! /usr/bin/python
from xbee import ZigBee
from xbee.frame import APIFrame
import time
import serial
import threading
import sys
##data_manager = imp.load_source('data_manager', "./Storage/Storage.py")
##storage = data_manager.data_manager()

#define for zigbee
get_success='\x00'
get_sensor_data = '0'
get_command_data = '1'
time_to_wait = 4
#map_address={"2":"\x00\x13\xA2\x00\x40\xF1\xED\x40", "1":"\x00\x13\xA2\x00\x40\xF1\xED\x0E"}

"""
Xbee.py
By Nhut Tan Nguyen Dang, 2010

Demonstrates reading the low-order address bits from an XBee Series 1
device over a serial port (USB) in API-mode.
"""
class Zigbee(ZigBee):
    """docstring for Xbee"""
        
    def __init__(self, ser, dat, config):
        super(Zigbee, self).__init__(ser)
        self.dat = dat
        self.config = config
        self.lock = threading.Lock()
        self.cmd = None
        self.lockcmd = threading.Lock()
        print 'init Xbee completed'


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
        while True:
            byte = self.serial.read()
            if byte == APIFrame.START_BYTE:
                self.lock.acquire()
                frame = self.wait_read_Packet(byte)
                self.lock.release()
                try:
                    data = self._split_response(frame.data)['rf_data']
                    return data , get_sensor_data
                except Exception as e:
                    command = self._split_response(frame.data)['deliver_status']
                    return command, get_command_data

    def listen_from_node(self, send_webservice, STATION_ID, STATION_PASS, gui, root):
        while True:
            data, check_data_type = self.readPacket()
            if data != '' and check_data_type == get_sensor_data:
                sys.stdout.flush()
                print 'Received from node:' , data
                sys.stdout.flush()
                gui.displaynode(root, '('+data+')')
                sen = self.dat.Sensor_data('('+data+')', self.config)
                thread1 = threading.Thread(target=send_webservice.sent_data, args=(sen,))
                thread1.start()
            elif data != '' and check_data_type == get_command_data:
                self.cmd = data


        
    def __write(self, data):
        """
        _write: binary data -> None

        Packages the given binary data in an API frame and writes the
        result to the serial port
        """
        frame = APIFrame(data, self._escaped).output()
        self.serial.write(frame)

    def _send(self, cmd, **kwargs):
        """
        send: string param=binary data ... -> None

        When send is called with the proper arguments, an API command
        will be written to the serial port for this XBee device
        containing the proper instructions and data.

        This method must be called with named arguments in accordance
        with the api_command specification. Arguments matching all
        field names other than those in reserved_names (like 'id' and
        'order') should be given, unless they are of variable length
        (of 'None' in the specification. Those are optional).
        """
        # Pass through the keyword arguments
        self.__write(self._build_command(cmd, **kwargs))
    
        
    def send_command(self, node_id, command):
        try:
            
            self.lockcmd.acquire()
            self.lock.acquire()
            
            addr=self.config.map_address[node_id]
            #print '-----send cm', command, addr,'--------'
            self._send('tx', dest_addr_long=addr, dest_addr='\xff\xfe', data=command)
            self.lock.release()
            start = time.time()
            while self.cmd != get_success:
                #print self.cmd
                if time.time() - start > time_to_wait:
                    self.lockcmd.release()
                    if command[0:1] != '[':
                        print "Send command Failed", command#debug
                    return False
            if command[0:1] != '[':
                print "SEND COMMAND SUCCESS:", command#debug
            self.cmd = ''
            self.lockcmd.release()
            return True
        except KeyError as m:
            print 'NOT FIND ADDRESS'
            self.lockcmd.release()
            self.lock.release()
        except Exception as e:
            raise e
            self.lock.release()
            self.lockcmd.release()
            print 'Send command error'
            return False
    def send_config(self, node_id, cofig):
        pass
##map_address={"2":"\x00\x13\xA2\x00\x40\xF1\xED\x40",
##             "1":"\x00\x13\xA2\x00\x40\xF1\xED\x0E",
##             "01":"\x00\x13\xA2\x00\x40\xF1\xED\x0E",
##             "123":"\x00\x13\xA2\x00\x40\xF1\xED\x40"}

##    def send_config(self, addr, config):
##            config_packet1 = config[:65]
##            config_packet2 = config[65:]
##            self.send_command(addr, config_packet1)
##            self.send_command(addr, config_packet2)

##PORT = '/dev/ttyUSB0'
##BAUD_RATE = 9600
##ser = serial.Serial(PORT, BAUD_RATE, timeout=1)
##
##config = "[airTemperature#10#0##25#0#,airHumidity#20#0##45#0#,soilTemperature#18#0##33#0#,soilMoisture#10#0##15#0#,lightIntensity#60#0##150#0#]"
##dataoff = "000:0"
##addr = "\x00\x13\xA2\x00\x40\xF1\xED\x40"
##zb = Zigbee(ser, None, None)
##zb.send_command('2',config)
##while True:
##    print zb.readPacket()
##    time.sleep(5)
##    print "back"
####    #zb.send('tx', dest_addr_long='\x00\x13\xA2\x00\x40\xF1\xED\x0E', dest_addr='\xff\xfe', data='hello')
##    print zb.readPacket()
##    time.sleep(5)
##while True:
##    data, check_data_type = zb.readPacket()
##    print data
#node="00"
##def main():
##    while True:
##        zb.send_command(node, config)
##        time.sleep(2)
##   
####    ##while True:
####    ##    print xb.readPacket()
#thread1 = threading.Thread(target=zb.listen_from_node, args=(None, None, None, None, None, None))
#thread1.start()
#time.sleep(1)
#thread2 = threading.Thread(target=main, args=())
#thread2.start()
##zb.send_command(addr, '222')
##time.sleep(.5)
##zb.send_command(addr, '4444')
##time.sleep(.5)
##zb.send_command(addr, dataoff)
##time.sleep(.5)
##zb.send_command(addr, dataoff)
##time.sleep(.5)
##zb.send_command(addr, dataoff)
##time.sleep(.5)
##zb.send_command(addr, dataoff)
##
##thread2 = threading.Thread(target=main, args=())
##thread2.start()

"""xb = Xbee(ser)
xb.send_command(addr, data)"""
