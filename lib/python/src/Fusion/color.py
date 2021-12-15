#===============================================================================
# color.py - Color Sensor class for the Fusion system
# Copyright (c) 2018-2019 Modern Robotics Inc.
#===============================================================================
# DISCLAIMER:
#	This software is provided "as is", without warranty of any kind, express or
#	implied, including but not limited to the warranties of merchantability,
#	fitness for a particular purpose and non-infringement. In no event shall 
#	the authors or copyright holders be liable for any claim, damages or other
#	liability, whether in an action of contract, tort or otherwise, arising 
#	from, out of, or in connection with the software or the use or other 
#	dealings in the software.
#===============================================================================
# REVISION HISTORY
#
# 26-Mar-20 <jwa> - Fixed problems in the getColorNumber and getColorIndex
#    functions that prevented function calls from returning.  Similar issues 
#    would exist in the iGyro functions being range-checked.  
# 02-Oct-19 <jwa> - Restructured and added comments; Modified all functions to
#	 check the values received from the sensor and to retake the reading if any
#	 value is out-of-range. (There is apparently some bus-stuffing when the 
#	 Color Sensor and the IntGyro are used at the same time.)
#
#===============================================================================

import time

class color:
	obj	 = None 
	addr = None 
	
	ACTIVE	 = 0x00
	PASSIVE	 = 0x01
	FIFTY_HZ = 0x35 
	SIXTY_HZ = 0x36 
	BLACKBAL = 0x42
	WHITEBAL = 0x43

	
	def __init__(self, main_obj, i2c_addr=0x3C):
		self.obj = main_obj
		self.addr = i2c_addr
		
	#def __del__(self):


#---[ colorSetup - Initializes sensor Active/Passive & 50/60Hz ]---
#
	def colorSetup(self, mode, rate=SIXTY_HZ):
		if((mode == self.ACTIVE) or (mode == self.PASSIVE)):		 
			self.obj.i2cWrite(self.addr, 0x03, [mode])
			time.sleep(0.01)		
		if((rate == self.FIFTY_HZ) or (rate == self.SIXTY_HZ)):
			self.obj.i2cWrite(self.addr, 0x03, [rate])
			while(self.obj.i2cRead(self.addr, 0x03, 1)[0] == rate): pass 
		return


#---[ whiteBalance - Performs White Balance on Sensor ]---
#
	def whiteBalance(self):
		self.obj.i2cWrite(self.addr, 0x03, [self.WHITEBAL])
		while(self.obj.i2cRead(self.addr, 0x03, 1)[0] == self.WHITEBAL): pass 
		return
  
  
#---[ blackBalance - Performs Black level calibration on Sensor ]---
#
	def blackBalance(self):
		self.obj.i2cWrite(self.addr, 0x03, [self.BLACKBAL])
		while(self.obj.i2cRead(self.addr, 0x03, 1)[0] == self.BLACKBAL): pass 
		return

  
#---[ getColorNumber - Returns Approximate color as a number from 0 to 16 ]---
#	Check and limit value to [0..16]
#
	def getColorNumber(self):
		DataOK = False
		while ( DataOK == False ):
			data = self.obj.i2cRead(self.addr, 0x04, 1)[0]
			if ( data <= 16 ):
				DataOK = True
		return data
 
  
#---[ getColorValue - Returns 8-bit R G B W Values ]---
#	Can only return 8-bit values, no need to check since 
#	we wouldn't know how to adjust them
	def getColorValue(self):
		return self.obj.i2cRead(self.addr, 0x05, 4)
   
   
#---[ getColorIndex - Returns Approximate color as 6-bit value (0 - 63) ]---
#	Check and limit to [0..63]
	def getColorIndex(self):
		DataOK = False
		while ( DataOK == False ):
			data = self.obj.i2cRead(self.addr, 0x09, 1)[0]
			if ( data <= 63 ):
				DataOK = True
		return data
   
   
#---[ getRGBIndex - Returns 8-bit R G B Values ]---
#	Can only return 8-bit values, no need to check since 
#	we wouldn't know how to adjust them
	def getRGBIndex(self):
		return self.obj.i2cRead(self.addr, 0x0A, 3)
 

#---[ getColorReading - Returns 16-bit R G B W Values ]---
#	Can return 16-bit values, no need to check since 
#	we wouldn't know how to adjust them
	def getColorReading(self):
		data  = self.obj.i2cRead(self.addr, 0x0E, 8)
		red	  = (data[1] << 8) | data[0]
		green = (data[3] << 8) | data[2]
		blue  = (data[5] << 8) | data[4]
		white = (data[7] << 8) | data[6]
		return [red, green, blue, white]
 
 
#---[ getColorNormalized - Returns 16-bit R G B W Values ]---
#	Can return 16-bit values, no need to check since 
#	we wouldn't know how to adjust them
	def getColorNormalized(self):
		data  = self.obj.i2cRead(self.addr, 0x16, 8)
		red	  = (data[1] << 8) | data[0]
		green = (data[3] << 8) | data[2]
		blue  = (data[5] << 8) | data[4]
		white = (data[7] << 8) | data[6]
		return [red, green, blue, white]

#---[ End of Color.py ]---

