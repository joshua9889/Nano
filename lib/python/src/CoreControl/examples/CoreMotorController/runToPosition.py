'''
runToPosition.py - Run to encoder position example
    (c) Modern Robotics Inc. 2017  http://www.modernroboticsinc.com

Description:
    The following example uses feedback from the motor encoders to hold a 
    selected position. PID values for difference motors can be changed using
    the setPID.py example. 
    
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

# Alternate the target position in 2 second intervals.
while True:
    m1.runToPosition(1, 50, 1000)   # Move to position 1000 at a speed of 50
    time.sleep(2)
    m1.runToPosition(1, 50, 0)      # Move to position 0 at a speed of 50
    time.sleep(2)