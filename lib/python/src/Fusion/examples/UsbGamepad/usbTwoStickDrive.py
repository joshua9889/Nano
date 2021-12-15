'''
usbTwoStickDrive.py - Two-Stick drive example for USB Controller
    (c) Modern Robotics Inc. 2018  http://www.modernroboticsinc.com

Description:    
    The following example uses the base configuration of the Fusion robot
    kit and allows the user to drive the robot using a wired or wireless
    USB Gamepad controller. 
    
    This uses a basic two-stick tank style drive configuration 
    where the left stick y-axis controls the left motor and the right 
    stick y-axis controls the right motor. 
    
Connections:
    USB Gamepad             = USB Port
    Left Motor              = M1 
    Right Motor             = M0 
    
'''

import Fusion 

# Class definitions -----------------------------------------------------------
f = Fusion.driver()
u = Fusion.usbGamepad(0)

# Axis definitions ------------------------------------------------------------
# Refer to the documentation or use the identify joystick example to 
# determine the appropriate axis numbers for the joystick intended. 

# Logitech F310
LEFT_Y_AXIS     = 1 
RIGHT_Y_AXIS    = 3

# Xbox 360
# LEFT_Y_AXIS     = 1 
# RIGHT_Y_AXIS    = 4

# Program start ---------------------------------------------------------------
while True: 
    # Get the y axis value from each joystick and place them 
    # in the left and right motor values accordingly. 
    # NOTE: set inv to True/False if motors are reversed based
    # on your controller. 
    
    left = u.readAxis(LEFT_Y_AXIS, inv=True)
    right = u.readAxis(RIGHT_Y_AXIS, inv=True)
    
    # Set the left and right motors to the values accordingly. 
    f.motorSpeed(f.M1, left) 
    f.motorSpeed(f.M0, right) 