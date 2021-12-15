'''
motorTest.py - Motor example for use with the Fusion Control System
    (c) Modern Robotics Inc. 2017  http://www.modernroboticsinc.com

Description:
    The following example drives both motors at 50% power in forward 
    and reverse one at a time in 1 second intervals. The use of the 
    MRI 6.0v NIMH battery pack is required in order to drive the DC 
    motor ports. 
    
Connections:
    MRI 6.0v NIMH Battery    = Battery Port
    Right Motor              = M0 (+/-)
    Left Motor               = M1 (-/+)
'''

import Fusion

# Class definitions -----------------------------------------------------------
f = Fusion.driver()

# Constants/Variables ---------------------------------------------------------
speed = 50                          # Speed at which the motors will turn
delay = 1.0                         # Delay between changing directions in seconds

# Program Start ---------------------------------------------------------------
while True:
    f.motorSpeed(f.M1, speed)       # Set M1 to the desired speed
    f.motorSpeed(f.M0, 0)           # M0 = Off
    f.delay(delay)                  # Delay the specified amount of time 
    
    f.motorSpeed(f.M1, -speed)      # Set M1 to the desired reverse speed
    f.motorSpeed(f.M0, 0)           # M0 = Off
    f.delay(delay)                  # Delay the specified amount of time 
    
    f.motorSpeed(f.M1, 0)           # M1 = Off
    f.motorSpeed(f.M0, speed)       # Set M0 to the desired speed
    f.delay(delay)                  # Delay the specified amount of time 
    
    f.motorSpeed(f.M1, 0)           # M1 = Off 
    f.motorSpeed(f.M0, -speed)      # Set M0 to the desired reverse speed 
    f.delay(delay)                  # Delay the specified amount of time 
    