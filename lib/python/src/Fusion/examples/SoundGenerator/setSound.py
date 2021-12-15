'''
setSound.py - Sound Generator beep example. 
    (c) Modern Robotics Inc. 2017  http://www.modernroboticsinc.com

Description:
    The following example uses the setSound function to emit a sound
    at a duration of up to (2550 ms). This begins an internal countdown
    timer within the sound generator at which the sound will stop when 
    the timer has expired. The function exits as soon as the sound begins,
    allowing the user program to continue without waiting for the sound to
    stop first. 
    
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
    while touch.read() == 0: pass           # Wait for the button to be pressed 
    while touch.read() == 1: pass           # and released.
    
    beep.setSound(beep.LOW, 2000, 1000)     # Sound level Low, 2000Hz, 1000mS duration
    
    while (beep.getDuration() != 0):        # Wait for the internal counter to expire
        f.setLED(f.BLUE, 1)                 # Blink the Blue LED indicating user 
        f.delay_ms(100)                     # program has continued and stop when the
        f.setLED(f.BLUE, 0)                 # internal duration counter has expired. 
        f.delay_ms(100)