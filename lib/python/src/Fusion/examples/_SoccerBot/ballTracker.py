import Fusion
import time 

# Constructors
f = Fusion.driver()
cam = Fusion.camera(-1, (320,240))
gyro = Fusion.intGyro(f, 0x24)
gyro.setZero()

ORANGE_HSV      = ((10, 150, 0),(30, 255, 255))
GREEN_HSV       = ((50,80,30),(80,255,255))
DETECTION_HSV   = GREEN_HSV

CAMERA_MASK     = (185, 0)
VNC             = False

FORWARD_SPEED   = 50
TURN_SPEED      = 18
GAIN            = 0.22
OFFSET          = 40
MIN_RADIUS      = 45

TURN_GAIN       = 0.06
MIN_SPEED       = 13

invert          = True
x_scaled        = 0
motor_val       = 0

while True:
    # Drive towards ball and stop at ball 

    (x, y, radius) = cam.trackObjectMasked(DETECTION_HSV, CAMERA_MASK, 2, 5, VNC)
    if (radius > MIN_RADIUS): 
        if(x != None):
            gyro.setZero()
            x_scaled = x-160 
            
            motor_val = int(x_scaled * TURN_GAIN)
            if(motor_val >= 100): motor_val = 100 
            elif(motor_val <= -100): motor_val = -100
            
            if(motor_val > 0): motor_val += MIN_SPEED
            if(motor_val < 0): motor_val -= MIN_SPEED
            
            f.motorSpeed(f.M0, -motor_val)
            f.motorSpeed(f.M1, motor_val)
            
            if ((x_scaled > -10) and (x_scaled < 10)): f.motorSpeed(f.M0+f.M1, 0)
    elif(x != None):
        gyro.setZero()
        x_scaled = int((x-160+OFFSET)*GAIN)
        f.motorSpeed(f.M0, -FORWARD_SPEED-x_scaled)
        f.motorSpeed(f.M1, -FORWARD_SPEED+x_scaled)
    else:
        temp = gyro.getAbsolute()
        if (invert == False):
            if(temp > 180): invert = True          
            f.motorSpeed(f.M0, -TURN_SPEED)
            f.motorSpeed(f.M1, TURN_SPEED)
        else:
            if(temp < -180): invert = False         
            f.motorSpeed(f.M0, TURN_SPEED)
            f.motorSpeed(f.M1, -TURN_SPEED)