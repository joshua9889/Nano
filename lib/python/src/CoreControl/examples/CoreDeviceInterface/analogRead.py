'''
analogRead.py - Analog input example for use with the Core Device Interface
    (c) Modern Robotics Inc. 2018 http://www.modernroboticsinc.com

Description:
    The following example uses the low level analogRead function to return 
    the value of an analog device connected to port A0.
    
Connections:
    Analog Device   = A0
'''

import CoreControl
import time 

# Class definitions -----------------------------------------------------------
c = CoreControl.driver()
cdi = CoreControl.coreDeviceInterface(c, 'A900VGFC')

# Program Start ---------------------------------------------------------------
while True:
    print cdi.analogRead(cdi.A0)        # Read the analog value on A0
    time.sleep(0.01)                    # Delay 10ms (0.01 Seconds)