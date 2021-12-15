"""
coreLegacyModule.py - Core legacy module class for the Fusion system
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
import time 
from ht_EOPD import *
from ht_ForceSensor import *
from ht_Accelerometer import *
from ht_Angle import *
from ht_Compass import *
from ht_Color import *
from ht_Barometric import *
from ht_IRseekerV2 import *
from ht_IRreciever import *
from ht_Magnetic import *
from nxt_Touch import * 
from nxt_Ultrasonic import * 
from nxt_Sound import *
from nxt_Light import *

class coreLegacyModule:
    S0      = 0x00 
    S1      = 0x01 
    S2      = 0x02 
    S3      = 0x03 
    S4      = 0x04
    S5      = 0x05
    
    ON      = 0x01 
    OFF     = 0x00

    def __init__(self, driver, dev_id):
        self.driver = driver 
        self.dev_id = dev_id 
        dev_index = self.driver.serial_numbers.index(self.dev_id)
        self.PORT = serial.Serial("/dev/" + self.driver.port_list[dev_index], baudrate=250000)
        self.PORT.close()
        self.PORT.open()
        
    def __del__(self):
        self.driver.FTDI_WRITE(0x00, [0x00]*0xD1, self.PORT)
        self.PORT.close()
        
    # ---------------------------------------------------------------------------
    def analogRead(self, sensor_port):
        if (sensor_port < 0): sensor_port = 0 
        elif (sensor_port > 5): sensor_port = 5 
        start_addr = 0x04 + (0x02 * sensor_port)
        temp_buf = self.driver.FTDI_READ(start_addr, [0x00, 0x00], self.PORT)
        return (temp_buf[1] << 8) | temp_buf[0]
        
    # ---------------------------------------------------------------------------
    def digitalEnable(self, sensor_port, pin, value):
        if (sensor_port < 0): sensor_port = 0 
        elif (sensor_port > 5): sensor_port = 5
        start_addr = 0x10 + (0x20 * sensor_port)
        temp = self.driver.FTDI_READ(start_addr, [0x00], self.PORT)[0]
        if(pin == 0):
            if (value == 1): temp |= 0x04
            else: temp &= 0xFB
        elif(pin == 1):
            if (value == 1): temp |= 0x08
            else: temp &= 0xF7
        else: return; 
        
        self.driver.FTDI_WRITE(start_addr, [temp], self.PORT)
        return;
        
    # ---------------------------------------------------------------------------
    def enable_9v (self, sensor_port, state=False):
        if (sensor_port < 0): sensor_port = 0 
        elif (sensor_port > 5): sensor_port = 5
        start_addr = 0x10 + (0x20 * sensor_port)
        temp = self.driver.FTDI_READ(start_addr, [0x00], self.PORT)[0]
        if (state == True): temp |= 0x02
        else: temp &= 0xFD        
        self.driver.FTDI_WRITE(start_addr, [temp], self.PORT)        
        return;
        
    # ---------------------------------------------------------------------------   
    def i2cRead(self, sensor_port, addr, reg, len):
        if (sensor_port < 0): sensor_port = 0 
        elif (sensor_port > 5): sensor_port = 5 
        start_addr = 0x10 + (0x20 * sensor_port)
        temp = self.driver.FTDI_READ(start_addr, [0x00], self.PORT)[0]
        temp |= 0x81     
        temp_buf = [temp, addr, reg, len] + [0x00]*27 + [0xFF]        
        self.driver.FTDI_WRITE(start_addr, temp_buf, self.PORT)
        time.sleep(0.001)
        return self.driver.FTDI_READ(start_addr, temp_buf, self.PORT)[4:4+len]
    
    # ---------------------------------------------------------------------------    
    def i2cWrite(self, sensor_port, addr, reg, buffer):
        if (sensor_port < 0): sensor_port = 0 
        elif (sensor_port > 5): sensor_port = 5 
        start_addr = 0x10 + (0x20 * sensor_port)
        temp = self.driver.FTDI_READ(start_addr, [0x00], self.PORT)[0]
        temp &= 0x0E
        temp |= 0x01
        temp_buf = [temp, addr, reg, len(buffer)] + buffer + [0x00]*(27-len(buffer)) + [0xFF]        
        self.driver.FTDI_WRITE(start_addr, temp_buf, self.PORT)
        return None;   
        
    # ---------------------------------------------------------------------------    
    def setLED(self, led, set):
        value = self.driver.FTDI_READ(0xD0, [0x00], self.PORT)[0]
        if (led == 0):
            if (set == 1): value |= 0x01 
            else: value &= ~0x01 
            
        elif (led == 1):
            if (set == 1): value |= 0x02 
            else: value &= ~0x02
            
        elif (led == 3):
            if (set == 1): value |= 0x04 
            else: value &= ~0x04
            
        elif (led == 2):
            if (set == 1): value |= 0x08 
            else: value &= ~0x08
            
        else: pass 
        self.driver.FTDI_WRITE(0xD0, [value], self.PORT)
        return;

    # ---------------------------------------------------------------------------    
    def getAddress(self, sensor_port):
        if (sensor_port < 0): sensor_port = 0 
        elif (sensor_port > 5): sensor_port = 5 
        start_addr = 0x10 + (0x20 * sensor_port)
        
        temp_buf = [0x81, 0x00, 0x40, 0x01] + [0x00]*27 + [0xFF]
        self.driver.FTDI_WRITE(start_addr, temp_buf, self.PORT)
        
        for i in range(0, 127):
            self.driver.FTDI_WRITE(start_addr+1, [i&0xFE], self.PORT)
            self.driver.FTDI_WRITE(start_addr+0x1F, [0xFF], self.PORT)
            time.sleep(0.001)
            temp_buf = self.driver.FTDI_READ(start_addr+4, [0x00], self.PORT)
            if (temp_buf[0] != 0xFF): return i;
        
        return False; 
    
    # -------------------------------------------------------------------------
    # Sensor library constructors 
    def ht_EOPD(self, port_loc): return ht_EOPD(self, port_loc)
    def ht_ForceSensor(self, port_loc): return ht_ForceSensor(self, port_loc)
    def ht_Accelerometer(self, port_loc): return ht_Accelerometer(self, port_loc)
    def ht_Angle(self, port_loc): return ht_Angle(self, port_loc)
    def ht_Compass(self, port_loc): return ht_Compass(self, port_loc)
    def ht_Color(self, port_loc): return ht_Color(self, port_loc)
    def ht_Barometric(self, port_loc): return ht_Barometric(self, port_loc)
    def ht_IRseekerV2(self, port_loc): return ht_IRseekerV2(self, port_loc)
    def ht_IRreciever(self, port_loc): return ht_IRreciever(self, port_loc)
    def ht_Magnetic(self, port_loc): return ht_Magnetic(self, port_loc)
    def nxt_Touch(self, port_loc): return nxt_Touch(self, port_loc)
    def nxt_Ultrasonic(self, port_loc): return nxt_Ultrasonic(self, port_loc)
    def nxt_Sound(self, port_loc): return nxt_Sound(self, port_loc)
    def nxt_Light(self, port_loc): return nxt_Light(self, port_loc)
   
    