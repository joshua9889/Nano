'''
readPID.py - Return the current PID parameters of a motor controller 
    (c) Modern Robotics Inc. 2017  http://www.modernroboticsinc.com

Description:
    The following example reads and returns the PID settings of a connected 
    Core motor controller for both ports. 
    
    NOTE:
    Use detectDevices.py example to determine the serial number of your connected
    motor controller and enter that value in the constructor below.
        
Connections:
    Core Motor Controller   = USB Port
'''

import CoreControl 
import time 

# Class definitions
c = CoreControl.driver()

# Change the 'AL00VVPP' value to reflect the Serial number
# of your connected module. 
m1 = CoreControl.coreMotorController(c, 'AL00VVPP')

# Read and print the current PID values for both motor ports 
values = m1.readPIDvalues(1)
print "\nPort 1: "
print '  P = ' + str(values[0])
print '  I = ' + str(values[1])
print '  D = ' + str(values[2])
print '  R = ' + str(values[3])
print 

values = m1.readPIDvalues(2)
print "Port 2: "
print '  P = ' + str(values[0])
print '  I = ' + str(values[1])
print '  D = ' + str(values[2])
print '  R = ' + str(values[3])
print
