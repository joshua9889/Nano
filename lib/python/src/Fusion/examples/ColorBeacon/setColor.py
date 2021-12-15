'''
setColor.py - Set the Color Beacon to a fixed color.
    (c) Modern Robotics Inc. 2017  http://www.modernroboticsinc.com

Description:
    The following example cycles through the available colors of the 
    MRI ColorBeacon. The first instance cycles through based on the 
    class name for the specific color while the second shows that the 
    color can also be set by a number 0-7 accordingly. 
    
Connections:
    MRI Color Beacon        = I2C  
'''

import Fusion

# Class definitions -----------------------------------------------------------
f = Fusion.driver()
c = Fusion.colorBeacon(f)

# Program Start ---------------------------------------------------------------
while True: 
    c.setColor(c.WHITE)     # Set the color to WHITE
    f.delay(0.25)           # Delay 250ms
    
    c.setColor(c.TEAL)      # Set the color to TEAL
    f.delay(0.25)           # Delay 250ms
    
    c.setColor(c.PURPLE)    # Set the color to PURPLE
    f.delay(0.25)           # Delay 250ms
    
    c.setColor(c.BLUE)      # Set the color to BLUE
    f.delay(0.25)           # Delay 250ms
    
    c.setColor(c.YELLOW)    # Set the color to YELLOW
    f.delay(0.25)           # Delay 250ms
    
    c.setColor(c.GREEN)     # Set the color to GREEN
    f.delay(0.25)           # Delay 250ms
    
    c.setColor(c.RED)       # Set the color to RED
    f.delay(0.25)           # Delay 250ms
    
    c.setColor(c.OFF)       # Turn the beacon off 
    f.delay(0.25)           # Delay 250ms
    
    for i in range(0, 8):   # Run 8 cycles with values from 0-7
        c.setColor(i)       # Set the color as the current cycle number
        f.delay(0.25)       # Delay 250ms (0.25 seconds)
    
    