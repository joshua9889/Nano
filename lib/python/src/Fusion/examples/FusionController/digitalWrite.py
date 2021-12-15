'''
digitalWrite.py - Digital output example for use with the Fusion Control System
    (c) Modern Robotics Inc. 2017  http://www.modernroboticsinc.com

Description:
    The following example uses the low level digitalWrite function to toggle the 
    output of port D7 in 1 second intervals. 
    
Connections:
    Digital Device   = D0    
'''

import Fusion 

# Class definitions -----------------------------------------------------------
f = Fusion.driver()

# Program Start ---------------------------------------------------------------
f.digitalState(f.D0, f.OUTPUT)  # Set D0 to be an output

while True:
    f.digitalWrite(f.D0, 1)     # Set D0 high
    f.delay(1)                  # Wait 1 second
    f.digitalWrite(f.D0, 0)     # Set D0 low 
    f.delay(1)                  # Wait 1 second