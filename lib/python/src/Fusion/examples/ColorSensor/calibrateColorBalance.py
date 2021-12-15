'''
calibrateColorBalance.py - Calibration procedure for MRI Color Sensor with Fusion Control System
    (c) Modern Robotics Inc. 2017  http://www.modernroboticsinc.com

Description:
    Use the following example to calibrate the black and white balance of the Color Sensor 
    accordingly.
    
Connections:
    Touch Sensor            = D0
    Color Sensor            = I2C
'''

import Fusion

# Class definitions -----------------------------------------------------------
f = Fusion.driver()
t = Fusion.digital(f, f.D0)
c = Fusion.color(f)

# Program Start ---------------------------------------------------------------
# Set the color sensor to active mode for calibration
c.colorSetup(c.ACTIVE, c.SIXTY_HZ)

# Calibrate the black balance value
print "\nStep 1:\nHold the sensor pointing to empty space and"
print "press the TOUCH sensor to calibrate Black Balance"
while (t.read() == 0): pass 
while (t.read() == 1): pass 
c.blackBalance()
print "Calibrating..."
f.delay(1)

# Calibrate the white balance value
print "\nStep 2:\nHold the sensor approximately 2 inches away from white target"
print "and press the TOUCH sensor to calibrate White Balance"
while (t.read() == 0): pass 
while (t.read() == 1): pass 
c.whiteBalance()
print "Calibrating..."
f.delay(1)

print "\nDone!\nThe COLOR sensor can now be used to read color values"
print "using examples or user generated code.\n"