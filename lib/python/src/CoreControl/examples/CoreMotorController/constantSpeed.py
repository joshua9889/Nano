'''
constantSpeed.py - Constant speed example for use with the Core Motor Module
    (c) Modern Robotics Inc. 2017  http://www.modernroboticsinc.com

Description:
    The following example runs a motor on port 1 of the selected motor controller
    with an alternating direction in 1 second intervals. Constant speed mode utilizes
    feedback from the motor encoder to maintain a specific speed regardless of load. 
    
    NOTE:
    Use detectDevices.py example to determine the serial number of your connected
    motor controller and enter that value in the constructor below.
    
    
Connections:
    Core Motor Controller   = USB Port
    DC motor                = Motor Port 1 
    Encoder                 = Encoder Port 1
'''

import CoreControl 
import time 

# Class definitions
c = CoreControl.driver()

# Change the 'AL00VVPP' value to reflect the Serial number
# of your connected module. 
m1 = CoreControl.coreMotorController(c, 'AL00VVPP')

# Alternate the direction in 1 second intervals
while True:
    m1.constantSpeed(1, 30)
    time.sleep(1)
    m1.constantSpeed(1, -30)
    time.sleep(1)