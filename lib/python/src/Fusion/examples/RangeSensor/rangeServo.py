'''
rangeServo.py - Sweep a servo based on ODS value of Range Sensor
    (c) Modern Robotics Inc. 2017  http://www.modernroboticsinc.com

Description:
    The following example reads the current value of the ODS built
    into the Range Sensor as a value 0-255 and sets the target of
    the connected servo to that value accordingly. 
    
Connections:
    MRI Range Sensor            = I2C 
    Servo                       = S0
'''

import Fusion

# Class definitions -----------------------------------------------------------
f = Fusion.driver()
r = Fusion.range(f)

# Program Start ---------------------------------------------------------------
f.servoEnable(f.S0, 1)                  # Enable PWM on servo port S0

while True:
    temp = r.optical()                  # Store the current ODS value in temp
    print "Optical = " + str(temp)      # Print the current value 
    f.servoTarget(f.S0, temp)           # Set the servo target to the value 
    