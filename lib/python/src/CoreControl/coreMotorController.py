"""
coreMotorController.py - Core motor module class for the Fusion system
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

class coreMotorController:
    POWER       = 0x00 
    SPEED       = 0x01 
    POSITION    = 0x02 
    RESET       = 0x03
    
    M1          = 0x01 
    M2          = 0x02

    def __init__(self, driver, dev_id):
        self.driver = driver 
        self.dev_id = dev_id 
        dev_index = self.driver.serial_numbers.index(self.dev_id)
        self.PORT = serial.Serial("/dev/" + self.driver.port_list[dev_index], baudrate=250000)
        self.PORT.close()
        self.PORT.open()
                
    def __del__(self):
        self.driver.FTDI_WRITE(0x00, [0x00]*0x56, self.PORT)
        self.PORT.close()
        return;
    
    def constantSpeed(self, motor, power):    
        if (power == 128): pass 
        elif (power < -100): power = -100 
        elif (power > 100): power = 100 
        
        if(power < 0): power += 256
        
        if (motor == 1): 
            temp_buf = [0x00, 0x00, 0x00, 0x00, self.SPEED, power]
            self.driver.FTDI_WRITE(0x40, temp_buf, self.PORT)
        elif (motor == 2): 
            temp_buf = [power, self.SPEED, 0x00, 0x00, 0x00, 0x00]
            self.driver.FTDI_WRITE(0x46, temp_buf, self.PORT)
        return;
    
    def constantPower(self, motor, power):
        if (power == 128): pass 
        elif (power < -100): power = -100 
        elif (power > 100): power = 100 
        
        if(power < 0): power += 256
        
        if (motor == 1): 
            temp_buf = [0x00, 0x00, 0x00, 0x00, self.POWER, power]
            self.driver.FTDI_WRITE(0x40, temp_buf, self.PORT)
        elif (motor == 2): 
            temp_buf = [power, self.POWER, 0x00, 0x00, 0x00, 0x00]
            self.driver.FTDI_WRITE(0x46, temp_buf, self.PORT)
        return;
        
    def runToPosition(self, motor, power, target):
        if (power == 128): pass 
        elif (power < -100): power = -100 
        elif (power > 100): power = 100 
        
        if(power < 0): power += 256
        
        if (motor == 1): 
            temp_buf = [(target >> 24) & 0xFF, (target >> 16) & 0xFF, (target >> 8) & 0xFF, target & 0xFF, self.POSITION, power]
            self.driver.FTDI_WRITE(0x40, temp_buf, self.PORT)
        elif (motor == 2): 
            temp_buf = [power, self.POSITION, (target >> 24) & 0xFF, (target >> 16) & 0xFF, (target >> 8) & 0xFF, target & 0xFF]
            self.driver.FTDI_WRITE(0x46, temp_buf, self.PORT)
        return;
        
    # ---------------------------------------------------------------------------
    def readEncoder(self, motor):
        if (motor == 1): register = 0x4C
        elif (motor == 2): register = 0x50 
        else: return;
        
        temp_buf = self.driver.FTDI_READ(register, [0x00]*4, self.PORT)
        temp = ((temp_buf[0]<<24) | (temp_buf[1]<<16) | (temp_buf[2]<<8) | temp_buf[3])
        if(temp >= 2147483647): temp -= 4294967295
        return temp;
        
    # ---------------------------------------------------------------------------
    def readBattVoltage(self):
        temp_buf = self.driver.FTDI_READ(0x54, [0x00, 0x00], self.PORT)
        return((temp_buf[0]<<2) | temp_buf[1]);
        
    # ---------------------------------------------------------------------------
    def readPIDvalues(self, motor):
        if(motor == 1): return self.driver.FTDI_READ(0x56, [0x00]*4, self.PORT);
        elif(motor == 2): return self.driver.FTDI_READ(0x5A, [0x00]*4, self.PORT);
        else: return None;
    
    # ---------------------------------------------------------------------------    
    def writePIDvalues(self, motor, buf):
        if (motor == 1):
            self.driver.FTDI_WRITE(0x03, [0xBB], self.PORT)
            self.driver.FTDI_WRITE(0x56, buf, self.PORT)
            self.driver.FTDI_WRITE(0x03, [0x00], self.PORT) 
            
        elif (motor == 2):
            self.driver.FTDI_WRITE(0x03, [0xBB], self.PORT)
            self.driver.FTDI_WRITE(0x5A, buf, self.PORT)
            self.driver.FTDI_WRITE(0x03, [0x00], self.PORT) 
        else: return None;       
        return;