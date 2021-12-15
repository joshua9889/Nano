'''
virtMixedDrive.py - One stick mixed drive example for Virtual Gamepad
    (c) Modern Robotics Inc. 2018  http://www.modernroboticsinc.com

Description:
    The following uses the VirtualGamepad library to create 
    a browser accessible game controller for use with a touch device
    such as a phone or tablet. 
    
    This uses a mixed style drive configuration where the left stick 
    x-axis controls turning and the y-axis controls forward and reverse.
    
Connections:
    Phone or Tablet         = WiFi @ (IpAddress):5000
    Left Motor              = M1 
    Right Motor             = M0 
    
'''

import Fusion 
import VirtualGamepad 

# Class definitions -----------------------------------------------------------
f = Fusion.driver()
v = VirtualGamepad.service()

# Program start ---------------------------------------------------------------
v.telemetry(0, "Mixed drive example")
while True: 
    # Get the (x,y) values for the left joystick. 
    # These values now map to the left and right motors as 
    # the returned values are mixed accordingly. 
    (left, right) = v.leftJoystick(mixer=True, y_inv=False, x_inv=True)
    
    # Set the left and right motors to the values accordingly. 
    f.motorSpeed(f.M1, left) 
    f.motorSpeed(f.M0, right) 
    
    # Print the Left stick values to the telemetry window. 
    v.telemetry(1, "Left Motor  = " + str(left))
    v.telemetry(2, "Right Motor = " + str(right))