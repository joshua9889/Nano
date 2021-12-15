import serial
import os 
import commands 
import time
from pylibftdi import Driver

class driver:    
    def __init__(self):
        self.port_list = []
        self.dev_id = []
        self.serial_numbers = []
        self.updateDevices()
    
    def updateDevices(self):
        for fname in os.listdir('/dev'):
            if 'ttyUSB' in fname:
                self.port_list.append(fname) 
        
        for i in range(0, len(self.port_list)):
            port = serial.Serial("/dev/"+self.port_list[i], baudrate=250000)
            port.close()
            port.open()
            time.sleep(0.01)
            TEMP_BUF = self.FTDI_READ(0x02, [0x00], port)
            port.close()
            time.sleep(0.01)
            self.dev_id.append(TEMP_BUF[0])

        for i in range(0, len(self.dev_id)):
            if(self.dev_id[i] == 0x4D): self.dev_id[i] = "USBMCON"
            elif(self.dev_id[i] == 0x41): self.dev_id[i] = "USBAMUX"
            elif(self.dev_id[i] == 0x49): self.dev_id[i] = "USBLSMUX"
            elif(self.dev_id[i] == 0x53): self.dev_id[i] = "USBSCON"
            else: self.dev_id[i] = "UNKNOWN"
            
        dev_list = []
        for device in Driver().list_devices():
            # list_devices returns bytes rather than strings
            dev_info = map(lambda x: x.decode('latin1'), device)
            self.serial_numbers.append(str(dev_info[2]))
        
    def printDevices(self):        
        print 
        print "Serial Ports   = " + str(self.port_list)
        print "Device IDs     = " + str(self.dev_id)
        print "Serial Numbers = " + str(self.serial_numbers)
        print 
    
    # -----------------------------------------------------------------------------
    def FTDI_WRITE(self, start, buffer_data, ser_port):
        WRITE_HEADER = [0x55, 0xAA, 0x00, start, len(buffer_data)]
        WRITE_RESPONSE = [0x33, 0xCC, 0x00, start, 0x00]
        RESPONSE_HEADER = [0x00] * 5
        
        ser_port.flushInput()
        ser_port.write(self.hexstr(WRITE_HEADER) + self.hexstr(buffer_data))
        counter = 0
        while ser_port.inWaiting() < 5 and counter <= 50000:
            counter += 1
        if counter >= 50000:
            return;
        for i in range (0, 5):
            RESPONSE_HEADER[i] = ord(ser_port.read(1))
            
        if RESPONSE_HEADER != WRITE_RESPONSE: return;    
        return True;
        
    # -------------------------------------------------------------------------
    def FTDI_READ(self, start, buffer_data, ser_port):
        READ_HEADER = [0x55, 0xAA, 0x80, start, len(buffer_data)]
        READ_RESPONSE = [0x33, 0xCC, 0x80, start, len(buffer_data)]
        RESPONSE_HEADER = [0x00] * 5
        RESPONSE_DATA = []
        
        ser_port.flushInput()
        ser_port.write(self.hexstr(READ_HEADER))
        
        counter = 0
        while ser_port.inWaiting() < 5 and counter <= 50000:
            counter += 1  
        if counter >= 50000:
            return buffer_data;
        
        for i in range(0, 5):
            RESPONSE_HEADER[i] = ord(ser_port.read(1))  
        
        if RESPONSE_HEADER != READ_RESPONSE and RESPONSE_HEADER[4] != len(buffer_data): 
            return buffer_data;

        counter = 0
        while ser_port.inWaiting() < len(buffer_data) and counter <= 50000:
            counter += 1
        if counter >= 50000:
            return buffer_data;
        
        for i in range(0, len(buffer_data)):
            RESPONSE_DATA.append(ord(ser_port.read(1)))
        return RESPONSE_DATA;

    # -------------------------------------------------------------------------
    def hexstr(self, hexbuffer):
        return_string = ""
        for i in range(0, len(hexbuffer)):
            return_string += chr(hexbuffer[i])
        return return_string;