'''
magneticRead.py - Read the analog value of a Magnetic Sensor
    (c) Modern Robotics Inc. 2017  http://www.modernroboticsinc.com

Description:
    The following example uses the analog wrapper library to attach
    a name to a MRI Magnetic sensor on the specified port and 
    read its analog value. 
    
Connections:
    MRI Magnetic Sensor            = A0 
'''

import Fusion

# Class definitions -----------------------------------------------------------
f = Fusion.driver()
mag = Fusion.analog(f, f.A0)

# Program Start ---------------------------------------------------------------
while True:
    print "Magnetic = " + str(mag.read())    # Print the value of the magnetic sensor
    f.delay_ms(10)                           # Delay for 10ms 