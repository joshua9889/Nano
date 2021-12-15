'''
detectDevices.py - Detect Core modules connected to the Fusion Controller
    (c) Modern Robotics Inc. 2018 http://www.modernroboticsinc.com

Description:
    The following example scans the USB bus for FTDI enabled devices and 
    determines if they are valid core modules. This will then display the
    device type and FTDI serial number for each to be used in addressing 
    the module within a user program. 
    
Connections:
    Core Module               = USB Port
    
'''

import CoreControl

# Class definitions
c = CoreControl.driver()

# Print to the console all detected devices and their information
c.printDevices()