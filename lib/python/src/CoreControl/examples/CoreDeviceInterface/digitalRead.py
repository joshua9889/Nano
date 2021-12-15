'''
digitalRead.py - Digital input example for use with the Core Device Interface
    (c) Modern Robotics Inc. 2018  http://www.modernroboticsinc.com

Description:
    The following example uses the low level digitalRead function to return
    the value of a digital device connected to port D0.
    
Connections:
    Digital Device   = D0   
'''

import CoreControl
import time 

# Class definitions -----------------------------------------------------------
c = CoreControl.driver()
cdi = CoreControl.coreDeviceInterface(c, 'A900VGFC')

# Program Start ---------------------------------------------------------------
cdi.digitalState(cdi.D0, cdi.INPUT)     # Set D0 to be an input

while True:
    print cdi.digitalRead(cdi.D0)       # Read the value on port D0
    time.sleep(0.01)                    # Delay 10ms