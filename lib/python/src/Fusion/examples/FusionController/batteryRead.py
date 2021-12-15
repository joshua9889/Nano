'''
batteryRead.py - Read the battery voltage on the Fusion Control System
    (c) Modern Robotics Inc. 2017  http://www.modernroboticsinc.com

Description:
    The following example uses the readBattRaw and readBatt function 
    to return the current value of the MRI 6.0v NIMH battery pack connected
    to the Fusion controller. 
    
Connections:
    MRI 6.0v NIMH Battery    = Battery Port    
'''

import Fusion 

# Class definitions -----------------------------------------------------------
f = Fusion.driver()

# Program Start ---------------------------------------------------------------
volts = f.readBatt()                    # Read the battery voltage as a float
raw = f.readBattRaw()                   # Reads the raw A/D value of the device

print "Raw value = " + str(raw)         # Convert to string and print the raw A/D value
print "Voltage   = " + str(volts) + "v" # Convert to string and print the battery voltage