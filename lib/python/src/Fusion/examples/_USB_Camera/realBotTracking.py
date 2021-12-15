# import the necessary packages
import Fusion
import numpy as np
import imutils
import cv2
import time

f = Fusion.driver()

camera      = 0                             # Selects first camera detected
resolution  = (320,240)                     # Set camera resolution (width,height)
hsv_value   = ((50,80,30),(80,255,255))    # Set lower/upper HSV boundaries
iterations  = 2                             # Cleanup Iterations (optional)
radius      = 2                             # Set the minimum pixel radius for detection 
cam_output  = False                         # See the camera output when in VNC or HDMI

# Constructor for the camera class 
cam = Fusion.usbCamera(camera, resolution, hsv_value, iterations, radius, cam_output)

FORWARD_SPEED = 50
TURN_GAIN = 0.75
STOP_RADIUS = 30 

print "running"

# Keep looping
while True:
    x = cam.read()[0]    
    
    if (cam.RADIUS >= STOP_RADIUS):
        left_motor = 0
        right_motor = 0
    
    elif(x != None):
        x = int(((x-160) / 1.6) * TURN_GAIN)
        y = FORWARD_SPEED
        
        left_motor = y + x 
        if(left_motor >= 100): left_motor = 100
        elif (left_motor <= -100): left_motor = -100
        
        right_motor = y - x
        if(right_motor >= 100): right_motor = 100 
        elif(right_motor <= -100): right_motor = -100
        
    else: 
        left_motor = 0
        right_motor = 0
    
    print cam.read()
        
    f.motorSpeed(f.M0, -right_motor)
    f.motorSpeed(f.M1, -left_motor)
    
