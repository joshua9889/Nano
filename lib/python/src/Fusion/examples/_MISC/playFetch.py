import Fusion
import time 
import math

s       = Fusion.driver()
ods     = Fusion.range(f)
ir      = Fusion.locator360(f)
comp    = Fusion.compass(f)

# -------------------------------------------------------------------
# Camera setup for tracking green ball
# -------------------------------------------------------------------
# Connect RPI to a HDMI display or VNC desktop and run the following
# in a terminal, using the sliders to determine the correct upper and
# lower HSV values of the object/ball you wish to detect and place them
# in the hsv_value constant below. 
#
# $ range-detector --filter HSV --webcam
#
# DUCTAPE ((40,60,60),(90,255,255))
# PAINTED ((50,100,100),(80,255,255))
camera      = 0                             # Selects first camera detected
resolution  = (320,240)                     # Set camera resolution (width,height)
hsv_value   = ((50,100,100),(80,255,255))     # Set lower/upper HSV boundaries
iterations  = 2                             # Cleanup Iterations (optional)
radius      = 5                             # Set the minimum pixel radius for detection 
cam_output  = False                         # See the camera output when in VNC or HDMI
cam = Fusion.usbCamera(camera, resolution, cam_output)

# -------------------------------------------------------------------
# Camera variables and constants
output                   = None 
cam_servo_position       = 12
temp_servo_position      = 0
cam_servo_off_bandwidth  = 30
cam_servo_gain           = 0.02
cam_swing_toggle         = False

# -------------------------------------------------------------------
# Mechanical definitions
CAM_SERVO                = f.S1
f.servoEnable(CAM_SERVO, 1)
f.servoTarget(CAM_SERVO, cam_servo_position)

GRIP_SERVO              = f.S0
GRIP_OPEN               = 140
GRIP_CLOSE              = 40
f.servoEnable(GRIP_SERVO, 1)

LEFT_MOTOR              = f.M1
RIGHT_MOTOR             = f.M0
DEFAULT_FORWARD         = 40
MOTOR_GAIN              = 0.2
CENTER_TARGET           = 200
left_motor              = DEFAULT_FORWARD
right_motor             = DEFAULT_FORWARD

RANGE_TRIG              = 5

LOCATOR_CENTER          = 36
LOCATOR_INTENSITY       = 150

compass_bw              = 2
compass_home            = comp.getHeading()
print compass_home

while True:
    
    # ---------------------------------------------------------------
    # Look for the ball....
    f.servoTarget(GRIP_SERVO, GRIP_CLOSE)
    while True:
        output = cam.trackObject(hsv_value, iterations, radius)[0]        
        if(cam_swing_toggle == False): cam_servo_position += 1
        else: cam_servo_position -= 1
        if(cam_servo_position > 250): cam_swing_toggle = True 
        elif(cam_servo_position < 5): cam_swing_toggle = False
        f.servoTarget(CAM_SERVO, cam_servo_position)        
        f.motorSpeed(LEFT_MOTOR+RIGHT_MOTOR, 0)
        if (output != None): break;    
    temp_servo_position = cam_servo_position
    cam_servo_position = 127
    f.servoTarget(CAM_SERVO, cam_servo_position)
    time.sleep(0.1)
    while True:
        output = cam.trackObject(hsv_value, iterations, radius)[0]
        if(output != None):
            output -= int(resolution[0]/2) 
            if((output <= cam_servo_off_bandwidth) and (output >= -cam_servo_off_bandwidth)): break; 
        if (temp_servo_position <= 127):
            f.motorSpeed(LEFT_MOTOR, 25)
        elif(temp_servo_position >= 127):
            f.motorSpeed(RIGHT_MOTOR, 25)    
    f.motorSpeed(LEFT_MOTOR+RIGHT_MOTOR, 0)
    
    # ---------------------------------------------------------------
    # Go and retrieve the ball
    f.servoTarget(GRIP_SERVO, GRIP_OPEN)
    time.sleep(0.1)
    while True:
        output = cam.trackObject(hsv_value, iterations, radius)[0]
        if (output == None):   
            f.motorSpeed(LEFT_MOTOR+RIGHT_MOTOR, DEFAULT_FORWARD)
            
        # Drive to ball and stop when range sensor detects an object
        else:
            output = CENTER_TARGET - output
            left_motor = (DEFAULT_FORWARD - int(output*MOTOR_GAIN))
            if(left_motor > 100): left_motor = 100 
            elif(left_motor < -100): left_motor = -100                        
            right_motor = (DEFAULT_FORWARD + int(output*MOTOR_GAIN))
            if(right_motor > 100): right_motor = 100 
            elif(right_motor < -100): right_motor = -100            
            f.motorSpeed(LEFT_MOTOR, left_motor)
            f.motorSpeed(RIGHT_MOTOR, right_motor)
        if (ods.optical() > RANGE_TRIG): break;
    
    #----------------------------------------------------------------
    # Drive forward and close gripper
    f.motorSpeed(LEFT_MOTOR+RIGHT_MOTOR, DEFAULT_FORWARD)
    time.sleep(0.5)
    f.motorSpeed(LEFT_MOTOR+RIGHT_MOTOR, 0)
    f.servoTarget(GRIP_SERVO, GRIP_CLOSE)
    time.sleep(0.2)
    # ---------------------------------------------------------------
    #Search for IR Beacon
    while True:
        value = ir.getHeading(1200)
        f.motorSpeed(LEFT_MOTOR, 50)
        f.motorSpeed(RIGHT_MOTOR, -50)
        if (value == LOCATOR_CENTER): break;
    
    # ---------------------------------------------------------------
    # Drive towards IR Beacon till a certain intensity value
    while True:
        if(ir.getIntensity(1200) >= LOCATOR_INTENSITY): break;
        if(ir.getHeading(1200) == LOCATOR_CENTER): 
            f.motorSpeed(LEFT_MOTOR+RIGHT_MOTOR, 100)
        elif(ir.getHeading(1200) < LOCATOR_CENTER):
            f.motorSpeed(LEFT_MOTOR, 50)
            f.motorSpeed(RIGHT_MOTOR, 100)
        elif(ir.getHeading(1200) > LOCATOR_CENTER): 
            f.motorSpeed(LEFT_MOTOR, 100)
            f.motorSpeed(RIGHT_MOTOR, 50)
    
    # ---------------------------------------------------------------
    # Drop off ball and return to starting direction     
    f.motorSpeed(LEFT_MOTOR+RIGHT_MOTOR, 0)
    time.sleep(0.2)
    f.servoTarget(GRIP_SERVO, GRIP_OPEN)
    time.sleep(0.5)
    f.motorSpeed(LEFT_MOTOR+RIGHT_MOTOR, -100)
    time.sleep(0.5)
    f.motorSpeed(LEFT_MOTOR+RIGHT_MOTOR, 0)
    
    # ---------------------------------------------------------------
    # Turn until facing the starting home position
    f.motorSpeed(LEFT_MOTOR, 100)
    f.motorSpeed(RIGHT_MOTOR, -100)
    while True:
        temp = comp.getHeading()
        print (temp,compass_home)
        if ((temp >= (compass_home - compass_bw)) and (temp <= (compass_home + compass_bw))): break;
    f.motorSpeed(LEFT_MOTOR+RIGHT_MOTOR, 0)   
