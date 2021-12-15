'''
lightRead.py - Read the analog value of a Light Sensor
    (c) Modern Robotics Inc. 2017  http://www.modernroboticsinc.com

Description:
    The following example uses the analog wrapper library to attach
    a name to a MRI Ambient Light sensor on the specified port and 
    read its analog value. 
    
Connections:
    MRI Light Sensor            = A0 
'''

import Fusion

# Class definitions -----------------------------------------------------------
f = Fusion.driver()
light = Fusion.analog(f, f.A0)

# Program Start ---------------------------------------------------------------
while True:
    print "Light = " + str(light.read())    # Print the value of the light sensor
    f.delay_ms(10)                          # Delay for 10ms 