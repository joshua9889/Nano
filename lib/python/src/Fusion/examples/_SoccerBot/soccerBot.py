import Fusion
import time 

# Constructors
f = Fusion.driver()
cam = Fusion.camera(-1, (320,240))
l_color = Fusion.color(f, 0x20)
r_color = Fusion.color(f, 0x22)
gyro = Fusion.intGyro(f, 0x24)

# Global Variables
post_pause = 0.0
invert = True

# Initializations
f.motorMode(f.M0+f.M1, f.BRAKE)
while (gyro.getAbsolute() != 0): 
    gyro.setZero()
    time.sleep(0.01)

# -----------------------------------------------------------------------------
# Camera Mask and Thresholds
ORANGE_HSV  = ((0, 150, 0),(40, 255, 255))
BLUE_HSV    = ((100, 100, 0),(130, 255, 255))
YELLOW_HSV  = ((0,0,0),(255,255,255))
CAMERA_MASK = (195, 0)
VNC         = False
# ------------------------------------------------------------------------------

f.servoTarget(f.S0, 128)
f.servoEnable(f.S0, 1)

def turnTo(target, speed=14, gain=0.15, bandwidth=1):       
    while True:
        gyro_val = gyro.getAbsolute()
        
        turn_speed = int((target - gyro_val) * gain)
        
        if(turn_speed > 0): turn_speed += speed
        if(turn_speed < 0): turn_speed -= speed
        #print gyro_val
        
        if ((gyro_val >= (target - bandwidth)) and (gyro_val <= (target + bandwidth))): break;
        f.motorSpeed(f.M0, -turn_speed)
        f.motorSpeed(f.M1, turn_speed)          
    f.motorSpeed(f.M0+f.M1, 0)
    return;

# while True:
    # turnTo(90)
    # time.sleep(0.5)
    
    # turnTo(180)
    # time.sleep(0.5)
    
    # turnTo(90)
    # time.sleep(0.5)
    
    # turnTo(0)
    # time.sleep(0.5)
    
