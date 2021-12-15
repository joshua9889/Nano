'''
rateGyroRead.py - Read a rate gyro using the analog wrapper class 
    (c) Modern Robotics Inc. 2017  http://www.modernroboticsinc.com

Description:
   The following example reads the value of an MRI Rate Gyro Sensor
   using the analog wrapper class to give the device a unique name. 
    
Connections:
    MRI Rate Gyro            = A0
'''

import Fusion

# Class definitions -----------------------------------------------------------
f = Fusion.driver()
gyro = Fusion.analog(f, f.A0)

# Program Start ---------------------------------------------------------------
while True:
    print "Gyro = " + str(gyro.read())      # Print the value of the rate gyro
    f.delay_ms(10)                          # Delay for 10ms