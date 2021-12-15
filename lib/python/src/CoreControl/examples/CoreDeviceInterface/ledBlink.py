'''
ledBlink.py - Onboard LED example for use with the Core Device Interface
    (c) Modern Robotics Inc. 2017  http://www.modernroboticsinc.com

Description:
    The following example toggles the onboard Red and Blue LEDs
    in 0.5 second intervals. 
    
Connections:
    None    
'''

import CoreControl
import time 

# Class definitions -----------------------------------------------------------
c = CoreControl.driver()
cdi = CoreControl.coreDeviceInterface(c, 'A900VGFC')

# Program Start ---------------------------------------------------------------
while True:
    cdi.setLED(cdi.BLUE, 1)         # Blue LED = On
    cdi.setLED(cdi.RED, 0)          # Yellow LED = Off
    time.sleep(0.5)                 # Wait 500ms
    
    cdi.setLED(cdi.BLUE, 0)         # Blue LED = Off 
    cdi.setLED(cdi.RED, 1)          # Yellow LED = On
    time.sleep(0.5)                 # Wait 500ms