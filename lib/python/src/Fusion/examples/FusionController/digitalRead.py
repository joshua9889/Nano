'''
digitalRead.py - Digital input example for use with the Fusion Control System
    (c) Modern Robotics Inc. 2017  http://www.modernroboticsinc.com

Description:
    The following example uses the low level digitalRead function to return
    the value of a digital device connected to port D0.
    
Connections:
    Digital Device   = D0   
'''

import Fusion 

# Class definitions -----------------------------------------------------------
f = Fusion.driver()

# Program Start ---------------------------------------------------------------
f.digitalState(f.D0, f.INPUT)       # Set D0 to be an input

while True:
    print f.digitalRead(f.D0)       # Read the value on port D0
    f.delay(0.01)                   # Delay 10ms