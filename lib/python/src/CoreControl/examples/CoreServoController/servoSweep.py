'''
servoSweep.py - Sweep servo using both standard and extended mode.
    (c) Modern Robotics Inc. 2018 http://www.modernroboticsinc.com

Description:
    The following example sweeps a servo from 50 to 200 to avoid hitting the 
    mechanical limits on two different ports, one being standard range 
    750us-2250us and the other being extended 500us to 2500us. 
    
    NOTE:
    Use detectDevices.py example to determine the serial number of your connected
    motor controller and enter that value in the constructor below.
    
Connections:
    Core Servo Controller   = USB Port
    Servo                   = Servo Port 1
    Servo                   = Servo Port 2
'''

import CoreControl 
import time 

# Class definitions
c = CoreControl.driver()
c.printDevices()

# Change the 'AL00VVPP' value to reflect the Serial number
# of your connected module. 
s1 = CoreControl.coreServoController(c, 'AL00VVPP')

# Enable servo PWM and set servo 2 to extended mode 
s1.pwmEnable(True)
s1.extendedModeEnable(1, False)
s1.extendedModeEnable(2, True)

# Read and print the encoder value every 10mS 
while True:
    s1.servoTarget(1, 200)
    s1.servoTarget(2, 200)
    time.sleep(1)
    
    s1.servoTarget(1, 50)
    s1.servoTarget(2, 50)
    time.sleep(1)