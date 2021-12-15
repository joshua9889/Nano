'''
usbMixedDrive.py - One stick mixed drive example for USB controller
    (c) Modern Robotics Inc. 2018  http://www.modernroboticsinc.com

Description:    
    The following example uses the base configuration of the Fusion robot
    kit and allows the user to drive the robot using a wired or wireless
    USB Gamepad controller. 
    
    This uses a mixed style drive configuration where the left stick 
    x-axis controls turning and the y-axis controls forward and reverse.
    
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

# Logitech F310 and Xbox 360
LEFT_X_AXIS = 0 
LEFT_Y_AXIS = 1 

# Program start ---------------------------------------------------------------
while True: 
    # Get the mixed axis values of the left joystick and 
    # return them to left and right motor variables 
    # accordingly. 
    (left, right) = u.mixer(LEFT_X_AXIS, LEFT_Y_AXIS, x_inv=True, y_inv=True)
    
    # Set the left and right motors to the values accordingly. 
    f.motorSpeed(f.M1, left) 
    f.motorSpeed(f.M0, right) 