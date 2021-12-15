import Fusion

f = Fusion.driver()
j = Fusion.joystick()

while True:
    (left_motor, right_motor) = j.mixer(0,1)
    f.motorSpeed(f.M0, right_motor)
    f.motorSpeed(f.M1, left_motor)