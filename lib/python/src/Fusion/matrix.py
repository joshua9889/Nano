"""
matrix.py - Matrix Controller class for the Fusion system
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

class locator360:
    obj = None 
    addr = None 
    
    S1  = 0x01
    S2  = 0x02
    S3  = 0x04 
    S4  = 0x08 
    M1  = 0x01 
    M2  = 0x02 
    M3  = 0x04 
    M4  = 0x08
    
    PENDING = 0x80 
    INVERT  = 0x10 
    FLOAT   = 0x00 
    BRAKE   = 0x01 
    SPEED   = 0x02 
    SLEW    = 0x03 
    
    SERVO_ENABLE_STORED = 0x00
    CURRENT_BUFFER      = 0x00
    BUFF_LENGTH         = 16
    I2C_BUFFER          = [0x00]*16    
    
    S1_SPEED            = 0
    S1_TARGET           = 0
    S2_SPEED            = 0
    S2_TARGET           = 0
    S3_SPEED            = 0
    S3_TARGET           = 0
    S4_SPEED            = 0
    S4_TARGET           = 0
    
    M1_MODE             = 0
    M2_MODE             = 0
    M3_MODE             = 0
    M4_MODE             = 0
    
    def __init__(self, main_obj, i2c_addr=0x12):
        self.obj = main_obj
        self.addr = i2c_addr
        
    #def __del__(self):
    
    def servoEnable(self, servo, state):
        if(state == True): self.SERVO_ENABLE_STORED |= servo
        else: self.SERVO_ENABLE_STORED &= ~servo
        self.I2C_BUFFER[0] = 0x00
        self.I2C_BUFFER[1] = 0x10
        self.I2C_BUFFER[2] = 0x45
        self.I2C_BUFFER[3] = 0x01
        self.I2C_BUFFER[4] = self.SERVO_ENABLE_STORED
        self.I2C_BUFFER[self.BUFF_LENGTH-1] = 0xFF        
        self.nextBuffer()
        self.obj.i2cWrite(self.addr, self.CURRENT_BUFFER, self.I2C_BUFFER)
        return;
    
    def servoTarget(self, servo, target):
        if((servo & self.S1) == self.S1): self.S1_TARGET = target 
        if((servo & self.S2) == self.S2): self.S2_TARGET = target 
        if((servo & self.S3) == self.S3): self.S3_TARGET = target 
        if((servo & self.S4) == self.S4): self.S4_TARGET = target 
        
        self.nextBuffer()
        self.I2C_BUFFER[0] = 0x00 
        self.I2C_BUFFER[1] = 0x10 
        self.I2C_BUFFER[2] = 0x46
        self.I2C_BUFFER[3] = 0x08 
        self.I2C_BUFFER[4] = self.S1_SPEED 
        self.I2C_BUFFER[5] = self.S1_TARGET
        self.I2C_BUFFER[6] = self.S2_SPEED 
        self.I2C_BUFFER[7] = self.S2_TARGET
        self.I2C_BUFFER[8] = self.S3_SPEED 
        self.I2C_BUFFER[9] = self.S3_TARGET
        self.I2C_BUFFER[10] = self.S4_SPEED 
        self.I2C_BUFFER[11] = self.S4_TARGET
        self.I2C_BUFFER[self.BUFF_LENGTH-1] = 0xFF;
        self.obj.i2cWrite(self.addr, self.CURRENT_BUFFER, self.I2C_BUFFER)
        return;
        
    def servoSpeed(self, servo, speed):
        if((servo & self.S1) == self.S1): self.S1_SPEED = speed 
        if((servo & self.S2) == self.S2): self.S2_SPEED = speed
        if((servo & self.S3) == self.S3): self.S3_SPEED = speed
        if((servo & self.S4) == self.S4): self.S4_SPEED = speed
        
        self.nextBuffer()
        self.I2C_BUFFER[0] = 0x00 
        self.I2C_BUFFER[1] = 0x10 
        self.I2C_BUFFER[2] = 0x46
        self.I2C_BUFFER[3] = 0x08 
        self.I2C_BUFFER[4] = self.S1_SPEED 
        self.I2C_BUFFER[5] = self.S1_TARGET
        self.I2C_BUFFER[6] = self.S2_SPEED 
        self.I2C_BUFFER[7] = self.S2_TARGET
        self.I2C_BUFFER[8] = self.S3_SPEED 
        self.I2C_BUFFER[9] = self.S3_TARGET
        self.I2C_BUFFER[10] = self.S4_SPEED 
        self.I2C_BUFFER[11] = self.S4_TARGET
        self.I2C_BUFFER[self.BUFF_LENGTH-1] = 0xFF;
        self.obj.i2cWrite(self.addr, self.CURRENT_BUFFER, self.I2C_BUFFER)
        return;
    
    def motorSpeed(self, motor, speed):
        if(speed > 100): speed = 100 
        elif (speed < -100): speed = -100 
        self.I2C_BUFFER[0] = 0x00 
        self.I2C_BUFFER[1] = 0x10 
        self.I2C_BUFFER[3] = 0x01 
        self.I2C_BUFFER[4] = speed 
        
        if((motor & self.M1) == self.M1):
            self.nextBuffer()
            self.I2C_BUFFER[3] = 0x56 
            self.I2C_BUFFER[self.BUFF_LENGTH-1] = 0xFF 
            self.obj.i2cWrite(self.addr, self.CURRENT_BUFFER, self.I2C_BUFFER)
            
        if((motor & self.M2) == self.M2):
            self.nextBuffer()
            self.I2C_BUFFER[3] = 0x60 
            self.I2C_BUFFER[self.BUFF_LENGTH-1] = 0xFF 
            self.obj.i2cWrite(self.addr, self.CURRENT_BUFFER, self.I2C_BUFFER)
            
        if((motor & self.M3) == self.M3):
            self.nextBuffer()
            self.I2C_BUFFER[3] = 0x6A 
            self.I2C_BUFFER[self.BUFF_LENGTH-1] = 0xFF 
            self.obj.i2cWrite(self.addr, self.CURRENT_BUFFER, self.I2C_BUFFER)
            
        if((motor & self.M4) == self.M4):
            self.nextBuffer()
            self.I2C_BUFFER[3] = 0x75 
            self.I2C_BUFFER[self.BUFF_LENGTH-1] = 0xFF 
            self.obj.i2cWrite(self.addr, self.CURRENT_BUFFER, self.I2C_BUFFER)
        return;        
    
    def motorMode(self, motor, mode):
        self.I2C_BUFFER[0] = 0x00 
        self.I2C_BUFFER[1] = 0x10 
        self.I2C_BUFFER[3] = 0x01 
        self.I2C_BUFFER[4] = mode 
        
        if((motor & self.M1) == self.M1):
            self.nextBuffer()
            self.I2C_BUFFER[3] = 0x57 
            self.I2C_BUFFER[self.BUFF_LENGTH-1] = 0xFF 
            self.obj.i2cWrite(self.addr, self.CURRENT_BUFFER, self.I2C_BUFFER)
            self.M1_MODE = mode 
            
        if((motor & self.M2) == self.M2):
            self.nextBuffer()
            self.I2C_BUFFER[3] = 0x61
            self.I2C_BUFFER[self.BUFF_LENGTH-1] = 0xFF 
            self.obj.i2cWrite(self.addr, self.CURRENT_BUFFER, self.I2C_BUFFER)
            self.M2_MODE = mode 
            
        if((motor & self.M3) == self.M3):
            self.nextBuffer()
            self.I2C_BUFFER[3] = 0x6B 
            self.I2C_BUFFER[self.BUFF_LENGTH-1] = 0xFF 
            self.obj.i2cWrite(self.addr, self.CURRENT_BUFFER, self.I2C_BUFFER)
            self.M3_MODE = mode 
            
        if((motor & self.M4) == self.M4):
            self.nextBuffer()
            self.I2C_BUFFER[3] = 0x76 
            self.I2C_BUFFER[self.BUFF_LENGTH-1] = 0xFF 
            self.obj.i2cWrite(self.addr, self.CURRENT_BUFFER, self.I2C_BUFFER)
            self.M4_MODE = mode 
            
        return;
    
    def motorReset(self, motor):
        self.I2C_BUFFER[0] = 0x00 
        self.I2C_BUFFER[1] = 0x10 
        self.I2C_BUFFER[3] = 0x01 
        self.I2C_BUFFER[4] = 0x04 
        
        if((motor & self.M1) == self.M1):
            self.nextBuffer()
            self.I2C_BUFFER[3] = 0x57 
            self.I2C_BUFFER[self.BUFF_LENGTH-1] = 0xFF 
            self.obj.i2cWrite(self.addr, self.CURRENT_BUFFER, self.I2C_BUFFER)
            self.motorMode(self.M1, self.M1_MODE)
            
        if((motor & self.M2) == self.M2):
            self.nextBuffer()
            self.I2C_BUFFER[3] = 0x61 
            self.I2C_BUFFER[self.BUFF_LENGTH-1] = 0xFF 
            self.obj.i2cWrite(self.addr, self.CURRENT_BUFFER, self.I2C_BUFFER)
            self.motorMode(self.M2, self.M2_MODE)
            
        if((motor & self.M3) == self.M3):
            self.nextBuffer()
            self.I2C_BUFFER[3] = 0x6B 
            self.I2C_BUFFER[self.BUFF_LENGTH-1] = 0xFF 
            self.obj.i2cWrite(self.addr, self.CURRENT_BUFFER, self.I2C_BUFFER)
            self.motorMode(self.M3, self.M3_MODE)
            
        if((motor & self.M4) == self.M4):
            self.nextBuffer()
            self.I2C_BUFFER[3] = 0x76 
            self.I2C_BUFFER[self.BUFF_LENGTH-1] = 0xFF 
            self.obj.i2cWrite(self.addr, self.CURRENT_BUFFER, self.I2C_BUFFER)
            self.motorMode(self.M4, self.M4_MODE)
        return;
        
    def motorPending(self, motor, mode):
        if(speed > 100): speed = 100 
        elif (speed < -100): speed = -100 
        self.I2C_BUFFER[0] = 0x00 
        self.I2C_BUFFER[1] = 0x10 
        self.I2C_BUFFER[3] = 0x02 
        self.I2C_BUFFER[4] = speed 
        
        if((motor & self.M1) == self.M1):
            self.nextBuffer()
            self.I2C_BUFFER[3] = 0x56 
            self.I2C_BUFFER[5] = (self.M1_MODE & 0x13) | 0x08
            self.I2C_BUFFER[self.BUFF_LENGTH-1] = 0xFF 
            self.obj.i2cWrite(self.addr, self.CURRENT_BUFFER, self.I2C_BUFFER)
            
        if((motor & self.M2) == self.M2):
            self.nextBuffer()
            self.I2C_BUFFER[3] = 0x60 
            self.I2C_BUFFER[5] = (self.M2_MODE & 0x13) | 0x08
            self.I2C_BUFFER[self.BUFF_LENGTH-1] = 0xFF 
            self.obj.i2cWrite(self.addr, self.CURRENT_BUFFER, self.I2C_BUFFER)
            
        if((motor & self.M3) == self.M3):
            self.nextBuffer()
            self.I2C_BUFFER[3] = 0x6A 
            self.I2C_BUFFER[5] = (self.M3_MODE & 0x13) | 0x08
            self.I2C_BUFFER[self.BUFF_LENGTH-1] = 0xFF 
            self.obj.i2cWrite(self.addr, self.CURRENT_BUFFER, self.I2C_BUFFER)
            
        if((motor & self.M4) == self.M4):
            self.nextBuffer()
            self.I2C_BUFFER[3] = 0x75 
            self.I2C_BUFFER[5] = (self.M4_MODE & 0x13) | 0x08
            self.I2C_BUFFER[self.BUFF_LENGTH-1] = 0xFF 
            self.obj.i2cWrite(self.addr, self.CURRENT_BUFFER, self.I2C_BUFFER)
        return;
        
    def startPending(self):
        self.nextBuffer()
        self.I2C_BUFFER[0] = 0x00 
        self.I2C_BUFFER[1] = 0x10 
        self.I2C_BUFFER[2] = 0x44 #Start Flag
        self.I2C_BUFFER[3] = 0x01 
        self.I2C_BUFFER[4] = 0x01 
        self.I2C_BUFFER[self.BUFF_LENGTH-1] = 0xFF 
        self.obj.i2cWrite(self.addr, self.CURRENT_BUFFER, self.I2C_BUFFER)
        return;
    
    def motorPosition(self, motor):
        if((motor & self.M1) == self.M1): self.I2C_BUFFER[2] = 0x4E         #M1 position 
        elif((motor & self.M1) == self.M1): self.I2C_BUFFER[2] = 0x58    #M2 position 
        elif((motor & self.M1) == self.M1): self.I2C_BUFFER[2] = 0x62    #M3 position 
        elif((motor & self.M1) == self.M1): self.I2C_BUFFER[2] = 0x6C    #M4 position 
        else: return 0;
        
        self.nextBuffer()
        self.I2C_BUFFER[0] = 0x80 
        self.I2C_BUFFER[1] = 0x10 
        self.I2C_BUFFER[3] = 0x04
        self.I2C_BUFFER[self.BUFF_LENGTH-1] = 0xFF 
        
        self.obj.i2cWrite(self.addr, self.CURRENT_BUFFER, self.I2C_BUFFER)
        while(self.obj.i2cRead(self.addr, self.CURRENT_BUFFER+self.BUFF_LENGTH-2, 1)[0] != 0x00): pass 
        data = self.obj.i2cRead(self.addr, self.CURRENT_BUFFER+4, 4)
        
        output = data[0] << 24 
        output |= data[1] << 16 
        output |= data[2] << 8 
        output |= data[3] 
        
        return output;
    
    def motorTarget(self, motor, target):    
        self.I2C_BUFFER[0] = 0x00 
        self.I2C_BUFFER[1] = 0x10 
        self.I2C_BUFFER[3] = 0x05
        self.I2C_BUFFER[4] = (target & 0xFF000000) >> 24 
        self.I2C_BUFFER[5] = (target & 0x00FF0000) >> 16 
        self.I2C_BUFFER[6] = (target & 0x0000FF00) >> 8 
        self.I2C_BUFFER[7] = (target & 0x000000FF) 
        self.I2C_BUFFER[8] = speed 
        
        if((motor & self.M1) == self.M1): 
            self.nextBuffer()
            self.I2C_BUFFER[2] = 0x52 
            self.I2C_BUFFER[self.BUFF_LENGTH-1] = 0xFF 
            self.obj.i2cWrite(self.addr, self.CURRENT_BUFFER, self.I2C_BUFFER)
            
        if((motor & self.M2) == self.M2): 
            self.nextBuffer()
            self.I2C_BUFFER[2] = 0x5C 
            self.I2C_BUFFER[self.BUFF_LENGTH-1] = 0xFF 
            self.obj.i2cWrite(self.addr, self.CURRENT_BUFFER, self.I2C_BUFFER)
            
        if((motor & self.M3) == self.M3): 
            self.nextBuffer()
            self.I2C_BUFFER[2] = 0x66 
            self.I2C_BUFFER[self.BUFF_LENGTH-1] = 0xFF 
            self.obj.i2cWrite(self.addr, self.CURRENT_BUFFER, self.I2C_BUFFER)
            
        if((motor & self.M4) == self.M4): 
            self.nextBuffer()
            self.I2C_BUFFER[2] = 0x71 
            self.I2C_BUFFER[self.BUFF_LENGTH-1] = 0xFF 
            self.obj.i2cWrite(self.addr, self.CURRENT_BUFFER, self.I2C_BUFFER)

        return;
        
    def getBatteryVoltage(self):
        self.nextBuffer()
        self.I2C_BUFFER[0] = 0x80 
        self.I2C_BUFFER[1] = 0x10 
        self.I2C_BUFFER[2] = 0x43
        self.I2C_BUFFER[3] = 0x01
        self.I2C_BUFFER[self.BUFF_LENGTH-1] = 0xFF 
        
        self.obj.i2cWrite(self.addr, self.CURRENT_BUFFER, self.I2C_BUFFER)
        while(self.obj.i2cRead(self.addr, self.CURRENT_BUFFER+self.BUFF_LENGTH-2, 1)[0] != 0x00): pass 
        return (self.obj.i2cRead(self.addr, self.CURRENT_BUFFER+4, 1)[0] * 40);
    
    def getControllerStatus(self):
        self.nextBuffer()
        self.I2C_BUFFER[0] = 0x80 
        self.I2C_BUFFER[1] = 0x10 
        self.I2C_BUFFER[2] = 0x41
        self.I2C_BUFFER[3] = 0x01
        self.I2C_BUFFER[self.BUFF_LENGTH-1] = 0xFF 
        
        self.obj.i2cWrite(self.addr, self.CURRENT_BUFFER, self.I2C_BUFFER)
        while(self.obj.i2cRead(self.addr, self.CURRENT_BUFFER+self.BUFF_LENGTH-2, 1)[0] != 0x00): pass 
        return self.obj.i2cRead(self.addr, self.CURRENT_BUFFER+4, 1)[0];
    
    def nextBuffer(self):
        if ((self.CURRENT_BUFFER & 0x04) == 0x04):
            self.CURRENT_BUFFER += 0x10
            if(self.CURRENT_BUFFER > 0x64):
                self.CURRENT_BUFFER = 0x04
                self.BUFF_LENGTH = 17 
            elif (self.CURRENT_BUFFER == 0x64): self.BUFF_LENGTH = 13
        else:
            self.CURRENT_BUFFER = 0x04 
            self.BUFF_LENGTH = 17 
        while(self.obj.i2cRead(self.addr, self.CURRENT_BUFFER+self.BUFF_LENGTH-2, 1)[0] != 0x00): pass 
        return self.CURRENT_BUFFER;
        