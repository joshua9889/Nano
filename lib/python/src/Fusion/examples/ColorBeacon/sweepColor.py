'''
sweepColor.py - Color sweep example for use with the MRI ColorBeacon
    (c) Modern Robotics Inc. 2017  http://www.modernroboticsinc.com

Description:
    The following example sweeps through the RGB channels as an 8 bit
    value. 
    
Connections:
    MRI Color Beacon        = I2C  
'''

import Fusion

# Class definitions -----------------------------------------------------------
f = Fusion.driver()
c = Fusion.colorBeacon(f)

# Constants/Variables ---------------------------------------------------------
time_delay = 1          # Time delay between loop cycles in milliseconds

# Program Start ---------------------------------------------------------------
while True:
    for i in range(255):                        # RED(0->255) GREEN(0) BLUE(0)
        c.setCustomColor(i, 0, 0)
        f.delay_ms(time_delay)
    
    for i in range(255):                        # RED(255->0) GREEN(0->255) BLUE(0)
        c.setCustomColor(255-i, i, 0)   
        f.delay_ms(time_delay)

    for i in range(255):                        # RED(0->255) GREEN(255) BLUE(0)
        c.setCustomColor(i, 255, 0)
        f.delay_ms(time_delay)
    
    for i in range(255):                        # RED(255->0) GREEN(255->0) BLUE(0->255)
        c.setCustomColor(255-i, 255-i, i)   
        f.delay_ms(time_delay)
        
    for i in range(255):                        # RED(0->255) GREEN(0) BLUE(255)
        c.setCustomColor(i, 0, 255)
        f.delay_ms(time_delay)
    
    for i in range(255):                        # RED(255->0) GREEN(0->255) BLUE(255)
        c.setCustomColor(255-i, i, 255)
        f.delay_ms(time_delay)

    for i in range(255):                        # RED(0->255) GREEN(255) BLUE(255)
        c.setCustomColor(i, 255, 255)
        f.delay_ms(time_delay)
    
    for i in range(255):                        # RED(255->0) GREEN(255->0) BLUE(255->0)
        c.setCustomColor(255-i, 255-i, 255-i)
        f.delay_ms(time_delay)