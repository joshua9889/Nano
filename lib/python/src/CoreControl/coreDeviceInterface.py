"""
coreDeviceInterface.py - Core device interface class for the Fusion system
Author: Justin Mathews
Copyright (c) 2018 Modern Robotics Inc.

Fusion Web Page: http://www.modernroboticsinc.com/fusion-controller

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

import serial
import Fusion 

class coreDeviceInterface:
    OUTPUT  = 1
    INPUT   = 0
    
    D0      = 0x00 
    D1      = 0x01
    D2      = 0x02
    D3      = 0x03
    D4      = 0x04
    D5      = 0x05
    D6      = 0x06
    D7      = 0x07
    
    A0      = 0x00 
    A1      = 0x01
    A2      = 0x02
    A3      = 0x03
    A4      = 0x04
    A5      = 0x05
    A6      = 0x06
    A7      = 0x07
    
    P0      = 0x00 
    P1      = 0x01
    
    AO0     = 0x00 
    AO1     = 0x01
    
    BLUE    = 0x00
    RED     = 0x01
    
    def __init__(self, driver, dev_id):
        self.driver = driver 
        self.dev_id = dev_id 
        dev_index = self.driver.serial_numbers.index(self.dev_id)
        self.PORT = serial.Serial("/dev/" + self.driver.port_list[dev_index], baudrate=250000)
        self.PORT.close()
        self.PORT.open()        
        
    def __del__(self):
        self.driver.FTDI_WRITE(0x00, [0x00]*0xD0, self.PORT)
        self.PORT.close()
        return;
    
    # ---------------------------------------------------------------------------    
    def getI2CAddresses(self):
        addresses = []
        temp_buf = [0x80, 0x00, 0x02, 0x01] + [0x00]*27 + [0xFF]
        self.driver.FTDI_WRITE(0x30, temp_buf, self.PORT)
        
        for i in range(0x10, 0xEE):
            if (i & 0x01 != 0x01):
                self.driver.FTDI_WRITE(0x31, [i], self.PORT)
                self.driver.FTDI_WRITE(0x4F, [0xFF], self.PORT)
                temp_buf = self.driver.FTDI_READ(0x34, [0x00], self.PORT) 
                if (temp_buf[0] != 0xFF): addresses.append([i, temp_buf[0]])                
        return addresses;
    
    # ---------------------------------------------------------------------------    
    def analogRead(self, analog_port):
        temp_buf = self.driver.FTDI_READ(0x04 + (analog_port * 0x02), [0x00, 0x00], self.PORT)
        return((temp_buf[1] << 8) | temp_buf[0]);
        
    # ---------------------------------------------------------------------------    
    def digitalState(self, port, state):
        temp_buf = self.driver.FTDI_READ(0x15, [0x00], self.PORT)              
        if state == 0: temp_buf[0] = temp_buf[0] & ((0x01 << port) ^ 0xFF)
        else: temp_buf[0] = temp_buf[0] | (0x01 << port)
        self.driver.FTDI_WRITE(0x15, temp_buf, self.PORT)
        return;
        
    # ---------------------------------------------------------------------------
    def digitalRead(self, port):
        mask = 0x01 << port
        temp_buf = self.driver.FTDI_READ(0x14, [0x00], self.PORT)        
        if (temp_buf[0] & mask) > 0: return 1;
        else: return 0;
        
    # ---------------------------------------------------------------------------
    def digitalWrite(self, port, value):
        if (port < 0): port = 0
        elif (port > 7): port = 7
        temp_buf = self.driver.FTDI_READ(0x16, [0x00], self.PORT)
        if value == 0: temp_buf[0] = temp_buf[0] & ((0x01 << port) ^ 0xFF)
        else: temp_buf[0] = temp_buf[0] | (0x01 << port)
        self.driver.FTDI_WRITE(0x16, temp_buf, self.PORT)
        return;
    
    # ---------------------------------------------------------------------------   
    def setLED(self, led, value):
        temp_buf = self.driver.FTDI_READ(0x17, [0x00], self.PORT)
        if value == 0: temp_buf[0] = temp_buf[0] & ((0x01 << led) ^ 0xFF)
        else: temp_buf[0] = temp_buf[0] | (0x01 << led)
        self.driver.FTDI_WRITE(0x17, temp_buf, self.PORT)
        return;
        
    # ---------------------------------------------------------------------------   
    def analogOutputWrite(self, port, voltage, frequency, mode):
        temp_buf = [voltage & 0x00FF, (voltage & 0xFF00) >> 8, frequency & 0x00FF, (frequency & 0xFF00) >> 8, mode]
        if port >= 1: register = 0x1E
        elif port <= 0: register = 0x18
        self.driver.FTDI_WRITE(register, temp_buf, self.PORT)
        return;
        
    # ---------------------------------------------------------------------------   
    def setPWM(self, port, on_time, period):
        temp_buf = [on_time & 0x00FF, (on_time & 0xFF00) >> 8, period & 0x00FF, (period & 0xFF00) >> 8]
        if port >= 1: register = 0x28 
        elif port <= 0: register = 0x24 
        self.driver.FTDI_WRITE(register, temp_buf, self.PORT)
        return;
    
    # ---------------------------------------------------------------------------
    def changeAddress(self, current, new):
        temp_buf = [0x00, current, 0x70, 0x03, new, 0x55, 0xAA] + [0x00]*24 + [0xFF]
        self.driver.FTDI_WRITE(0x30, temp_buf, self.PORT)
        return;
        
    # ---------------------------------------------------------------------------   
    def i2cRead(self, addr, reg, len):
        temp_buf = [0x80, addr, reg, len] + [0x00]*27 + [0xFF]
        self.driver.FTDI_WRITE(0x30, temp_buf, self.PORT)
        temp_buf = self.driver.FTDI_READ(0x30, temp_buf, self.PORT)
        return temp_buf[4:4+len]
    
    # ---------------------------------------------------------------------------    
    def i2cWrite(self, addr, reg, buffer):
        temp_buf = [0x00, addr, reg, len(buffer)] + buffer + [0x00]*(27-len(buffer)) + [0xFF]
        self.driver.FTDI_WRITE(0x30, temp_buf, self.PORT)
        return None;
        
    # -------------------------------------------------------------------------
    # Sensor library constructors 
    def analog (self, *args): return Fusion.analog(self, *args)
    def color (self, *args): return Fusion.color(self, *args)
    def colorBeacon (self, *args): return Fusion.colorBeacon(self, *args)
    def compass (self, *args): return Fusion.compass(self, *args)
    def digital (self, *args): return Fusion.digital(self, *args)
    def intGyro (self, *args): return Fusion.intGyro(self, *args)
    def locator360 (self, *args): return Fusion.locator360(self, *args)
    def range (self, *args): return Fusion.range(self, *args)
    def seekerV3 (self, *args): return Fusion.seekerV3(self, *args)
    def sound (self, *args): return Fusion.sound(self, *args)
    def thread (self, *args): return Fusion.thread(self, *args)
    def usbGamepad (self, *args): return Fusion.usbGamepad(self, *args)
        