import Fusion

f = Fusion.driver()

# Original correct string if needed. 
# "raspberrypi login:;pi\n;Password:;raspberry\n;pi@raspberrypi:~$;sudo poweroff\n;Power down;*"

#--------------------------------------------------------------------------------------------------
# Only modify this string when performing tests, use the one above to reset if needed. 

new_string = "rasppi login:;pi\n;Password:;raspberry\n;pi@raspberrypi:~$;sudo poweroff\n;Power down;*"

#--------------------------------------------------------------------------------------------------
# Uncomment the functions below as needed 

#f.writeEEPROM(new_string)
#f.reloadEEPROM()
f.defaultEEPROM()

#--------------------------------------------------------------------------------------------------
# Do not modify below this line...
print 
print f.readEEPROM()
print
print f.readVariables()
print
print f.getPowerState()

'''
1.  Comment defaultEEPROM and uncomment writeEEPROM. Change the "raspberrypi login" 
    in new string to "rasp login" and run the program. 
    - Verify EEPROM has rasp and variable still has raspberry
    - Power off/on and verify power state does not reach level 6
    
2.  Comment writeEEPROM and uncomment defaultEEPROM and run the program. 
    - Verify EEPROM variable now says raspberry and variable says rasp 
    - Power off/on and verify power state reaches level 6
    
3.  Comment defaultEEPROM and uncomment writeEEPROM. Change the "raspberrypi login" 
    to "raspberrypiMRI login" and run the program. 
    - Verify EEPROM has raspberrypiMRI login and variable still says raspberry
    - Power off/on and verify power state does not reach level 6
    
4.  Repeat step 2 

5.  Comment defaultEEPROM and uncomment writeEEPROM. Change the "raspberrypi login" 
    in new string to "rasp login" and run the program. 
    - Verify EEPROM has rasp and variable still has raspberry
    - Reboot from the console using "sudo reboot". 
    - The device should still boot to power state 6 as the internal variables 
      have not been updated yet. 
      
6.  Comment writeEEPROM and defaultEEPROM and uncomment reloadEEPROM. Run the program.
    - Verify EEPROM and variables match and have "rasp login"
    - Reboot from the console using "sudo reboot"
    - Verify the power state does not reach level 6
    
7.  Comment writeEEPROM and uncomment defaultEEPROM/reloadEEPROM. Run the program. 
    - Verify EEPROM and variables match and are the correct values. 
    - Reboot from the console using "sudo reboot"
    - Verify the device boots properly, reaches level 6, and properly
      performs a soft shutdown. 
'''