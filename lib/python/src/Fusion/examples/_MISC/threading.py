'''
multithreading.py - Threading example for use with the Fusion Control System
    (c) Modern Robotics Inc. 2018  http://www.modernroboticsinc.com

Description:
    The following example uses the Fusion thread library to create an easy to use 
    system for multi-threading programs. All thread processes will stop when the 
    main program has been terminated or a stop() command has been issued. 
    
Connections:
    None
'''

import Fusion
import time 

# Class definitions -----------------------------------------------------------
f = Fusion.driver()

# Variables 
yellow_led = 0

# Thread Functions ------------------------------------------------------------
def thread_1():        
    for i in range(3): 
        print "thread_1"
        time.sleep(1)
t1 = Fusion.thread(thread_1)
        
def thread_2():
    f.setLED(f.BLUE, 1)
    time.sleep(0.25)
    f.setLED(f.BLUE, 0)
    time.sleep(0.25)
t2 = Fusion.thread(thread_2)

def thread_3():        
    global yellow_led 
    yellow_led ^= 1 
    f.setLED(f.YELLOW, yellow_led)
t3 = Fusion.thread(thread_3)

# Program Start ---------------------------------------------------------------
# The following thread will be executed one time and can be started again. 
t1.start()

# Start thread as an infinite loop()
t2.start(0)

# Run thread every 0.5 seconds unless function takes longer than set time. 
t3.start(0.5)

while True:
    print (str(t1.isAlive()) + ' ' + str(t2.isAlive()) + ' ' + str(t3.isAlive()))
    time.sleep(0.1)