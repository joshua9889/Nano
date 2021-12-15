'''
calibrateAccelerometer.py - Calibrate the accelerometer axes
    (c) Modern Robotics Inc. 2017  http://www.modernroboticsinc.com

Description:
    Use the following example to null/calibrate the three axis
    of the Compass/Accelerometer combo board. 
    
Connections:
    Touch Sensor        - D0
    Compass Sensor      - I2C
'''

import Fusion

# Class definitions -----------------------------------------------------------
f = Fusion.driver()
touch = Fusion.digital(f, f.D0)
comp = Fusion.compass(f)

# Program Start ---------------------------------------------------------------
print "\n---------- Accelerometer Calibration ----------" 
print "Step 1:"
print "Lay the sensor perfectly flat and push the touch"
print "sensor button to calibrate the X and Y values"
while (touch.read() == 0): pass 
while (touch.read() == 1): pass 
comp.nullAccelerometer('X')
comp.nullAccelerometer('Y')

print "\nStep 2:"
print "Set the sensor completely vertical and push the"
print "touch sensor button to calibrate the Z value"
while (touch.read() == 0): pass 
while (touch.read() == 1): pass 
comp.nullAccelerometer('Z')

print "\nDone!\n"