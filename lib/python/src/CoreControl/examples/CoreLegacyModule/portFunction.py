'''
portFunction.py - Low level port function example for Core Legacy Module
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

# Program Start ---------------------------------------------------------------

# Set S5 to have 9v enabled for the ultrasonic sensor 
leg.enable_9v(leg.S5, True)

while True:
    # Read touch sensor 
    touch = leg.analogRead(leg.S3)

    # Read Light sensor with led off 
    leg.digitalEnable(leg.S4, 0, 0)
    time.sleep(0.1)
    off_light = leg.analogRead(leg.S4)

    # Read Light sensor with led on
    leg.digitalEnable(leg.S4, 0, 1)
    time.sleep(0.1)
    on_light = leg.analogRead(leg.S4)

    # Read Ultrasonic distance 
    ultra = leg.i2cRead(leg.S5, 0x02, 0x42, 1)[0]

    print "touch=%s  off_light=%s  on_light=%s  ultra=%s" % (touch, off_light, on_light, ultra)