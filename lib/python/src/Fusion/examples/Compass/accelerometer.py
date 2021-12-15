'''
accelerometer.py - Read the accelerometer on the MRI compass sensor
    (c) Modern Robotics Inc. 2017  http://www.modernroboticsinc.com

Description:
    The following example reads and returns the value of the three 
    accelerometer axes.
    
Connections:
    Compass Sensor      - I2C
'''

import Fusion

# Class definitions -----------------------------------------------------------
f = Fusion.driver()
comp = Fusion.compass(f)

# Program Start ---------------------------------------------------------------
while True:
    accel = comp.getAccelerometer() 
    print "X = " + str(accel[0]) + "     Y = " + str(accel[1]) + "     Z = " + str(accel[2])
    f.delay(0.1)