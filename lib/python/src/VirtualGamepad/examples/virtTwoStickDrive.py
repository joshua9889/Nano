'''
virtTwoStickDrive.py - Two stick drive example for Virtual Gamepad
    (c) Modern Robotics Inc. 2018  http://www.modernroboticsinc.com

Description:
    The following uses the VirtualGamepad library to create 
    a browser accessible game controller for use with a touch device
    such as a phone or tablet. 
    
    This uses a tank style configuration where the left stick controls 
    the left side and the right stick controls the right. 
    
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
v.telemetry(0, "Two stick drive example")
while True: 
    # Get the (x,y) values of both joysticks
    left_stick = v.leftJoystick()
    right_stick = v.rightJoystick()
    
    # Set the left and right motor equal to the 
    # the Y value accordingly. 
    f.motorSpeed(f.M1, left_stick[1]) 
    f.motorSpeed(f.M0, right_stick[1])
    
    # Print the left and right stick Y values 
    # to the telemetry window. 
    v.telemetry(1, "Left Y = " + str(left_stick[1]))
    v.telemetry(2, "Right Y = " + str(right_stick[1]))
    
    