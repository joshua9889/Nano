'''
i2cReadWrite.py - I2C example for use with the Core Device Interface
    (c) Modern Robotics Inc. 2018  http://www.modernroboticsinc.com

Description:
    The following example reads, increments, and writes to the 
    specified register location of the the device at the specified address. 
    
    For the purpose of this example a MRI ColorBeacon will be used. 
    The register 0x04, which is the color register, will be incremented 
    every 0.5 seconds untill it exceeds the valid range of 0-7. Once it 
    exceeds this range the value is reset back to zero and the cycle 
    begins again. 
    
Connections:
    I2C Device (MRI ColorBeaon)         = I2C 
'''

import CoreControl
import time 

# Class definitions -----------------------------------------------------------
c = CoreControl.driver()
cdi = CoreControl.coreDeviceInterface(c, 'A900VGFC')

# Constants/Variables ---------------------------------------------------------
address     = 0x4C                              # Address for the MRI ColorBeacon
register    = 0x04                              # "SetColor" register

# Program Start ---------------------------------------------------------------
try:
    while True:
        temp = cdi.i2cRead(address, register, 1)    # Read one byte from the device (returns a list of length 1)
        print temp[0]                               # Print the value in temp at list index 0
        temp[0] += 1                                # Increment the value returned from the device
        if(temp[0] > 7): temp[0] = 0                # If the value is greater than 7, reset back to 0
        cdi.i2cWrite(address, register, temp)       # Write the value back to the device
        time.sleep(0.5)                          # Delay 500ms
        
except:
    cdi.i2cWrite(address, register, [0x00])           # Write 0x00 to the register to turn off the LED
                                                    # at program exit.