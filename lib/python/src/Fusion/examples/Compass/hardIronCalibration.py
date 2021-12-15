'''
hardIronCalibration.py - Perform hard iron calibration for compass sensor
    (c) Modern Robotics Inc. 2017  http://www.modernroboticsinc.com
    
Description:
    Use the following example to perform the hard iron calibration
    for the compass sensor element. After pressing the Touch Sensor
    button, the device must be rotate a minimum of 360 degrees 
    within the 5 second delay. 
    
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
print "\n---------- Hard Iron Calibration ----------" 
print "Step 1:"
print "Lay the sensor perfectly flat and push the Touch"
print "Sensor button, rotate the device a minimum of 360"
print "degrees before the 5 second timeout expires...\n"
while (touch.read() == 0): pass 
while (touch.read() == 1): pass 
print 
print "START: Rotate compass sensor a minimum of 360 degrees..."
print 
if(comp.hardIronCalibration() != 0): 
    print "HARD IRON CALIBRATION FAILED!..."
    print "Ensure device is rotated a minimum of 360"
    print "degrees after pressing the touch sensor button."
else:
    print "SUCCESS!\n"