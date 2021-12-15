'''
i2cAddresses.py - Show the address of all devices connected 
    (c) Modern Robotics Inc. 2017  http://www.modernroboticsinc.com

Description:
    The following example uses the built in function getI2CAddresses
    to pull the address of all the currently connected devices
    on the Core Device Interface I2C bus. 
    
Connections:
    I2C Device          = I2C     
'''

import CoreControl
import time 

# Class definitions -----------------------------------------------------------
c = CoreControl.driver()
cdi = CoreControl.coreDeviceInterface(c, 'A900VGFC')

# Program Start ---------------------------------------------------------------
print "Reading addresses..."
print cdi.getI2CAddresses()   # Return and print a list of all addresses found