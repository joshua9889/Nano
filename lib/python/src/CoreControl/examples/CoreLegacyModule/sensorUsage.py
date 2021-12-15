'''
sensorUsage.py - Sensor library usage for the Core Legacy Module 
    (c) Modern Robotics Inc. 2018 http://www.modernroboticsinc.com

Description:
    The following example shows the use of the low level function calls
    within the Legacy Module library for support of custom or unsupported
    sensors.
    
    Note 9v for lego NXT Ultrasonic sensor is only avaialable on ports
    S4 and S5. 
    
Connections:
    NXT Touch           = S3
    NXT Light           = S4
    NXT Ultrasonic      = S5
'''

import CoreControl
import time 

# Class definitions -----------------------------------------------------------
c = CoreControl.driver()
leg = CoreControl.coreLegacyModule(c, 'AL00VCO2')

t = leg.nxt_Touch(leg.S3)
l = leg.nxt_Light(leg.S4)
u = leg.nxt_Ultrasonic(leg.S5)

# Program Start ---------------------------------------------------------------
while True:
    # Read touch sensor 
    touch = t.read()

    # Read Light sensor with led off 
    l.ledEnable(False)
    time.sleep(0.1)
    off_light = l.read()

    # Read Light sensor with led on
    l.ledEnable(True)
    time.sleep(0.1)
    on_light = l.read()

    # Read aUltrasonic distance 
    ultra = u.read()

    print "touch=%s  off_light=%s  on_light=%s  ultra=%s" % (touch, off_light, on_light, ultra)