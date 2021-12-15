'''
getPassiveColor.py - Return the color of a light source using passive mode
    (c) Modern Robotics Inc. 2017  http://www.modernroboticsinc.com

Description:
    The following example uses an MRI Touch Sensor and Color Sensor
    to read and return all color readings of a light source such as 
    an MRI Color Beacon. Pressing the Touch sensor button will take 
    one reading per press. 
    
Connections:
    Touch Sensor            = D0
    Color Sensor            = I2C
'''
import Fusion

# Class definitions -----------------------------------------------------------
f = Fusion.driver()
t = Fusion.digital(f, f.D0)
c = Fusion.color(f)

# Program Start ---------------------------------------------------------------
c.colorSetup(c.PASSIVE, c.SIXTY_HZ)

while True:
    print "Press the TOUCH sensor to read the COLOR sensor"
    while (t.read() == 0): pass 
    while (t.read() == 1): pass 
    
    print 
    print "Color Number = " + str(c.getColorNumber())
    print    
    
    (red, green, blue, white) = c.getColorValue()
    print "Color Value:"
    print "RED = " + str(red)
    print "GRN = " + str(green)
    print "BLU = " + str(blue)
    print "WHT = " + str(white)
    print 
    
    print "Color index = " + str(c.getColorIndex())
    print 
    
    (red, green, blue) = c.getRGBIndex()
    print "RGB Index:"
    print "RED = " + str(red)
    print "GRN = " + str(green)
    print "BLU = " + str(blue)
    print 
    
    (red, green, blue, white) = c.getColorReading()
    print "Color Reading:"
    print "RED = " + str(red)
    print "GRN = " + str(green)
    print "BLU = " + str(blue)
    print "WHT = " + str(white)
    print 
    
    (red, green, blue, white) = c.getColorNormalized()
    print "Color Normalized:"
    print "RED = " + str(red)
    print "GRN = " + str(green)
    print "BLU = " + str(blue)
    print "WHT = " + str(white)
    print
    print "---------------------------------------"
    print 