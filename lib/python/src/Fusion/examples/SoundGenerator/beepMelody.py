'''
beepMelody.py - Melody example using the Sound Generator 
    (c) Modern Robotics Inc. 2017  http://www.modernroboticsinc.com

Description:
    The following example shows how a melody can be made using the 
    Sound Generator and the setSoundBlocking function. 
    
    Can you guess what the melody is :)
    
    Note:
        The function setSoundBlocking has a "post_pause" field which places 
        a time delay of the indicated number of milliseconds after the sound
        has finished playing. This is so subsequent calls to setSoundBlocking
        can be made without manually placing delays between notes useful
        when creating tunes. 
    
Connections:
    MRI Sound Generator             = I2C 
    MRI Touch Sensor                = D0
'''

import Fusion

f = Fusion.driver()
beep = Fusion.sound(f)
touch = Fusion.digital(f, f.D0)

# Volume of beeps -----------------------------------------
volume = beep.MED

# Pause between notes -------------------------------------
post_pause = 0.01

# Note Frequency ------------------------------------------
E = 1319
D = 1175
C = 1047
G = 1568

# ---------------------------------------------------------
print "Press the Touch Sensor button to begin..."
while True:
    while touch.read() == 0: pass                       # Wait for the button to be pressed
    while touch.read() == 1: pass                       # and released.
    
    beep.setSoundBlocking(volume, E, 300, post_pause)    
    beep.setSoundBlocking(volume, D, 300, post_pause)    
    beep.setSoundBlocking(volume, C, 300, post_pause)    
    beep.setSoundBlocking(volume, D, 300, post_pause)       
    beep.setSoundBlocking(volume, E, 300, post_pause)       
    beep.setSoundBlocking(volume, E, 300, post_pause)
    beep.setSoundBlocking(volume, E, 600, post_pause)
        
    beep.setSoundBlocking(volume, D, 300, post_pause)    
    beep.setSoundBlocking(volume, D, 300, post_pause)    
    beep.setSoundBlocking(volume, D, 600, post_pause)
    
    beep.setSoundBlocking(volume, E, 300, post_pause)   
    beep.setSoundBlocking(volume, G, 300, post_pause)      
    beep.setSoundBlocking(volume, G, 600, post_pause)
    
    beep.setSoundBlocking(volume, E, 300, post_pause)    
    beep.setSoundBlocking(volume, D, 300, post_pause)    
    beep.setSoundBlocking(volume, C, 300, post_pause)    
    beep.setSoundBlocking(volume, D, 300, post_pause)    
    beep.setSoundBlocking(volume, E, 300, post_pause)   
    beep.setSoundBlocking(volume, E, 300, post_pause)   
    beep.setSoundBlocking(volume, E, 300, post_pause)   
    beep.setSoundBlocking(volume, E, 300, post_pause)   
    beep.setSoundBlocking(volume, D, 300, post_pause)   
    beep.setSoundBlocking(volume, D, 300, post_pause)   
    beep.setSoundBlocking(volume, E, 300, post_pause)   
    beep.setSoundBlocking(volume, D, 300, post_pause)   
    beep.setSoundBlocking(volume, C, 1000, post_pause)   