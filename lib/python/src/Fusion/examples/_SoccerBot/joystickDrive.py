import Fusion
import time 

f = Fusion.driver()
j = Fusion.joystick()
#cam = Fusion.camera(-1, (320,240))

speed_factor = 1.0
spinner = 128

f.servoTarget(f.S0, 128)
f.servoEnable(f.S0, 1)

while True:
    #cam.trackObject(hsv_thresh=((10, 100, 0),(30, 255,255)),cam_enable=True)
    
    (left_motor, right_motor) = j.mixer(0, 1)
    
    f.motorSpeed(f.M0, int(right_motor*speed_factor))
    f.motorSpeed(f.M1, int(left_motor*speed_factor))