while True:
    # 2 ---------------------------------------------------------------------------
    # Turn left 90 degrees
    print "1  - Turn left 90 Degrees"
    turnTo(270)
    time.sleep(post_pause)
    
    # 3 ---------------------------------------------------------------------------
    # Goto white line 
    print "2  - Go to white line"
    while True:
        if ((l_color.getColorNumber() == 14) or (r_color.getColorNumber() == 14)): break
        f.motorSpeed(f.M0, -100)
        f.motorSpeed(f.M1, -95)
    f.motorSpeed(f.M0, 100)
    f.motorSpeed(f.M1, 100)
    time.sleep(0.3)
    f.motorSpeed(f.M0+f.M1, 0)
    time.sleep(post_pause)

    # 4 ---------------------------------------------------------------------------
    # Turn left 90 degrees 
    print "3  - Turn Left 90 degrees"
    turnTo(180)
    time.sleep(post_pause)
    
    # 5 ---------------------------------------------------------------------------
    # Follow white line to the end 
    print "4  - Follow white line to the end"
    while True:
        if (l_color.getColorNumber() == 14): 
            break;
        if (r_color.getColorNumber() == 14):
            f.motorSpeed(f.M0, 0)#0)
            f.motorSpeed(f.M1, -20)#-20)
        else:
            f.motorSpeed(f.M0, -90)
            f.motorSpeed(f.M1, -50)
    f.motorSpeed(f.M0+f.M1, 100)
    time.sleep(0.5)
    f.motorSpeed(f.M0+f.M1, 0)
    time.sleep(post_pause)
    
    # 6 ---------------------------------------------------------------------------
    # Turn and face the center of the arena
    print "5  - Turn and face the center of the arena"
    turnTo(40)
    time.sleep(0.1)
    f.motorSpeed(f.M0+f.M1, -100)
    time.sleep(0.3)
    f.motorSpeed(f.M0+f.M1, 0)
    time.sleep(post_pause)

    # 7 ---------------------------------------------------------------------------
    # Look for a ball and face towards it
    print "6  - Look for the ball and face towards it"
    turn_gain = 0.09
    min_speed = 13
    max_speed = 50
    invert = True
    while True:
        (x, y, radius) = cam.trackObjectMasked(ORANGE_HSV, CAMERA_MASK, 2, 3, VNC)
        if(x != None):
            x_scaled = x-160 
            
            motor_val = int(x_scaled * turn_gain)
            if(motor_val >= 100): motor_val = 100 
            elif(motor_val <= -100): motor_val = -100
            
            if(motor_val > 0): motor_val += min_speed
            if(motor_val < 0): motor_val -= min_speed
            
            f.motorSpeed(f.M0, -motor_val)
            f.motorSpeed(f.M1, motor_val)
            
            if ((x_scaled > -10) and (x_scaled < 10)): break;
        
        else:
            temp = gyro.getAbsolute()
            if (invert == False):
                if(temp > 45): invert = True          
                f.motorSpeed(f.M0, -15)
                f.motorSpeed(f.M1, 15)
            else:
                if(temp < -45): invert = False         
                f.motorSpeed(f.M0, 15)
                f.motorSpeed(f.M1, -15)
    f.motorSpeed(f.M0+f.M1, 0)
    time.sleep(post_pause)

    # 8 ---------------------------------------------------------------------------
    # Drive towards ball and stop at ball 
    print "7  - Drive towards ball until close"
    forward_speed = 50
    gain = 0.22
    OFFSET = 40
    f.servoTarget(f.S0, 255)
    while True: 
        (x, y, radius) = cam.trackObjectMasked(ORANGE_HSV, CAMERA_MASK, 2, 3, VNC)
        if (radius > 40): break;
        if(x != None):
            x_scaled = int((x-160+OFFSET)*gain)
            f.motorSpeed(f.M0, -forward_speed-x_scaled)
            f.motorSpeed(f.M1, -forward_speed+x_scaled)
        else:
            f.motorSpeed(f.M0+f.M1, 0)
    f.motorSpeed(f.M0+f.M1, -15)
    time.sleep(0.5)
    f.motorSpeed(f.M0+f.M1, 15)
    time.sleep(0.5)
    f.motorSpeed(f.M0+f.M1, 0)
    time.sleep(0.2)
    time.sleep(post_pause)
    
    # 9 -----------------------------------------------------------------------
    # Look at the blue goal
    print "8  - Look for the blue goal"
    turn_gain = 0.1
    min_speed = 14
    max_speed = 40 
    invert = True
    
    f.servoTarget(f.S0, 255)
    while True:
        (x, y, radius) = cam.trackObjectMasked(BLUE_HSV, CAMERA_MASK, 2, 3, VNC)
        if(x != None):
            x_scaled = x-160 
            
            motor_val = int(x_scaled * turn_gain)
            if(motor_val >= 100): motor_val = 100 
            elif(motor_val <= -100): motor_val = -100
            
            if(motor_val > 0): motor_val += min_speed
            if(motor_val < 0): motor_val -= min_speed
            
            if(motor_val > 0): f.motorSpeed(f.M1, abs(motor_val))
            else: f.motorSpeed(f.M0, abs(motor_val))
            # f.motorSpeed(f.M0, -motor_val)
            # f.motorSpeed(f.M1, motor_val)
            
            if ((x_scaled > -5) and (x_scaled < 5)): break;
        
        else:
            temp = gyro.getAbsolute()
            if (invert == False):
                if(temp > 90): invert = True          
                f.motorSpeed(f.M0, 0)
                f.motorSpeed(f.M1, 20)
            else:
                if(temp < -90): invert = False         
                f.motorSpeed(f.M0, 20)
                f.motorSpeed(f.M1, 0)
    f.motorSpeed(f.M0+f.M1, 0)
    time.sleep(post_pause)
    
    # 10 --------------------------------------------------------------------------
    # Kick Ball
    print "9 - Kick the ball towards goal"
    f.motorSpeed(f.M0+f.M1, -100)
    time.sleep(0.1)
    f.servoTarget(f.S0, 0)
    time.sleep(0.5)
    f.motorSpeed(f.M0+f.M1, 100)
    f.servoTarget(f.S0, 128)
    time.sleep(0.5)
    f.motorSpeed(f.M0+f.M1, 0)
            