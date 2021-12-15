'''
getHeading.py - Returns the current heading of the compass sensor
    (c) Modern Robotics Inc. 2017  http://www.modernroboticsinc.com

Description:
    The following example continuously returns the current heading
    of the compass sensor in degrees and also an indication of 
    NESW direction. 
    
Connections:
    Compass Sensor      - I2C
'''

import Fusion

# Class definitions -----------------------------------------------------------
f = Fusion.driver()
comp = Fusion.compass(f)

# Program Start ---------------------------------------------------------------
while True:
    heading = comp.getHeading()    
    if((heading >= 0 and heading <= 22) or (heading >= 337 and heading <= 359)):
        print(str(heading) + "   N")
    elif(heading > 22 and heading < 67):
        print(str(heading) + "   NE")
    elif(heading >= 67 and heading <= 112):
        print(str(heading) + "   E")
    elif(heading > 112 and heading < 157):
        print(str(heading) + "   SE")
    elif(heading >= 157 and heading <= 202):
        print(str(heading) + "   S")
    elif(heading > 202 and heading < 247):
        print(str(heading) + "   SW")
    elif(heading >= 247 and heading <= 292):
        print(str(heading) + "   W")
    elif(heading > 292 and heading < 337):
        print(str(heading) + "   NW")
    f.delay_ms(10)