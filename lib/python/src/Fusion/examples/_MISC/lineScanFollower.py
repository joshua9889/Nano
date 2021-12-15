import Fusion
import time 

f = Fusion.driver()
l = Fusion.lineScan(f)

# Adjust the forward speed and GAIN if necessary and at your own risk ---------
FORWARD_SPEED = 30      # Forward speed
GAIN = 2                # Rate at which turn adjustment is made based on sensor reading
CENTER_POINT = 49       # Value when black line is centered on robot

# Set mode for black or white line --------------------------------------------
l.setMode(l.BLACK_LINE);

while True:
    temp = int((CENTER_POINT - l.centerReading()[0]) * GAIN)       
    f.motorSpeed(f.M0, -(FORWARD_SPEED + temp))
    f.motorSpeed(f.M1, -(FORWARD_SPEED - temp))