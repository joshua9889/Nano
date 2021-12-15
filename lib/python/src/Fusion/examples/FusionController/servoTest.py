''' 
servoTest.py - Servo example for use with the Fusion Control System
    (c) Modern Robotics Inc. 2017  http://www.modernroboticsinc.com

Description:
    The following example swings two servos connected to ports S0 and S1 from end
    to end and requires the MRI 6.0v NIMH battery pack for operation. Note the enable 
    function has an option "extended=True" which changes the bandwidth from 
    750us/2250us to the extended 500us/2500us and can be set on a port by port basis. 
    
Note:
    Modern Robotics Inc. is not responsible for damage to servos caused by using  
    extended mode and the user exceeding the mechanical limits of the servo. When
    using extended mode, start from 128 and work your way to 0/255 listening for 
    a humming sound that indicates the mechanical limits have been reached and do 
    not exceed these values. 
    
Connections:
    MRI 6.0v NIMH Battery   = Battery Port
    Servo                   = S0
    Servo                   = S1
'''

import Fusion

# Class definitions -----------------------------------------------------------
f = Fusion.driver()

# Constants/Variables ---------------------------------------------------------
f.servoEnable(f.S0, 1)
f.servoEnable(f.S1, 1, extended=True)

# Program Start ---------------------------------------------------------------
while True:
    f.servoTarget(f.S0+f.S1, 200)   # Set the servo target to 200 (can go to 255 but limits may be exceeded in extended mode)
    f.delay(1)    
    f.servoTarget(f.S0+f.S1, 50)    # Set the servo target to 50 (can go to 0 but limits may be exceeded in extended mode)
    f.delay(1)
    