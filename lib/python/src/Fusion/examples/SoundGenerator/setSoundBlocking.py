'''
setSoundBlocking.py - Sound Generator extended beep example. 
    (c) Modern Robotics Inc. 2017  http://www.modernroboticsinc.com

Description:
    The following example uses the setSoundBlocking function to emit a sound
    with a duration up to or more than then 2550ms (2.5s) limit. This funtion
    however is "Blocking" meaning that the user program will not continue untill
    the function has completed its beep duration. This is useful when creating 
    melodys as the next beep will not begin untill the last has finished. 
    
Connections:
    MRI Sound Generator             = I2C 
    MRI Touch Sensor                = D0
'''

import Fusion

# Class definitions -----------------------------------------------------------
f = Fusion.driver()
beep = Fusion.sound(f)
touch = Fusion.digital(f, f.D0)

# Program Start ---------------------------------------------------------------
while True:
    f.setLED(f.BLUE, 0)                             # Blue = Off    Yellow = On
    f.setLED(f.YELLOW, 1)
    
    while touch.read() == 0: pass                   # Wait for the button to be pressed 
    while touch.read() == 1: pass                   # and released.
    
    f.setLED(f.BLUE, 1)                             # Blue = On     Yellow = Off
    f.setLED(f.YELLOW, 0)
    
    beep.setSoundBlocking(beep.LOW, 2000, 3000)     # Sound level Low, 2000Hz, 3000mS duration
    
   