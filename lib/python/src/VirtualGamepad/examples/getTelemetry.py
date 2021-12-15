'''
getTelemetry.py - Return the controller values as telemetry data
    (c) Modern Robotics Inc. 2018  http://www.modernroboticsinc.com

Description:
    The following uses the VirtualGamepad library to create 
    a browser accessible game controller for use with a touch device
    such as a phone or tablet. 
    
    This example reads the value of all buttons and axis within the
    environment and returns their values as telemetry data to the 
    screen. 
    
Connections:
    Phone or Tablet         = WiFi @ (IpAddress):5000
    
'''

import VirtualGamepad
import time 

# Class definitions -----------------------------------------------------------
v = VirtualGamepad.service(cam=True)

# Program start ---------------------------------------------------------------
while True:    
    v.telemetry(1, "Left  = " + str(v.leftJoystick()))
    v.telemetry(2, "Right = " + str(v.rightJoystick()))
    v.telemetry(3, "Btn A = " + str(v.readButton('A')))
    v.telemetry(4, "Btn B = " + str(v.readButton('B')))
    v.telemetry(5, "Btn X = " + str(v.readButton('X')))
    v.telemetry(6, "Btn Y = " + str(v.readButton('Y')))
    
    # This shows that any line can be updated even after
    # a telemetry line after it has been created by printing 
    # the current CPU time. 
    v.telemetry(0, str(time.time()))
