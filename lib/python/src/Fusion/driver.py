#===============================================================================
# driver.py - Main sensor port driver class for the Fusion System
# Copyright (c) 2018-2019 Modern Robotics Inc.
#===============================================================================
# DISCLAIMER:
#   This software is provided "as is", without warranty of any kind, express or
#   implied, including but not limited to the warranties of merchantability,
#   fitness for a particular purpose and non-infringement. In no event shall 
#   the authors or copyright holders be liable for any claim, damages or other
#   liability, whether in an action of contract, tort or otherwise, arising 
#   from, out of, or in connection with the software or the use or other 
#   dealings in the software.
#===============================================================================
# REVISION HISTORY
#
# 18-Sep-19 <jwa> - Updated from the original version 
#
#===============================================================================


import time
import smbus
import traceback
import os 


class driver:
    BACKPACK_ADDRESS    = 0x08 
    
    VERSION             = 0x00
    MANUFACTURER        = 0x01
    DEVICE_ID           = 0x02
    COMMAND             = 0x03
    A0_LOW_BYTE         = 0x04
    A0_HIGH_BYTE        = 0x05
    A1_LOW_BYTE         = 0x06
    A1_HIGH_BYTE        = 0x07
    A2_LOW_BYTE         = 0x08
    A2_HIGH_BYTE        = 0x09
    A3_LOW_BYTE         = 0x0A
    A3_HIGH_BYTE        = 0x0B
    A4_LOW_BYTE         = 0x0C
    A4_HIGH_BYTE        = 0x0D
    A5_LOW_BYTE         = 0x0E
    A5_HIGH_BYTE        = 0x0F
    A6_LOW_BYTE         = 0x10
    A6_HIGH_BYTE        = 0x11
    A7_LOW_BYTE         = 0x12
    A7_HIGH_BYTE        = 0x13
    DIGITAL_INPUT       = 0x14
    DIGITAL_TRISTATE    = 0x15
    DIGITAL_OUTPUT      = 0x16
    SERVO_ENABLE        = 0x17
    SERVO_0_TARGET      = 0x18
    SERVO_1_TARGET      = 0x19
    SERVO_2_TARGET      = 0x1A
    SERVO_3_TARGET      = 0x1B
    MOTOR_0_MODE        = 0x1C
    MOTOR_0_SPEED       = 0x1D
    MOTOR_1_SPEED       = 0x1E
    MOTOR_1_MODE        = 0x1F
    I2C_MODE            = 0x20
    I2C_ADDR            = 0x21
    I2C_REGISTER        = 0x22
    I2C_LENGTH          = 0x23
    I2C_B0              = 0x24
    I2C_B1              = 0x25
    I2C_B2              = 0x26
    I2C_B3              = 0x27
    I2C_B4              = 0x28
    I2C_B5              = 0x29
    I2C_B6              = 0x2A
    I2C_B7              = 0x2B
    I2C_B8              = 0x2C
    I2C_B9              = 0x2D
    I2C_B10             = 0x2E
    I2C_B11             = 0x2F
    I2C_B12             = 0x30
    I2C_B13             = 0x31
    I2C_B14             = 0x32
    I2C_B15             = 0x33
    I2C_B16             = 0x34
    I2C_B17             = 0x35
    I2C_B18             = 0x36
    I2C_B19             = 0x37
    I2C_B20             = 0x38
    I2C_B21             = 0x39
    I2C_B22             = 0x3A
    I2C_B23             = 0x3B
    I2C_B24             = 0x3C
    I2C_B25             = 0x3D
    I2C_B26             = 0x3E
    I2C_FLAG            = 0x3F
    I2C_ERROR           = 0x40
    BATT_LOW            = 0x41
    BATT_HIGH           = 0x42
    POWER_STATE         = 0x43
    TEST_0              = 0x44
    TEST_1              = 0x45
    TEST_2              = 0x46
    TEST_3              = 0x47
    TEST_4              = 0x48
    
    S0 					= 0x01 
    S1 					= 0x02 
    S2 					= 0x04
    S3					= 0x08
    
    ENABLE              = 0x01
    DISABLE             = 0x00
	
    M0					= 0x01 
    M1					= 0x02 
    
    FLOAT               = 0x00 
    BRAKE               = 0x01
    
    D0                  = 0x0001 
    D1                  = 0x0002 
    D2                  = 0x0004 
    D3                  = 0x0008 
    D4                  = 0x0010 
    D5                  = 0x0020 
    D6                  = 0x0040 
    D7                  = 0x0080 
    
    A0                  = 0x0101 
    A1                  = 0x0102
    A2                  = 0x0104
    A3                  = 0x0108
    A4                  = 0x0110
    A5                  = 0x0120
    A6                  = 0x0140
    A7                  = 0x0180
    
    INPUT               = 0x01
    OUTPUT              = 0x00
    
    YELLOW              = 0x00
    BLUE                = 0x01
    
    i2cError = None
    bus = None 
    info = None
    
    def __init__(self):
        self.bus = smbus.SMBus(1)
        self.info = self.bus.read_i2c_block_data(self.BACKPACK_ADDRESS, self.VERSION, 3)
        try:
            self.bus.write_i2c_block_data(self.BACKPACK_ADDRESS, self.SERVO_0_TARGET, [128]*4)
        except:
            print traceback.format_exc(1)

        try: 
            with open("/sys/class/gpio/unexport", 'wb') as f: f.write("17")
        except: pass 
        
        try: 
            with open("/sys/class/gpio/unexport", 'wb') as f: f.write("18")
        except: pass
        
        try:
            with open("/sys/class/gpio/export", 'wb') as f: f.write("17")
        except: print traceback.format_exc(1)
        
        try:
            with open("/sys/class/gpio/export", 'wb') as f: f.write("18")
        except: print traceback.format_exc(1)
        
        try:
            with open("/sys/class/gpio/gpio17/direction", 'wb') as f: f.write("out")
        except: print traceback.format_exc(1)
        
        try:
            with open("/sys/class/gpio/gpio18/direction", 'wb') as f: f.write("out")        
        except: print traceback.format_exc(1)
        
    def __del__(self):
        try: 
            for i in range(0x40): self.bus.write_byte_data(self.BACKPACK_ADDRESS, i, 0x00)
        except: print traceback.format_exc(1)
        
        try:
            self.bus.write_i2c_block_data(self.BACKPACK_ADDRESS, self.SERVO_0_TARGET, [128]*4)
        except:
            print traceback.format_exc(1)
                
        try: 
            with open("/sys/class/gpio/unexport", 'wb') as f: f.write("17")
        except: print traceback.format_exc(1) 
        
        try: 
            with open("/sys/class/gpio/unexport", 'wb') as f: f.write("18")
        except: print traceback.format_exc(1)
                        
    def analogRead(self, port):
        try:
            if((port & 0x0100) == 0x0100):
                if (port == self.A0): temp = self.bus.read_i2c_block_data(self.BACKPACK_ADDRESS, self.A0_LOW_BYTE, 2)
                elif(port == self.A1): temp = self.bus.read_i2c_block_data(self.BACKPACK_ADDRESS, self.A1_LOW_BYTE, 2)
                elif(port == self.A2): temp = self.bus.read_i2c_block_data(self.BACKPACK_ADDRESS, self.A2_LOW_BYTE, 2)
                elif(port == self.A3): temp = self.bus.read_i2c_block_data(self.BACKPACK_ADDRESS, self.A3_LOW_BYTE, 2)
                elif(port == self.A4): temp = self.bus.read_i2c_block_data(self.BACKPACK_ADDRESS, self.A4_LOW_BYTE, 2)
                elif(port == self.A5): temp = self.bus.read_i2c_block_data(self.BACKPACK_ADDRESS, self.A5_LOW_BYTE, 2)
                elif(port == self.A6): temp = self.bus.read_i2c_block_data(self.BACKPACK_ADDRESS, self.A6_LOW_BYTE, 2)
                elif(port == self.A7): temp = self.bus.read_i2c_block_data(self.BACKPACK_ADDRESS, self.A7_LOW_BYTE, 2)
                else: return -1
                return((temp[1] << 8) | temp[0]);
            else: 
                return -1;
        except IOError: 
            print traceback.format_exc(1)
        
    def digitalRead(self, port):
        try:
            if((port & 0x0100) == 0x0000):
                data = self.bus.read_byte_data(self.BACKPACK_ADDRESS, self.DIGITAL_INPUT)
                if(data & port): return 1;
                else: return 0;
            elif ((port & 0x0100) == 0x0100):
                if (port == self.A0): temp = self.bus.read_byte_data(self.BACKPACK_ADDRESS, self.A0_HIGH_BYTE)
                elif(port == self.A1): temp = self.bus.read_byte_data(self.BACKPACK_ADDRESS, self.A1_HIGH_BYTE)
                elif(port == self.A2): temp = self.bus.read_byte_data(self.BACKPACK_ADDRESS, self.A2_HIGH_BYTE)
                elif(port == self.A3): temp = self.bus.read_byte_data(self.BACKPACK_ADDRESS, self.A3_HIGH_BYTE)
                elif(port == self.A4): temp = self.bus.read_byte_data(self.BACKPACK_ADDRESS, self.A4_HIGH_BYTE)
                elif(port == self.A5): temp = self.bus.read_byte_data(self.BACKPACK_ADDRESS, self.A5_HIGH_BYTE)
                elif(port == self.A6): temp = self.bus.read_byte_data(self.BACKPACK_ADDRESS, self.A6_HIGH_BYTE)
                elif(port == self.A7): temp = self.bus.read_byte_data(self.BACKPACK_ADDRESS, self.A7_HIGH_BYTE)
                if(temp): return 1;
                else: return 0;            
            else: 
                return 0xFF;
        except IOError:
            print traceback.format_exc(1)
    
    def digitalState(self, port, state):
        try:
            if((port & 0x0100) == 0x0000):
                data = self.bus.read_byte_data(self.BACKPACK_ADDRESS, self.DIGITAL_TRISTATE)
                if(state == 1): data |= port
                else: data &= ~port
                self.bus.write_byte_data(self.BACKPACK_ADDRESS, self.DIGITAL_TRISTATE, data)
                return;
            else: 
                return 0xFF;
        except IOError:
            print traceback.format_exc(1)

    def digitalWrite(self, port, state):
        try:
            if((port & 0x0100) == 0x0000):
                data = self.bus.read_byte_data(self.BACKPACK_ADDRESS, self.DIGITAL_OUTPUT)
                if (state == 1): data |= port
                else: data &= ~port
                self.bus.write_byte_data(self.BACKPACK_ADDRESS, self.DIGITAL_OUTPUT, data)
                return;
            else: 
                return 0xFF;
        except IOError:
            print traceback.format_exc(1)
    
    def servoEnable(self, servo, state, extended=False):
        try:
            data = self.bus.read_byte_data(self.BACKPACK_ADDRESS, self.SERVO_ENABLE)
            if (state == 1): data |= servo 
            else: data &= ~servo
            
            if(extended == False): data |= (servo << 4)
            else: data &= (~(servo << 4))
            
            try:
                self.bus.write_byte_data(self.BACKPACK_ADDRESS, self.SERVO_ENABLE, data)
            except:
                print traceback.format_exc(1)
                
            return;
        except IOError:
            print traceback.format_exc(1)
    
    def servoTarget(self, servo, target):
        try:
            temp = self.bus.read_i2c_block_data(self.BACKPACK_ADDRESS, self.SERVO_0_TARGET, 4)
            if(servo & self.S0 == self.S0): temp[0] = int(target)
            if(servo & self.S1 == self.S1): temp[1] = int(target)
            if(servo & self.S2 == self.S2): temp[2] = int(target)
            if(servo & self.S3 == self.S3): temp[3] = int(target)
            self.bus.write_i2c_block_data(self.BACKPACK_ADDRESS, self.SERVO_0_TARGET, temp)
            return;
        except IOError:
            print traceback.format_exc(1)
                
    def motorMode(self, motor, mode):
        try:
            temp = self.bus.read_i2c_block_data(self.BACKPACK_ADDRESS, self.MOTOR_0_MODE, 4)
            #time.sleep(0.001)
            if(motor & self.M0 == self.M0): temp[0] = int(mode)
            if(motor & self.M1 == self.M1): temp[3] = int(mode)
            self.bus.write_i2c_block_data(self.BACKPACK_ADDRESS, self.MOTOR_0_MODE, temp)
            #time.sleep(0.001)
            return;
        except IOError:
            print traceback.format_exc(1)
    
    def motorSpeed(self, motor, speed):
        try:
            temp = self.bus.read_i2c_block_data(self.BACKPACK_ADDRESS, self.MOTOR_0_MODE, 4)
            #time.sleep(0.001)
            if(motor & self.M0 == self.M0): temp[1] = int(speed)
            if(motor & self.M1 == self.M1): temp[2] = int(speed)
            self.bus.write_i2c_block_data(self.BACKPACK_ADDRESS, self.MOTOR_0_MODE, temp)
            #time.sleep(0.001)
            return 0xFF;
        except IOError:
            print traceback.format_exc(1)
    
    def i2cRead(self, addr, reg, len):
        try:
            while(self.bus.read_byte_data(self.BACKPACK_ADDRESS, self.I2C_FLAG) == 0xFF): pass
            time.sleep(0.001)
            temp_buf = [0x80, addr, reg, len]
            self.bus.write_i2c_block_data(self.BACKPACK_ADDRESS, self.I2C_MODE, temp_buf)
            self.bus.write_byte_data(self.BACKPACK_ADDRESS, self.I2C_FLAG, 0xFF)        
            while True:
                (temp, self.i2cError) = self.bus.read_i2c_block_data(self.BACKPACK_ADDRESS, self.I2C_FLAG, 2)
                if(temp != 0xFF): break;
            return self.bus.read_i2c_block_data(self.BACKPACK_ADDRESS, self.I2C_B0, len);       
        except IOError:
            print traceback.format_exc(1)
    
    def i2cWrite(self, addr, reg, buf):
        try:
            while(self.bus.read_byte_data(self.BACKPACK_ADDRESS, self.I2C_FLAG) == 0xFF): pass
            temp_buf = [0x00, addr, reg, len(buf)] + buf 
            self.bus.write_i2c_block_data(self.BACKPACK_ADDRESS, self.I2C_MODE, temp_buf)
            self.bus.write_byte_data(self.BACKPACK_ADDRESS, self.I2C_FLAG, 0xFF)
            self.i2cError = self.bus.read_byte_data(self.BACKPACK_ADDRESS, self.I2C_ERROR)
            return;
        except IOError:
            print traceback.format_exc(1)
        
    def readBattRaw(self):
        try:
            temp = self.bus.read_i2c_block_data(self.BACKPACK_ADDRESS, self.BATT_LOW, 2)
            return (temp[1] << 8) | temp[0];
        except IOError:
            print traceback.format_exc(1)
        
    def readBatt(self):
        try:
            temp = self.bus.read_i2c_block_data(self.BACKPACK_ADDRESS, self.BATT_LOW, 2)
            batt_temp = (temp[1] << 8) | temp[0]
            return float(str((batt_temp / 125.89))[:5]);
        except IOError:
            print traceback.format_exc(1)
        
    def setLED(self, led, value):
        if (led == self.YELLOW):
            try:
                with open("/sys/class/gpio/gpio17/value", 'wb') as f: f.write(str(value))
            except: print traceback.format_exc(1)
        elif (led == self.BLUE):
            try:
                with open("/sys/class/gpio/gpio18/value", 'wb') as f: f.write(str(value))
            except: print traceback.format_exc(1)
        else:
            return;
        return;
        
    def getI2CAddresses(self):
        try:
            addresses = []
            for i in range(255):
                self.i2cRead(i, 0x00, 1)
                if(self.i2cError == 0): addresses += [hex(i)]
            return addresses;
        except:
            print traceback.format_exc(1)
            
    def setI2CAddress(self, old, new):
        try:
            if(((new & 0x01) == 0x01) or (new < 0x10)): return;            
            self.i2cWrite(old, 0x70, [new, 0x55, 0xAA])
        except:
            print traceback.format_exc(1)
        return;
            
    def delay(self, seconds):
        time.sleep(seconds)
        return;
        
    def delay_ms(self, millis):
        time.sleep(millis/1000.0)
        return;
        
    def readEEPROM(self):
        try:
            eeprom_string = ""
        
            self.bus.write_byte_data(self.BACKPACK_ADDRESS, self.COMMAND, 0x55)
            while (self.bus.read_byte_data(self.BACKPACK_ADDRESS, self.COMMAND) == 0x55): pass 
            if(self.bus.read_byte_data(self.BACKPACK_ADDRESS, self.COMMAND) != 0x16): return -1;
            
            self.bus.write_byte_data(self.BACKPACK_ADDRESS, self.COMMAND, 0xAA)
            while (self.bus.read_byte_data(self.BACKPACK_ADDRESS, self.COMMAND) == 0xAA): pass 
            if(self.bus.read_byte_data(self.BACKPACK_ADDRESS, self.COMMAND) != 0x16): return -2;
        
            self.bus.write_byte_data(self.BACKPACK_ADDRESS, self.COMMAND, 0x0E)
            while (self.bus.read_byte_data(self.BACKPACK_ADDRESS, self.COMMAND) == 0x0E): pass 
            
            while True:
                temp_val = self.bus.read_byte_data(self.BACKPACK_ADDRESS, self.COMMAND)
                if((temp_val >= 0x20) and (temp_val <= 0x7F) or (temp_val == 0x0A)):
                    eeprom_string += chr(temp_val)
                    self.bus.write_byte_data(self.BACKPACK_ADDRESS, self.COMMAND, 0xFF)
                elif (temp_val == 0xFF): pass
                else: break;
           
            return eeprom_string;
        except IOError:
            print traceback.format_exc(1)
        
    def readVariables(self):
        try:
            variable_string = ""
        
            self.bus.write_byte_data(self.BACKPACK_ADDRESS, self.COMMAND, 0x55)
            while (self.bus.read_byte_data(self.BACKPACK_ADDRESS, self.COMMAND) == 0x55): pass 
            if(self.bus.read_byte_data(self.BACKPACK_ADDRESS, self.COMMAND) != 0x16): return -1;
            
            self.bus.write_byte_data(self.BACKPACK_ADDRESS, self.COMMAND, 0xAA)
            while (self.bus.read_byte_data(self.BACKPACK_ADDRESS, self.COMMAND) == 0xAA): pass 
            if(self.bus.read_byte_data(self.BACKPACK_ADDRESS, self.COMMAND) != 0x16): return -2;
            
            self.bus.write_byte_data(self.BACKPACK_ADDRESS, self.COMMAND, 0x0D)
            while (self.bus.read_byte_data(self.BACKPACK_ADDRESS, self.COMMAND) == 0x0D): pass 
            
            while True:
                temp_val = self.bus.read_byte_data(self.BACKPACK_ADDRESS, self.COMMAND)            
                if((temp_val >= 0x01) and (temp_val <= 0xFE)):
                    variable_string += chr(temp_val)
                    self.bus.write_byte_data(self.BACKPACK_ADDRESS, self.COMMAND, 0xFF)
                elif (temp_val == 0x00): break;
                else: pass
                
            return variable_string;
        except IOError:
            print traceback.format_exc(1)
                
    def writeEEPROM(self, new_string):        
        try:
            self.bus.write_byte_data(self.BACKPACK_ADDRESS, self.COMMAND, 0x55)
            while (self.bus.read_byte_data(self.BACKPACK_ADDRESS, self.COMMAND) == 0x55): pass 
            if(self.bus.read_byte_data(self.BACKPACK_ADDRESS, self.COMMAND) != 0x16): return -1;
            
            self.bus.write_byte_data(self.BACKPACK_ADDRESS, self.COMMAND, 0xAA)
            while (self.bus.read_byte_data(self.BACKPACK_ADDRESS, self.COMMAND) == 0xAA): pass 
            if(self.bus.read_byte_data(self.BACKPACK_ADDRESS, self.COMMAND) != 0x16): return -2;
            
            self.bus.write_byte_data(self.BACKPACK_ADDRESS, self.COMMAND, 0x0F)
            while (self.bus.read_byte_data(self.BACKPACK_ADDRESS, self.COMMAND) == 0x0F): pass 
            if(self.bus.read_byte_data(self.BACKPACK_ADDRESS, self.COMMAND) != 0xFF): return -3;
            
            for i in range(len(new_string)):
                self.bus.write_byte_data(self.BACKPACK_ADDRESS, self.COMMAND, ord(new_string[i]))
                time.sleep(0.01)
                
            self.bus.write_byte_data(self.BACKPACK_ADDRESS, self.COMMAND, 0x00)
            
            return 0;
        except IOError:
            print traceback.format_exc(1)
        
    def reloadEEPROM(self):
        try:
            self.bus.write_byte_data(self.BACKPACK_ADDRESS, self.COMMAND, 0x55)
            while (self.bus.read_byte_data(self.BACKPACK_ADDRESS, self.COMMAND) == 0x55): pass 
            if(self.bus.read_byte_data(self.BACKPACK_ADDRESS, self.COMMAND) != 0x16): return -1;
            
            self.bus.write_byte_data(self.BACKPACK_ADDRESS, self.COMMAND, 0xAA)
            while (self.bus.read_byte_data(self.BACKPACK_ADDRESS, self.COMMAND) == 0xAA): pass 
            if(self.bus.read_byte_data(self.BACKPACK_ADDRESS, self.COMMAND) != 0x16): return -2;
            
            self.bus.write_byte_data(self.BACKPACK_ADDRESS, self.COMMAND, 0x05)
            while (self.bus.read_byte_data(self.BACKPACK_ADDRESS, self.COMMAND) == 0x05): pass 
            if(self.bus.read_byte_data(self.BACKPACK_ADDRESS, self.COMMAND) != 0x00): return -3;
            
            return 0;
        except IOError:
            print traceback.format_exc(1)
        
    def defaultEEPROM(self):
        try:
            self.bus.write_byte_data(self.BACKPACK_ADDRESS, self.COMMAND, 0x55)
            while (self.bus.read_byte_data(self.BACKPACK_ADDRESS, self.COMMAND) == 0x55): pass 
            if(self.bus.read_byte_data(self.BACKPACK_ADDRESS, self.COMMAND) != 0x16): return -1;
            print self.bus.read_byte_data(self.BACKPACK_ADDRESS, self.COMMAND)
            
            self.bus.write_byte_data(self.BACKPACK_ADDRESS, self.COMMAND, 0xAA)
            while (self.bus.read_byte_data(self.BACKPACK_ADDRESS, self.COMMAND) == 0xAA): pass 
            if(self.bus.read_byte_data(self.BACKPACK_ADDRESS, self.COMMAND) != 0x16): return -2;
            print self.bus.read_byte_data(self.BACKPACK_ADDRESS, self.COMMAND)
            
            self.bus.write_byte_data(self.BACKPACK_ADDRESS, self.COMMAND, 0x06)
            while (self.bus.read_byte_data(self.BACKPACK_ADDRESS, self.COMMAND) == 0x06): pass 
            if(self.bus.read_byte_data(self.BACKPACK_ADDRESS, self.COMMAND) != 0x00): return -3;
            print self.bus.read_byte_data(self.BACKPACK_ADDRESS, self.COMMAND)
            
            return 0;
        except IOError:
            print traceback.format_exc(1)
    
    def cleanUp(self):
        try: 
            for i in range(0x40): self.bus.write_byte_data(self.BACKPACK_ADDRESS, i, 0x00)
        except: print traceback.format_exc(1)        
        try: 
            for i in range(0x40): self.bus.write_byte_data(self.BACKPACK_ADDRESS, i, 0x00)
        except: print traceback.format_exc(1)        
        try: 
            for i in range(0x40): self.bus.write_byte_data(self.BACKPACK_ADDRESS, i, 0x00)
        except: print traceback.format_exc(1)        
        try: 
            with open("/sys/class/gpio/unexport", 'wb') as f: f.write("17")
        except: print traceback.format_exc(1)        
        try: 
            with open("/sys/class/gpio/unexport", 'wb') as f: f.write("18")
        except: print traceback.format_exc(1)     

    def getPowerState(self):
        try:
            return self.bus.read_byte_data(self.BACKPACK_ADDRESS, self.POWER_STATE)
        except IOError:
            print traceback.format_exc(1)
        
    def readTest(self):
        try: 
            return self.bus.read_i2c_block_data(self.BACKPACK_ADDRESS, self.TEST_0, 5)
        except IOError:
            print traceback.format_exc(1)
