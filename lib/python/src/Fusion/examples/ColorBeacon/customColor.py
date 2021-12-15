'''
customColor.py - Set the Color Beacon to a custom 8-bit RGB color.
    (c) Modern Robotics Inc. 2017  http://www.modernroboticsinc.com

Description:
    The following example sets the Color Beacon to the custom 8-bit
    color indicated for a duration of 2 seconds. 
    
Connections:
    MRI Color Beacon        = I2C  
'''

import Fusion

# Class definitions -----------------------------------------------------------
f = Fusion.driver()
c = Fusion.colorBeacon(f)

# Constants/Variables ---------------------------------------------------------
red     = 220                       # Red value
green   = 43                        # Green value
blue    = 180                       # Blue value

# Program Start ---------------------------------------------------------------
c.setCustomColor(red, green, blue)  # Set the custom color value
f.delay(2)                          # Delay for 2 seconds
