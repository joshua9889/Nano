import Fusion
import time 

# Constructors
f = Fusion.driver()
cam = Fusion.camera(-1, (320,240))

HSV         = ((0, 150, 0),(40, 255, 255))
CAMERA_MASK = [240, 0]
VNC         = True

while True:
    
    print "Camera mask = " + str(CAMERA_MASK)
    print "Coordinates = " + str(cam.trackObjectMasked(HSV, CAMERA_MASK, 2, 3, VNC))
    print
    
    temp = cam.KEY_PRESS 
    
    if(temp == 81): CAMERA_MASK[1] -= 1
    elif(temp == 82): CAMERA_MASK[0] += 1 
    elif(temp == 83): CAMERA_MASK[1] += 1 
    elif(temp == 84): CAMERA_MASK[0] -= 1
    
    if(CAMERA_MASK[0] > 240): CAMERA_MASK[0] = 240 
    elif(CAMERA_MASK[0] < 0): CAMERA_MASK[0] = 0
    
    if(CAMERA_MASK[1] > 240): CAMERA_MASK[1] = 240 
    elif(CAMERA_MASK[1] < 0): CAMERA_MASK[1] = 0
    
    if(CAMERA_MASK[0] < CAMERA_MASK[1]): CAMERA_MASK[1] = CAMERA_MASK[0]
    