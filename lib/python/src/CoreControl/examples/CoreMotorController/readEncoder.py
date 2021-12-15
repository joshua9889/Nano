'''
readEncoder.py - Returns the encoder value of the connected motor
    (c) Modern Robotics Inc. 2017  http://www.modernroboticsinc.com

Description:
    The following example prints the value of an encoder connected to encoder motor
    port 1. Rotate the shaft to see the value change or change the motor speed from 
    0.     
    
    NOTE:
    Use detectDevices.py example to determine the serial number of your connected
    motor controller and enter that value in the constructor below.
    
    
Connections:
    Core Module             = USB Port
    DC motor                = Module Port 1 
    Encoder                 = Encoder Port 1
'''

import CoreControl 
import time 

# Class definitions
c = CoreControl.driver()

# Change the 'AL00VVPP' value to reflect the Serial number
# of your connected module. 
m1 = CoreControl.coreMotorController(c, 'AL00VVPP')

# Read and print the encoder value every 10mS 
while True:
    print "Encoder value = " + str(m1.readEncoder(2))
    time.sleep(0.01)