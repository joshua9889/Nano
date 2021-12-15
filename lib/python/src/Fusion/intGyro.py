#===============================================================================
# intGyro.py - Integrating Gyro sensor class for the Fusion system
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
# 26-Mar-20 <jwa> - Updated function calls to prevent issues seen with new
#		color sensor driver functions.  
# 02-Oct-19 <jwa> - Updated from the original version to correct 2's Compliment
#       conversions resulting in off-by-one errors for all negative numbers;
#       Restructured and added comments.
#
#===============================================================================

class intGyro:
    obj = None 
    addr = None 
    
    def __init__(self, main_obj, i2c_addr=0x20):
        self.obj = main_obj
        self.addr = i2c_addr
        
        
#---[ setNull - Clears and recalibrates the Gyro ]---
#
    def setNull(self):
        self.obj.i2cWrite(self.addr, 0x03, [0x4E])
        while (self.obj.i2cRead(self.addr, 0x03, 1)[0] != 0): pass 
        return;
 
 
#---[ setZero - Resets the heading to Zero w/o recalibrating ]---
#
    def setZero(self):
        self.obj.i2cWrite(self.addr, 0x03, [0x52])
        while (self.obj.i2cRead(self.addr, 0x03, 1)[0] != 0): pass 
        return;


#---[ getDegrees - Returns the Heading Data (0-359 degrees)  ]---
#   Value is range checked to be between 0 and 359. If bad, it takes another
#   reading...
#
    def getDegrees(self):
        DataOK = False
        while (DataOK == False):
            data = self.obj.i2cRead(self.addr, 0x04, 2) 
            heading = ((data[1] << 8) | data[0]);
            if ( (heading >= 0) and (heading <= 359) ):
                DataOK = True
        
        return heading
        
    
#---[ getAbsolute - Returns the cumulative Z-Axis rotating data ]---
#   Value from Gyro is 16-bit 2's Complement value. It is converted to a signed
#   integer for return to the caller.
#
    def getAbsolute(self):
        data = self.obj.i2cRead(self.addr, 0x06, 2)
        temp = ((data[1] << 8) | data[0]);
        
        if(temp > 32767): temp -= 65536
        return temp;
 
 
#---[ getAxis - Returns the cumulative Axis rotational data ]---
#   Value from Gyro is 16-bit 2's Complement value. It is converted to a signed
#   integer for return to the caller.
#   Function accepts X, Y, and Z as argument to return the given axis
#
    def getAxis(self, axis):
        
        if (axis == 'X'):  data = self.obj.i2cRead(self.addr, 0x08, 2)
        elif(axis == 'Y'): data = self.obj.i2cRead(self.addr, 0x0A, 2)
        elif(axis == 'Z'): data = self.obj.i2cRead(self.addr, 0x0C, 2)
        else: return -1
        temp = ((data[1] << 8) | data[0])
        
        if(temp > 32767): temp -= 65536
        return temp;
 
 
#---[ setScale - Allows the Z-Axis scale factor to be adjusted ]---
#
    def setScale(self, value):
        data = [0, 0]
        
        data[1] = int(value)
        data[0] = (value - int(value)) * 256
                
        self.obj.i2cWrite(self.addr, 0x10, data)
        self.setNull()
        return;

