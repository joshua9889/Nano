'''
ledBlink.py - Onboard LED example for use with the Fusion Control System
    (c) Modern Robotics Inc. 2017  http://www.modernroboticsinc.com

Description:
    The following example toggles the onboard Yellow and Blue LEDs
    in 0.5 second intervals. 
    
Connections:
    None    
'''

import Fusion

# Class definitions -----------------------------------------------------------
f = Fusion.driver()

# Program Start ---------------------------------------------------------------
while True:
    f.setLED(f.BLUE, 1)         # Blue LED = On
    f.setLED(f.YELLOW, 0)       # Yellow LED = Off
    f.delay(0.5)                # Wait 500ms
    
    f.setLED(f.BLUE, 0)         # Blue LED = Off 
    f.setLED(f.YELLOW, 1)       # Yellow LED = On
    f.delay(0.5)                # Wait 500ms