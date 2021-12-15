'''
analogRead.py - Analog input example for use with the Fusion Control System
    (c) Modern Robotics Inc. 2017  http://www.modernroboticsinc.com

Description:
    The following example uses the low level analogRead function to return 
    the value of an analog device connected to port A0.
    
Connections:
    Analog Device   = A0
'''

import Fusion

# Class definitions -----------------------------------------------------------
f = Fusion.driver()

# Program Start ---------------------------------------------------------------
while True:
    print f.analogRead(f.A0)        # Read the analog value on A0
    f.delay(0.01)                   # Delay 10ms (0.01 Seconds)