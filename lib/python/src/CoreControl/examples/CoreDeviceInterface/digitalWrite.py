'''
digitalWrite.py - Digital output example for use with the Core Device Interface
    (c) Modern Robotics Inc. 2018 http://www.modernroboticsinc.com

Description:
    The following example uses the low level digitalWrite function to toggle the 
    output of port D7 in 1 second intervals. 
    
Connections:
    Digital Device   = D0    
'''

import CoreControl
import time 

# Class definitions -----------------------------------------------------------
c = CoreControl.driver()
cdi = CoreControl.coreDeviceInterface(c, 'A900VGFC')

# Program Start ---------------------------------------------------------------
cdi.digitalState(cdi.D0, cdi.OUTPUT)    # Set D0 to be an output

while True:
    cdi.digitalWrite(cdi.D0, 1)         # Set D0 high
    time.sleep(1)                       # Wait 1 second
    cdi.digitalWrite(cdi.D0, 0)         # Set D0 low 
    time.sleep(1)                       # Wait 1 second