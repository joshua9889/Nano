'''
tiltCalibration.py - Perform tilt calibration for the compass element
    (c) Modern Robotics Inc. 2017  http://www.modernroboticsinc.com

Description:
    The following example performs the tilt calibration of the compass
    element.
    
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
print "\n---------- Tilt Calibration ----------" 
print "Step 1:"
print "Tilt the sensor upwards at an angle of 20"
print "degrees and push the touch sensor button"
print "to calibrate."
while (touch.read() == 0): pass 
while (touch.read() == 1): pass 
comp.tiltUp()

print "\nStep 2:"
print "Tilt the sensor downwards at an angle of 20"
print "degrees and push the touch sensor button"
print "to calibrate."
while (touch.read() == 0): pass 
while (touch.read() == 1): pass 
comp.tiltDown()

print "\nDone!..."
