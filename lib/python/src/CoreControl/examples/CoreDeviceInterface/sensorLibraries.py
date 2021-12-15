'''
sensorLibraries.py - Using Fusion sensor libraries with the Core Device Interface.
    (c) Modern Robotics Inc. 2018 http://www.modernroboticsinc.com

Description:
    The following example shows how to use the sensor libraries developed for the 
    Fusion control system with the Core Device Interface. Each libary for the sensor
    requires a driver object to be created before hand. The low-level api is the 
    same between these so that the library can be used with both devices. 
    
Connections:
    Color Beacon   = I2C
'''

import CoreControl
import time 

# Class definitions -----------------------------------------------------------
c = CoreControl.driver()
cdi = CoreControl.coreDeviceInterface(c, 'A900VGFC')

# Create the color beacon object, passing cdi driver object
beacon = cdi.colorBeacon()

# Program Start ---------------------------------------------------------------
while True:
    beacon.setColor(beacon.RED)
    time.sleep(1)
    beacon.setColor(beacon.GREEN)
    time.sleep(1)
    beacon.setColor(beacon.BLUE)
    time.sleep(1)