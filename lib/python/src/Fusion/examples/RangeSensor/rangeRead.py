'''
rangeRead.py - Read the ultrasonic and optical values of a Range Sensor
    (c) Modern Robotics Inc. 2017  http://www.modernroboticsinc.com

Description:
    The following example reads and prints the current ultrasonic and 
    optical readings of the connected Range Sensor and prints them to 
    the console in 10ms increments. 
    
Connections:
    MRI Range Sensor            = I2C
'''

import Fusion

# Class definitions -----------------------------------------------------------
f = Fusion.driver()
r = Fusion.range(f)

# Program Start ---------------------------------------------------------------
while True:
    print "Ultrasonic = " + str(r.ultrasonic()) + "     ODS = " + str(r.optical())
    f.delay(0.01)