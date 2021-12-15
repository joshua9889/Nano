'''
seekerRead.py - Get the 1200/600hZ Heading and Intesities. 
    (c) Modern Robotics Inc. 2017  http://www.modernroboticsinc.com

Description:
    The following example continuously reads the 1200Hz and 600Hz 
    heading and intensity values of the IR Seeker V3 sensor. Both values
    can be read independently allowing both frequencies to be used at the 
    same time.
    
Connections:
    MRI IR Seeker V3        = I2C  
'''

import Fusion

# Class definitions -----------------------------------------------------------
f = Fusion.driver()
s = Fusion.seekerV3(f)

# Program Start ---------------------------------------------------------------
while True:
    print "1200Hz Heading   = " + str(s.getHeading(1200))
    print "1200Hz Intensity = " + str(s.getIntensity(1200))
    print "600Hz Heading    = " + str(s.getHeading(600))
    print "600Hz Intensity  = " + str(s.getIntensity(600))
    print 
    f.delay(0.1)