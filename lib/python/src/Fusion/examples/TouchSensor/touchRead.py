'''
touchRead.py - Touch sensor example for use with the Fusion Control System
    (c) Modern Robotics Inc. 2017  http://www.modernroboticsinc.com

Description:
    The following example uses the digtial wrapper library to read 
    an MRI Touch sensor connected to port D0.
    
Connections:
    MRI Touch Sensor            = D0
'''

import Fusion

# Class definitions -----------------------------------------------------------
f = Fusion.driver()
touch = Fusion.digital(f, f.D0)

# Program Start ---------------------------------------------------------------
while True:
    print "TOUCH = " + str(touch.read())    # Print the value of the touch sensor
    f.delay_ms(10)                          # Delay 10ms