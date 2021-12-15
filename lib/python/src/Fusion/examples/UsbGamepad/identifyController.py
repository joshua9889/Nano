'''
identifyController.py - Identify gamepad and read button/axis numbers and values
    (c) Modern Robotics Inc. 2017  http://www.modernroboticsinc.com

Description:
    Use the following example to identify what button is associated with 
    each number before applying to your user program. 
    
    Note: Bluetooth gamepads and joysticks are currently not implemented, 
    only Wireless devices with an accompanying USB dongle are supported by
    this library. It should also be noted that using any device not on the
    MRI approved gamepad list may or may not be supported by the linux software
    and therefore may not be supported by this library. 
    
Connections:
    MRI approved Wired/Wireless USB Joystick or Gamepad     = USB port
'''

import Fusion
import time 

# Class definitions -----------------------------------------------------------
f = Fusion.driver()
j = Fusion.usbGamepad(0)

# Program Start ---------------------------------------------------------------
# Print the device information and the number of buttons, hats, and axis available
print "Name    = " + str(j.name)
print "Buttons = " + str(j.num_buttons)
print "Axes    = " + str(j.num_axes)
print "Hats    = " + str(j.num_hats)

# Detect and print the button, axis, or HAT being activated on the controller
while True:
    for i in range(j.num_buttons):
        if(j.readButton(i) == 1): print "Btn " + str(i)
        
    for i in range(j.num_axes):
        temp = j.readAxisFloat(i)
        if((temp <= -0.05) or (temp >= 0.05)): print "Axis " + str(i) + " --> " + str(j.readAxisFloat(i))[:5] + " --> " + str(j.readAxis(i))
        
    for i in range(j.num_hats):
        temp = j.readHat(i)
        if(temp != (0,0)): print "Hat " + str(i) + " --> " + str(temp)
        
    time.sleep(0.1)
    