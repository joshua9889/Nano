'''
odsRead.py - Read the analog value of an Optical Distance Sensor
    (c) Modern Robotics Inc. 2017  http://www.modernroboticsinc.com

Description:
    The following example uses the analog wrapper library to attach
    a name to an ODS on the specified port and read its analog value. 
    
Connections:
    MRI ODS Sensor            = A0 
'''

import Fusion

# Class definitions -----------------------------------------------------------
f = Fusion.driver()
ods = Fusion.analog(f, f.A0)

# Program Start ---------------------------------------------------------------
while True:
    print "ODS = " + str(ods.read())    # Print the value of the ods sensor
    f.delay_ms(10)                      # Delay for 10ms 