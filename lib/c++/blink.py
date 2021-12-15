import SpartanPi
import time

s = SpartanPi.driver()

while True:
    s.setLED(1, 1)
    s.setLED(0, 0)
    time.sleep(0.1)
    
    s.setLED(1, 0)
    s.setLED(0, 1)
    time.sleep(0.1)
    