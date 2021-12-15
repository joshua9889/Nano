"""
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
   
   Dependencies:
   apt-get install python-dev 
   pip install remi     (Unless locally packaged)  
"""

################################################################################
# Revision History:
#
# 27-Jul-2018 <jwa> 
#	changed \n to \r\n on file outputs for crlf eols (be careful not to 
#	  change this on the screen and/or profile file statements!)
#
################################################################################


import remi.gui as gui
from remi import start, App
from threading import Timer, Thread
import Fusion
import random
import time
import os 
import traceback
import subprocess

from dataLogger import user_name
        
class sensorFunctions():
    def __init__(self):
        self.f = Fusion.driver()
        self.fColor = None
        self.fCompass = None
        self.fIntGyro = None
        self.fLocator = None
        self.fRange = None
        self.fSeeker = None
        self.functions = {
            'digitalRead':self.digitalRead,
            'analogRead':self.analogRead,
            'getColorNumber':self.getColorNumber,
            'getColorValue_R':self.getColorValue_R,
            'getColorValue_G':self.getColorValue_G,
            'getColorValue_B':self.getColorValue_B,
            'getColorValue_W':self.getColorValue_W,
            'getColorIndex':self.getColorIndex,
            'getRGBIndex_R':self.getRGBIndex_R,
            'getRGBIndex_G':self.getRGBIndex_G,
            'getRGBIndex_B':self.getRGBIndex_B,
            'getColorReading_R':self.getColorReading_R,
            'getColorReading_G':self.getColorReading_G,
            'getColorReading_B':self.getColorReading_B,
            'getColorReading_W':self.getColorReading_W,
            'getColorNormalized_R':self.getColorNormalized_R,
            'getColorNormalized_G':self.getColorNormalized_G,
            'getColorNormalized_B':self.getColorNormalized_B,
            'getColorNormalized_W':self.getColorNormalized_W,
            'getHeading':self.getHeading,
            'getAccelerometer_X':self.getAccelerometer_X,
            'getAccelerometer_Y':self.getAccelerometer_Y,
            'getAccelerometer_Z':self.getAccelerometer_Z,
            'getMagnetometer_X':self.getMagnetometer_X,
            'getMagnetometer_Y':self.getMagnetometer_Y,
            'getMagnetometer_Z':self.getMagnetometer_Z,
            'getDegrees':self.getDegrees,
            'L_getHeading_600':self.L_getHeading_600,
            'L_getHeading_1200':self.L_getHeading_1200,
            'L_getIntensity_600':self.L_getIntensity_600,
            'L_getIntensity_1200':self.L_getIntensity_1200,
            'ultrasonic':self.ultrasonic,
            'optical':self.optical,
            'S_getHeading_600':self.S_getHeading_600,
            'S_getHeading_1200':self.S_getHeading_1200,
            'S_getIntensity_600':self.S_getIntensity_600,
            'S_getIntensity_1200':self.S_getIntensity_1200,
            'S_getLeftRaw_600':self.S_getLeftRaw_600,
            'S_getLeftRaw_1200':self.S_getLeftRaw_1200,
            'S_getRightRaw_1200':self.S_getRightRaw_1200,
            'S_getRightRaw_1200':self.S_getRightRaw_1200            
            }
        
    # Digital -----------------------------------------------------------------    
    def digitalRead(self, port):
        port = 0x0001 << port 
        self.f.digitalState(port, self.f.INPUT)
        return self.f.digitalRead(port);
        
    # Analog ------------------------------------------------------------------
    def analogRead(self, port):
        port = (0x0001 << port) | 0x0100
        return self.f.analogRead(port);
    
    # Color -------------------------------------------------------------------
    def getColorNumber(self):
        if(self.fColor == None): self.fColor = Fusion.color(self.f)
        return self.fColor.getColorNumber();
        
    def getColorValue_R(self):
        if(self.fColor == None): self.fColor = Fusion.color(self.f)
        return self.fColor.getColorValue()[0];
        
    def getColorValue_G(self):
        if(self.fColor == None): self.fColor = Fusion.color(self.f)
        return self.fColor.getColorValue()[1];
        
    def getColorValue_B(self):
        if(self.fColor == None): self.fColor = Fusion.color(self.f)
        return self.fColor.getColorValue()[2];
    
    def getColorValue_W(self):
        if(self.fColor == None): self.fColor = Fusion.color(self.f)
        return self.fColor.getColorValue()[3];
        
    def getColorIndex(self):
        if(self.fColor == None): self.fColor = Fusion.color(self.f)
        return self.fColor.getColorIndex();
        
    def getRGBIndex_R(self):
        if(self.fColor == None): self.fColor = Fusion.color(self.f)
        return self.fColor.getRGBIndex()[0];
    
    def getRGBIndex_G(self):
        if(self.fColor == None): self.fColor = Fusion.color(self.f)
        return self.fColor.getRGBIndex()[1];
        
    def getRGBIndex_B(self):
        if(self.fColor == None): self.fColor = Fusion.color(self.f)
        return self.fColor.getRGBIndex()[2];
        
    def getColorReading_R(self):
        if(self.fColor == None): self.fColor = Fusion.color(self.f)
        return self.fColor.getColorReading()[0];
        
    def getColorReading_G(self):
        if(self.fColor == None): self.fColor = Fusion.color(self.f)
        return self.fColor.getColorReading()[1];
        
    def getColorReading_B(self):
        if(self.fColor == None): self.fColor = Fusion.color(self.f)
        return self.fColor.getColorReading()[2];
        
    def getColorReading_W(self):
        if(self.fColor == None): self.fColor = Fusion.color(self.f)
        return self.fColor.getColorReading()[3];
        
    def getColorNormalized_R(self):
        if(self.fColor == None): self.fColor = Fusion.color(self.f)
        return self.fColor.getColorNormalized()[0];
        
    def getColorNormalized_G(self):
        if(self.fColor == None): self.fColor = Fusion.color(self.f)
        return self.fColor.getColorNormalized()[1];
        
    def getColorNormalized_B(self):
        if(self.fColor == None): self.fColor = Fusion.color(self.f)
        return self.fColor.getColorNormalized()[2];
        
    def getColorNormalized_W(self):
        if(self.fColor == None): self.fColor = Fusion.color(self.f)
        return self.fColor.getColorNormalized()[3];
    
    # Compass -----------------------------------------------------------------
    def getHeading(self):
        if(self.fCompass == None): self.fCompass = Fusion.compass(self.f)
        return self.fCompass.getHeading();
        
    def getAccelerometer_X(self):
        if(self.fCompass == None): self.fCompass = Fusion.compass(self.f)
        return self.fCompass.getAccelerometer()[0];
        
    def getAccelerometer_Y(self):
        if(self.fCompass == None): self.fCompass = Fusion.compass(self.f)
        return self.fCompass.getAccelerometer()[1];
        
    def getAccelerometer_Z(self):
        if(self.fCompass == None): self.fCompass = Fusion.compass(self.f)
        return self.fCompass.getAccelerometer()[2];
        
    def getMagnetometer_X(self):
        if(self.fCompass == None): self.fCompass = Fusion.compass(self.f)
        return self.fCompass.getMagnetometer()[0];
        
    def getMagnetometer_Y(self):
        if(self.fCompass == None): self.fCompass = Fusion.compass(self.f)
        return self.fCompass.getMagnetometer()[1];
        
    def getMagnetometer_Z(self):
        if(self.fCompass == None): self.fCompass = Fusion.compass(self.f)
        return self.fCompass.getMagnetometer()[2];
    
    # Int Gyro ----------------------------------------------------------------    
    def getDegrees(self):
        if(self.fIntGyro == None): self.fIntGyro = Fusion.intGyro(self.f)
        return self.fIntGyro.getDegrees();
        
    def getAxis_X(self):
        if(self.fIntGyro == None): self.fIntGyro = Fusion.intGyro(self.f)
        return self.fIntGyro.getAxis('X');
        
    def getAxis_Y(self):
        if(self.fIntGyro == None): self.fIntGyro = Fusion.intGyro(self.f)
        return self.fIntGyro.getAxis('Y');
        
    def getAxis_Z(self):
        if(self.fIntGyro == None): self.fIntGyro = Fusion.intGyro(self.f)
        return self.fIntGyro.getAxis('Z');
        
    def getAbsolute(self):
        if(self.fIntGyro == None): self.fIntGyro = Fusion.intGyro(self.f)
        return self.fIntGyro.getAbsolute();
    
    # Locator 360 -------------------------------------------------------------
    def L_getHeading_600(self):
        if(self.fLocator == None): self.fLocator = Fusion.locator360(self.f)
        return self.fLocator.getHeading(600);
        
    def L_getHeading_1200(self):
        if(self.fLocator == None): self.fLocator = Fusion.locator360(self.f)
        return self.fLocator.getHeading(1200);
        
    def L_getIntensity_600(self):
        if(self.fLocator == None): self.fLocator = Fusion.locator360(self.f)
        return self.fLocator.getIntensity(600);
        
    def L_getIntensity_1200(self):
        if(self.fLocator == None): self.fLocator = Fusion.locator360(self.f)
        return self.fLocator.getIntensity(600);
    
    # Range -------------------------------------------------------------------
    def ultrasonic(self):
        if(self.fRange == None): self.fRange = Fusion.range(self.f)
        return self.fRange.ultrasonic();
        
    def optical(self):  
        if(self.fRange == None): self.fRange = Fusion.range(self.f)
        return self.fRange.ultrasonic();
    
    # IR Seeker V3 ------------------------------------------------------------    
    def S_getHeading_600(self):
        if(self.fSeeker == None): self.fSeeker = Fusion.seekerV3(self.f)
        return self.fSeeker.getHeading(600);
        
    def S_getHeading_1200(self):
        if(self.fSeeker == None): self.fSeeker = Fusion.seekerV3(self.f)
        return self.fSeeker.getHeading(1200);
        
    def S_getIntensity_600(self):
        if(self.fSeeker == None): self.fSeeker = Fusion.seekerV3(self.f)
        return self.fSeeker.getIntensity(600);
        
    def S_getIntensity_1200(self):
        if(self.fSeeker == None): self.fSeeker = Fusion.seekerV3(self.f)
        return self.fSeeker.getIntensity(1200);
        
    def S_getLeftRaw_600(self):
        if(self.fSeeker == None): self.fSeeker = Fusion.seekerV3(self.f)
        return self.fSeeker.getLeftRaw(600);
        
    def S_getLeftRaw_1200(self):
        if(self.fSeeker == None): self.fSeeker = Fusion.seekerV3(self.f)
        return self.fSeeker.getLeftRaw(1200);
        
    def S_getRightRaw_600(self):
        if(self.fSeeker == None): self.fSeeker = Fusion.seekerV3(self.f)
        return self.fSeeker.getRightRaw(600);
        
    def S_getRightRaw_1200(self):
        if(self.fSeeker == None): self.fSeeker = Fusion.seekerV3(self.f)
        return self.fSeeker.getRightRaw(1200);

s = sensorFunctions()
        
def strToBool(string):
    if str(string) in ['True', 'T', 'true', 't']: return True;
    else: return False;
    
def secToStr(seconds):
    seconds = int(seconds)
    hrs = int(seconds/3600)
    seconds -= (hrs*3600)
    min = int(seconds/60)
    seconds -= min*60 
    return str(hrs).zfill(2)+':'+str(min).zfill(2)+':'+str(seconds).zfill(2);
    
def strToSec(string):
    temp = str(string).split(':')
    return (int(temp[0])*60*60) + (int(temp[1])*60) + int(temp[2]);
    
class sensorFactory():
    port_key = None 
    port_list = ['select', 'D0', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'I2C']
    port_index = None
    port_index_last = None  
    
    sensor_key = None 
    sensor_list = ['', 'Digital', 'Analog', 'Color', 'Compass', 'Int Gyro', 'Locator360', 'Range', 'SeekerV3']
    sensor_index_last = None 
    
    function_key = None
    function_list = [[''],
        ['digitalRead'],
        ['analogRead'],
        ['getColorNumber', 'getColorValue_R', 'getColorValue_G', 'getColorValue_B', 'getColorValue_W',  'getColorIndex', 'getRGBIndex_R', 'getRGBIndex_G', 'getRGBIndex_B', 'getColorReading_R', 'getColorReading_G', 'getColorReading_B', 'getColorReading_W', 'getColorNormalized_R', 'getColorNormalized_G', 'getColorNormalized_B', 'getColorNormalized_W'],
        ['getHeading', 'getAccelerometer_X', 'getAccelerometer_Y', 'getAccelerometer_Z', 'getMagnetometer_X', 'getMagnetometer_Y', 'getMagnetometer_Z'],
        ['getDegrees', 'getAxis_X', 'getAxis_Y', 'getAxis_Z', 'getAbsolute'],
        ['getHeading_600', 'getHeading_1200', 'getIntensity_600', 'getIntensity_1200'],
        ['ultrasonic', 'optical'],
        ['getHeading_600', 'getHeading_1200', 'getIntensity_600', 'getIntensity_1200', 'getLeftRaw_600', 'getLeftRaw_1200', 'getRightRaw_600', 'getRightRaw_1200']]
    function_temp = None 
        
    def __init__(self):
        self.main_container = gui.Widget(width='100%', height=40, margin='5px auto', layout_orientation=gui.Widget.LAYOUT_HORIZONTAL, style={'position': 'relative', 'top': '0px', 'left': '0px', 'display': 'block', 'overflow': 'auto', 'background-color': '#EEEEEE'})
        self.checkbox = gui.CheckBox(False, width=20, height=20, style={'position': 'absolute', 'top': '10px', 'left': '20px'})
        
        self.port_key = self.key_gen()
        self.port = gui.DropDown.new_from_list(self.port_list, width=100, height=25, style={'white-space':'pre', 'line-height': '25px', 'text-align': 'center', 'position': 'absolute', 'left': '100px', 'top':'6px', 'border-color': 'gray', 'border-width': '1px', 'border-style': 'solid'})
        self.port.set_on_change_listener(self.on_port_change)
        self.port.select_by_value('select')
        
        self.sensor_key = self.key_gen()
        self.sensor = gui.DropDown.new_from_list([''], width=150, height=25, style={'white-space':'pre', 'line-height': '25px', 'text-align': 'center', 'position': 'absolute', 'left': '250px', 'top':'6px', 'border-color': 'gray', 'border-width': '1px', 'border-style': 'solid'})
        self.sensor.set_on_change_listener(self.on_sensor_change)
        
        self.function_key = self.key_gen()
        self.function = gui.DropDown.new_from_list([''], width=250, height=25, style={'white-space':'pre', 'line-height': '25px', 'text-align': 'center', 'position': 'absolute', 'left': '450px', 'top':'6px', 'border-color': 'gray', 'border-width': '1px', 'border-style': 'solid'})
        
        self.main_container.append(self.checkbox)
        self.main_container.append(self.port, key=self.port_key)
        self.main_container.append(self.sensor, key=self.sensor_key)
        self.main_container.append(self.function, key=self.function_key)
    
    def key_gen(self):
        key = ''
        for i in range(32): key += random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        return key;
        
    def on_port_change(self, widget, value):
        self.port.style['background-color'] = 'white'
        if(self.port.get_value() != self.port_list[0]):
            self.port_index = self.port_list.index(self.port.get_value())
            if(self.port_index_last == 0): self.port_index_last = self.port_index
            
            if ((self.port_index >= 1) and (self.port_index <= 8) and (self.port_index_last >= 1) and (self.port_index_last <= 8)): 
                if(self.sensor.get_value() == ''):
                    sensor_temp = [self.sensor_list[1]]  
                    self.sensor = gui.DropDown.new_from_list(sensor_temp, width=150, height=25, style={'white-space':'pre', 'line-height': '25px', 'text-align': 'center', 'position': 'absolute', 'left': '250px', 'top':'6px', 'border-color': 'gray', 'border-width': '1px', 'border-style': 'solid'})
                    self.sensor.set_on_change_listener(self.on_sensor_change)
                    self.main_container.append(self.sensor, key=self.sensor_key)
                    function_temp = self.function_list[1]
                    self.function = gui.DropDown.new_from_list(function_temp, width=250, height=25, style={'white-space':'pre', 'line-height': '25px', 'text-align': 'center', 'position': 'absolute', 'left': '450px', 'top':'6px', 'border-color': 'gray', 'border-width': '1px', 'border-style': 'solid'})
                    self.main_container.append(self.function, key=self.function_key)
            elif((self.port_index >= 1) and (self.port_index <= 8)):
                sensor_temp = [self.sensor_list[1]]  
                self.sensor = gui.DropDown.new_from_list(sensor_temp, width=150, height=25, style={'white-space':'pre', 'line-height': '25px', 'text-align': 'center', 'position': 'absolute', 'left': '250px', 'top':'6px', 'border-color': 'gray', 'border-width': '1px', 'border-style': 'solid'})
                self.sensor.set_on_change_listener(self.on_sensor_change)
                self.main_container.append(self.sensor, key=self.sensor_key)
                function_temp = self.function_list[1]
                self.function = gui.DropDown.new_from_list(function_temp, width=250, height=25, style={'white-space':'pre', 'line-height': '25px', 'text-align': 'center', 'position': 'absolute', 'left': '450px', 'top':'6px', 'border-color': 'gray', 'border-width': '1px', 'border-style': 'solid'})
                self.main_container.append(self.function, key=self.function_key)
                
            if((self.port_index >= 9) and (self.port_index <= 16) and (self.port_index_last >= 9) and (self.port_index_last <= 16)): 
                if(self.sensor.get_value() == ''):
                    sensor_temp = [self.sensor_list[2]]
                    self.sensor = gui.DropDown.new_from_list(sensor_temp, width=150, height=25, style={'white-space':'pre', 'line-height': '25px', 'text-align': 'center', 'position': 'absolute', 'left': '250px', 'top':'6px', 'border-color': 'gray', 'border-width': '1px', 'border-style': 'solid'})
                    self.sensor.set_on_change_listener(self.on_sensor_change)                
                    self.main_container.append(self.sensor, key=self.sensor_key)
                    function_temp = self.function_list[2]
                    self.function = gui.DropDown.new_from_list(function_temp, width=250, height=25, style={'white-space':'pre', 'line-height': '25px', 'text-align': 'center', 'position': 'absolute', 'left': '450px', 'top':'6px', 'border-color': 'gray', 'border-width': '1px', 'border-style': 'solid'})
                    self.main_container.append(self.function, key=self.function_key)
            elif((self.port_index >= 9) and (self.port_index <= 16)):
                sensor_temp = [self.sensor_list[2]]
                self.sensor = gui.DropDown.new_from_list(sensor_temp, width=150, height=25, style={'white-space':'pre', 'line-height': '25px', 'text-align': 'center', 'position': 'absolute', 'left': '250px', 'top':'6px', 'border-color': 'gray', 'border-width': '1px', 'border-style': 'solid'})
                self.sensor.set_on_change_listener(self.on_sensor_change)                
                self.main_container.append(self.sensor, key=self.sensor_key)
                function_temp = self.function_list[2]
                self.function = gui.DropDown.new_from_list(function_temp, width=250, height=25, style={'white-space':'pre', 'line-height': '25px', 'text-align': 'center', 'position': 'absolute', 'left': '450px', 'top':'6px', 'border-color': 'gray', 'border-width': '1px', 'border-style': 'solid'})
                self.main_container.append(self.function, key=self.function_key)
                
            # if((self.port_index >= 17) and (self.port_index_last >= 17)): 
                # print "this happened here"
                # pass 
            elif(self.port_index >= 17):
                sensor_temp = self.sensor_list[3:]
                self.sensor = gui.DropDown.new_from_list(sensor_temp, width=150, height=25, style={'white-space':'pre', 'line-height': '25px', 'text-align': 'center', 'position': 'absolute', 'left': '250px', 'top':'6px', 'border-color': 'gray', 'border-width': '1px', 'border-style': 'solid'})
                self.sensor.set_on_change_listener(self.on_sensor_change)
                self.sensor.select_by_value(sensor_temp[0])
                self.main_container.append(self.sensor, key=self.sensor_key)
                sensor_index = self.sensor_list.index(self.sensor.get_value())
                function_temp = self.function_list[sensor_index]
                self.function = gui.DropDown.new_from_list(function_temp, width=250, height=25, style={'white-space':'pre', 'line-height': '25px', 'text-align': 'center', 'position': 'absolute', 'left': '450px', 'top':'6px', 'border-color': 'gray', 'border-width': '1px', 'border-style': 'solid'})
                self.function.select_by_value(function_temp[0])
                self.main_container.append(self.function, key=self.function_key)      
                
            self.port_index_last = self.port_index
            
        else:
            self.sensor = gui.DropDown.new_from_list([''], width=150, height=25, style={'white-space':'pre', 'line-height': '25px', 'text-align': 'center', 'position': 'absolute', 'left': '250px', 'top':'6px', 'border-color': 'gray', 'border-width': '1px', 'border-style': 'solid'})
            self.main_container.append(self.sensor, key=self.sensor_key)
            
            self.function = gui.DropDown.new_from_list([''], width=250, height=25, style={'white-space':'pre', 'line-height': '25px', 'text-align': 'center', 'position': 'absolute', 'left': '450px', 'top':'6px', 'border-color': 'gray', 'border-width': '1px', 'border-style': 'solid'})
            self.main_container.append(self.function, key=self.function_key)            
            self.port_index_last = 0
            
        return;
            
    def on_sensor_change(self, widget, value):
        sensor_index = self.sensor_list.index(self.sensor.get_value())
        function_temp = self.function_list[sensor_index]
        self.function = gui.DropDown.new_from_list(function_temp, width=250, height=25, style={'white-space':'pre', 'line-height': '25px', 'text-align': 'center', 'position': 'absolute', 'left': '450px', 'top':'6px', 'border-color': 'gray', 'border-width': '1px', 'border-style': 'solid'})
        self.function.select_by_value(function_temp[0])
        self.main_container.append(self.function, key=self.function_key)        
        return;
        
class realTimeDataFactory():
    def __init__(self):
        self.container = gui.Widget(width='100%', height=40, margin='5px auto', layout_orientation=gui.Widget.LAYOUT_HORIZONTAL, style={'position': 'relative', 'top': '0px', 'left': '0px', 'display': 'block', 'overflow': 'auto', 'background-color': '#EEEEEE'})
        self.port = gui.TextInput(single_line=True, width=40, height=25, style={'line-height': '25px', 'text-align': 'center', 'position': 'relative', 'left': '10px', 'top':'6px', 'border-color': 'gray', 'border-width': '1px', 'border-style': 'solid'})
        self.container.append(self.port)
        self.sensor = gui.TextInput(single_line=True, width=230, height=25, style={'line-height': '25px', 'text-align': 'center', 'position': 'relative', 'left': '30px', 'top':'6px', 'border-color': 'gray', 'border-width': '1px', 'border-style': 'solid'})
        self.container.append(self.sensor)
        self.data = gui.TextInput(single_line=True, width=70, height=25, style={'line-height': '25px', 'text-align': 'center', 'position': 'relative', 'left': '50px', 'top':'6px', 'border-color': 'gray', 'border-width': '1px', 'border-style': 'solid'})
        self.container.append(self.data)
        
class DataLogger(App):
    def __init__(self, *args):
        my_css_head = """
            <link rel="stylesheet" href="style.css" type="text/css">
            """
        res_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'res')
        super(DataLogger, self).__init__(*args, static_file_path=res_path, css_head=my_css_head)
        
        # Variables
        self.update_time = True
        self.write_file = False
        self.sample_update = False
        self.sample_file_write = False 
        self.start_time_var = None 
        self.countdown_var = None 
        self.duration_var = None
        self.enabled_sensors = None 
        self.file_delimiter = None 
        self.next_sample = None         
        self.time_var = None 
        self.file_size_var = None
        
        # Set the user file path 
        try:
            #self.user_file_path = os.path.join(os.path.abspath("."), 'filesystem')
            if (os.path.isdir('/usr/Fusion/FusionServer/Src')):
                self.user_file_path = '/usr/Fusion/FusionServer/Src/app/filesystem/'+str(user_name)+'/Logging'
                print self.user_file_path 
            else:
                self.user_file_path = '/usr/Fusion/FusionServer/Build/app/filesystem/'+str(user_name)+'/Logging'
                print self.user_file_path 
            os.mkdir(self.user_file_path) 
        except:
            pass #print traceback.format_exc(1) 
        
# ---------------------------------------------------------------------------------------------------------       
    def main(self):
        # Build main window      
        #--------------------------------------------------------------------------------------------------
        # Make a vertical container to append layers to
        self.vertical_container = gui.Widget(width=853, height=690, margin='0px auto', style={'display': 'block', 'overflow': 'hidden'})
        
        #--------------------------------------------------------------------------------------------------
        # Top Menu Bar
        self.menu = gui.Menu(width='100%', height='30px', style={'background-color': '#009688'})
        self.m1 = gui.MenuItem('Profile', width=100, height=30)
        self.m10 = gui.MenuItem('New', width=100, height=30)
        self.m10.set_on_click_listener(self.on_profile_new_click)
        self.m11 = gui.MenuItem('Save', width=100, height=30)     
        self.m11.set_on_click_listener(self.on_profile_save_click)
        self.m12 = gui.MenuItem('Load', width=100, height=30)
        self.m12.set_on_click_listener(self.on_profile_load_click)
        self.m1.append(self.m10)
        self.m1.append(self.m11)
        self.m1.append(self.m12)
        self.menu.append(self.m1)
        self.m2 = gui.MenuItem('File Manager', width=100, height=30)
        self.m21 = gui.MenuItem('Export', width=100, height=30)
        self.m21.set_on_click_listener(self.on_export_click)
        self.m22 = gui.MenuItem('Delete', width=100, height=30)
        self.m22.set_on_click_listener(self.on_delete_click)
        self.m2.append(self.m21)
        self.m2.append(self.m22)
        self.menu.append(self.m2)
        self.menu.append(gui.Label('Fusion Datalogging Tool V1.0', height=30, style={'white-space':'pre', 'position':'relative', 'top':'3px', 'left':'195px', 'font-size':'20px', 'font-weight':'bold'}))
        self.menubar = gui.MenuBar(width='100%', height='30px')
        self.menubar.append(self.menu)
        self.vertical_container.append(self.menubar)
        
        #--------------------------------------------------------------------------------------------------
        # Setup Container
        self.setup_container = gui.Widget(width='99%', height=185, margin='5px auto', style={'display': 'block', 'overflow': 'auto', 'text-align': 'left', 'border-color': "#c0c0c0", 'border-width': '2px', 'border-style': 'solid'})                   
        
        # Setup top label 
        self.setup_label = gui.Label(" Sampling Parameters", width='100%', height=25, style={'display': 'block', 'overflow': 'auto', 'white-space': 'pre', 'text-align': 'left', 'color': 'white', 'background-color': '#009688', 'font-weight':'bold'})                 
         
        # Horizontal container for two columns 
        self.setup_horizontal = gui.Widget(width='100%', height=160, layout_orientation=gui.Widget.LAYOUT_HORIZONTAL)
        self.setup_left_column = gui.Widget(width='50%', height='100%')
        self.setup_right_column = gui.Widget(width='50%', height='100%')
        
        # Log start
        self.setup_start_horizontal = gui.Widget(width='100%', height=40, layout_orientation=gui.Widget.LAYOUT_HORIZONTAL, style={'position': 'relative', 'top': '0px', 'left': '0px', 'display': 'block', 'overflow': 'auto'})
        self.setup_start_horizontal.append(gui.Label(' Start Delay =', height=25, style={'white-space': 'pre', 'position': 'relative', 'left': '10px', 'top':'6px'}))
        self.setup_start_entry = gui.TextInput(single_line=True, hint='H:M:S', width=80, height=25, style={'line-height': '25px', 'text-align': 'center', 'position': 'absolute', 'left': '120px', 'top':'6px', 'border-color': 'gray', 'border-width': '1px', 'border-style': 'solid'})
        self.setup_start_entry.set_text('00:00:00')
        self.setup_start_entry.set_on_blur_listener(self.on_setup_start_entry_blur)
        self.setup_start_horizontal.append(self.setup_start_entry)
        self.setup_start_horizontal.append(gui.Label('Hr:Min:Sec', height=25, style={'white-space': 'pre', 'position': 'absolute', 'left': '210px', 'top':'8px'}))
        self.setup_left_column.append(self.setup_start_horizontal) 
        
        # Log duration 
        self.setup_duration_horizontal = gui.Widget(width='100%', height=40, layout_orientation=gui.Widget.LAYOUT_HORIZONTAL, style={'position': 'relative', 'top': '0px', 'left': '0px', 'display': 'block', 'overflow': 'auto'})
        self.setup_duration_horizontal.append(gui.Label(' Duration =', height=25, style={'white-space': 'pre', 'position': 'relative', 'left': '10px', 'top':'6px'}))
        self.setup_duration_entry = gui.TextInput(single_line=True, hint='H:M:S', width=80, height=25, style={'line-height': '25px', 'text-align': 'center', 'position': 'absolute', 'left': '120px', 'top':'6px', 'border-color': 'gray', 'border-width': '1px', 'border-style': 'solid'})
        self.setup_duration_entry.set_text('00:00:00')
        self.setup_duration_entry.set_on_blur_listener(self.on_setup_duration_entry_blur)
        self.setup_duration_horizontal.append(self.setup_duration_entry)
        self.setup_duration_horizontal.append(gui.Label('Hr:Min:Sec', height=25, style={'white-space': 'pre', 'position': 'absolute', 'left': '210px', 'top':'8px'}))
        self.setup_left_column.append(self.setup_duration_horizontal)
        
        # Sample period
        self.setup_period_horizontal = gui.Widget(width='100%', height=40, layout_orientation=gui.Widget.LAYOUT_HORIZONTAL, style={'position': 'relative', 'top': '0px', 'left': '0px', 'display': 'block', 'overflow': 'auto'})
        self.setup_period_horizontal.append(gui.Label(' Period =', height=25, style={'white-space': 'pre', 'position': 'relative', 'left': '10px', 'top':'6px'}))
        self.setup_period_entry = gui.TextInput(single_line=True, hint='Seconds (float)', width=80, height=25, style={'line-height': '25px', 'text-align': 'center', 'position': 'absolute', 'left': '120px', 'top':'6px', 'border-color': 'gray', 'border-width': '1px', 'border-style': 'solid'})
        self.setup_period_entry.set_text('0.1')
        self.setup_period_entry.set_on_blur_listener(self.on_setup_period_entry_blur)
        self.setup_period_horizontal.append(self.setup_period_entry)
        self.setup_period_horizontal.append(gui.Label('Seconds (float)', height=25, style={'white-space': 'pre', 'position': 'absolute', 'left': '210px', 'top':'8px'}))
        self.setup_left_column.append(self.setup_period_horizontal)
        
        # Maximum file size 
        self.setup_filesize_horizontal = gui.Widget(width='100%', height=40, layout_orientation=gui.Widget.LAYOUT_HORIZONTAL, style={'position': 'relative', 'top': '0px', 'left': '0px', 'display': 'block', 'overflow': 'auto'})
        self.setup_filesize_horizontal.append(gui.Label(' Max Filesize =', height=25, style={'white-space': 'pre', 'position': 'relative', 'left': '10px', 'top':'6px'}))
        self.setup_filesize_entry = gui.TextInput(single_line=True, hint='Seconds (float)', width=80, height=25, style={'line-height': '25px', 'text-align': 'center', 'position': 'absolute', 'left': '120px', 'top':'6px', 'border-color': 'gray', 'border-width': '1px', 'border-style': 'solid'})
        self.setup_filesize_entry.set_text('32000000')
        self.setup_filesize_entry.set_on_blur_listener(self.on_setup_filesize_entry_blur)
        self.setup_filesize_horizontal.append(self.setup_filesize_entry)
        self.setup_filesize_horizontal.append(gui.Label('Bytes', height=25, style={'white-space': 'pre', 'position': 'absolute', 'left': '210px', 'top':'8px'}))
        self.setup_left_column.append(self.setup_filesize_horizontal)
        
        # File name 
        self.setup_file_horizontal = gui.Widget(width='100%', height=40, layout_orientation=gui.Widget.LAYOUT_HORIZONTAL, style={'position': 'relative', 'top': '0px', 'left': '0px', 'display': 'block', 'overflow': 'auto'})
        self.setup_file_label = gui.Label(' File Name =', height=25, style={'white-space': 'pre', 'position': 'relative', 'left': '10px', 'top':'6px'})
        self.setup_file_entry = gui.TextInput(single_line=True, width=200, height=25, style={'line-height': '25px', 'text-align': 'center', 'position': 'absolute', 'left': '120px', 'top':'6px', 'border-color': 'gray', 'border-width': '1px', 'border-style': 'solid'})
        self.setup_file_entry.set_on_blur_listener(self.on_setup_file_entry_blur)
        self.setup_file_extension = gui.Label('.txt', height=25, style={'white-space': 'pre', 'position': 'absolute', 'left': '325px', 'top':'8px'})
        self.setup_file_horizontal.append(self.setup_file_label)
        self.setup_file_horizontal.append(self.setup_file_entry)
        self.setup_file_horizontal.append(self.setup_file_extension)
        self.setup_right_column.append(self.setup_file_horizontal)
        
        # Column Labels and Quote strings 
        self.setup_column_horizontal = gui.Widget(width='100%', height=40, layout_orientation=gui.Widget.LAYOUT_HORIZONTAL, style={'position': 'relative', 'top': '0px', 'left': '0px', 'display': 'block', 'overflow': 'auto'})
        self.setup_column_checkbox = gui.CheckBoxLabel('  Column Labels ', height=25, style={'white-space': 'pre', 'position': 'absolute', 'left': '10px', 'top':'6px'})
        self.setup_quote_checkbox = gui.CheckBoxLabel('   "Quote" strings', height=25, style={'white-space': 'pre', 'position': 'absolute', 'left': '150px', 'top':'6px'})
        self.setup_column_horizontal.append(self.setup_column_checkbox)
        self.setup_column_horizontal.append(self.setup_quote_checkbox)
        self.setup_right_column.append(self.setup_column_horizontal)
        
        # Delimiter
        self.setup_delimiter_horizontal = gui.Widget(width='100%', height=40, layout_orientation=gui.Widget.LAYOUT_HORIZONTAL, style={'position': 'relative', 'top': '0px', 'left': '0px', 'display': 'block', 'overflow': 'auto'})
        self.setup_delimiter_label = gui.Label(' Delimiter type = ', height=25, style={'white-space': 'pre', 'position': 'relative', 'left': '10px', 'top':'6px'})
        self.setup_delimiter_dropdown = gui.DropDown.new_from_list(('Tab', 'Comma', 'SemiColon'), width=100, height=25, style={'line-height': '25px', 'text-align': 'center', 'position': 'absolute', 'left': '120px', 'top':'6px', 'border-color': 'gray', 'border-width': '1px', 'border-style': 'solid'})
        self.setup_delimiter_dropdown.select_by_value('Tab')
        self.setup_delimiter_horizontal.append(self.setup_delimiter_label)
        self.setup_delimiter_horizontal.append(self.setup_delimiter_dropdown)
        self.setup_right_column.append(self.setup_delimiter_horizontal)
        
        # Start sampling button        
        self.setup_begin_horizontal = gui.Widget(width='100%', height=40, layout_orientation=gui.Widget.LAYOUT_HORIZONTAL, style={'position': 'relative', 'top': '0px', 'left': '0px', 'display': 'block', 'overflow': 'auto'})
        self.setup_begin_button = gui.Button("Start Sampling", width=300, height=25, style={'line-height': '25px', 'text-align': 'center', 'position': 'relative', 'left': '40px', 'top':'7px', 'border-color': 'gray', 'border-width': '1px', 'border-style': 'solid', 'font-size':'18px', 'font-weight':'bold'})
        self.setup_begin_button.set_on_click_listener(self.on_begin_pressed)
        self.setup_begin_horizontal.append(self.setup_begin_button)
        self.setup_right_column.append(self.setup_begin_horizontal) 
        
        # Append containers 
        self.setup_container.append(self.setup_label)
        self.setup_container.append(self.setup_horizontal)        
        self.setup_horizontal.append(self.setup_left_column)           
        self.setup_horizontal.append(self.setup_right_column)
        self.vertical_container.append(self.setup_container)
        
        #--------------------------------------------------------------------------------------------------
        # Sensor Container 
        self.sensor_container = gui.Widget(width='99%', height=450, margin='5px auto', style={'text-align': 'left', 'border-color': "#c0c0c0", 'border-width': '2px', 'border-style': 'solid'})                   
        
        # Sensor top label 
        self.sensor_label = gui.Label(" Sensor Setup", width='100%', height=25, style={'white-space': 'pre', 'text-align': 'left', 'color': 'white', 'background-color': '#009688', 'font-weight':'bold'})
        self.sensor_container.append(self.sensor_label)
        
        # Sensor window description bar 
        self.sensor_description = gui.Widget(width='100%', height=30, layout_orientation=gui.Widget.LAYOUT_HORIZONTAL, style={'position': 'relative', 'top': '0px', 'left': '0px', 'display': 'block', 'overflow': 'auto', 'background-color': '#AAAAAA'}) 
        self.sensor_description.append(gui.Label("Enable", style={'white-space': 'pre', 'position': 'absolute', 'left': '10px', 'top':'2px', 'color':'white'}))
        self.sensor_description.append(gui.Label("Port", style={'white-space': 'pre', 'position': 'absolute', 'left': '135px', 'top':'2px', 'color':'white'}))
        self.sensor_description.append(gui.Label("Sensor", style={'white-space': 'pre', 'position': 'absolute', 'left': '300px', 'top':'2px', 'color':'white'}))
        self.sensor_description.append(gui.Label("Data Function", style={'white-space': 'pre', 'position': 'absolute', 'left': '530px', 'top':'2px', 'color':'white'}))
        
        self.sensor_container.append(self.sensor_description)
        
        # Build sensor list 
        self.sensor_objects = []
        for i in range(8): self.sensor_objects.append(sensorFactory())
        
        self.sensor_container.append(self.sensor_objects[0].main_container)
        self.sensor_container.append(self.sensor_objects[1].main_container)
        self.sensor_container.append(self.sensor_objects[2].main_container)
        self.sensor_container.append(self.sensor_objects[3].main_container)
        self.sensor_container.append(self.sensor_objects[4].main_container)
        self.sensor_container.append(self.sensor_objects[5].main_container)
        self.sensor_container.append(self.sensor_objects[6].main_container)
        self.sensor_container.append(self.sensor_objects[7].main_container)
        self.vertical_container.append(self.sensor_container)
        
# ---------------------------------------------------------------------------------------------------------
        # Build sample window
        #--------------------------------------------------------------------------------------------------
        # Make a vertical container to append layers to
        self.sample_container = gui.Widget(width=853, height=690, margin='0px auto', style={'display': 'block', 'overflow': 'hidden'})
        
        self.sample_container.append(gui.Label(" Sampling progress", width='100%', height=25, style={'display': 'block', 'overflow': 'auto', 'white-space': 'pre', 'text-align': 'left', 'color': 'white', 'background-color': '#009688', 'font-weight':'bold'}))
        
        #--------------------------------------------------------------------------------------------------
        # Top Container 
        self.sample_top_container = gui.Widget(width='99%', height=160, margin='5px auto', layout_orientation=gui.Widget.LAYOUT_HORIZONTAL, style={'display': 'block', 'overflow': 'auto', 'text-align': 'left', 'border-color': "#c0c0c0", 'border-width': '2px', 'border-style': 'solid'})                   
        
        # Horizontal container for two columns 
        self.sample_top_left = gui.Widget(width='50%', height='100%')
        self.sample_top_right = gui.Widget(width='50%', height='100%')
        
        # Countdown timer to start 
        self.sample_countdown = gui.Widget(width='100%', height=40, layout_orientation=gui.Widget.LAYOUT_HORIZONTAL, style={'position': 'relative', 'top': '0px', 'left': '0px', 'display': 'block', 'overflow': 'auto'})
        self.sample_countdown.append(gui.Label(' Start Countdown =', height=25, style={'white-space': 'pre', 'position': 'relative', 'left': '10px', 'top':'6px'}))     
        self.sample_countdown_entry = gui.TextInput(single_line=True, hint='00:00:00', width=80, height=25, style={'line-height': '25px', 'text-align': 'center', 'position': 'absolute', 'left': '162px', 'top':'6px', 'border-color': 'gray', 'border-width': '1px', 'border-style': 'solid'})
        self.sample_countdown_entry.set_enabled(False)
        self.sample_countdown.append(self.sample_countdown_entry)
        self.sample_top_left.append(self.sample_countdown)
        
        # Time Remaining 
        self.sample_time_remaining = gui.Widget(width='100%', height=40, layout_orientation=gui.Widget.LAYOUT_HORIZONTAL, style={'position': 'relative', 'top': '0px', 'left': '0px', 'display': 'block', 'overflow': 'auto'})
        self.sample_time_remaining.append(gui.Label(' Time Remaining =', height=25, style={'white-space': 'pre', 'position': 'relative', 'left': '10px', 'top':'6px'}))  
        self.sample_time_remaining_entry = gui.TextInput(single_line=True, hint='00:00:00', width=80, height=25, style={'line-height': '25px', 'text-align': 'center', 'position': 'absolute', 'left': '162px', 'top':'6px', 'border-color': 'gray', 'border-width': '1px', 'border-style': 'solid'})
        self.sample_time_remaining_entry.set_enabled(False)
        self.sample_time_remaining.append(self.sample_time_remaining_entry)
        self.sample_top_left.append(self.sample_time_remaining)
        
        # Completion % 
        self.sample_percent_complete = gui.Widget(width='100%', height=40, layout_orientation=gui.Widget.LAYOUT_HORIZONTAL, style={'position': 'relative', 'top': '0px', 'left': '0px', 'display': 'block', 'overflow': 'auto'})
        self.sample_percent_complete.append(gui.Label(' Completion =', height=25, style={'white-space': 'pre', 'position': 'absolute', 'left': '10px', 'top':'6px'}))
        self.sample_percent_value = gui.Label('---%', height=25, style={'white-space': 'pre', 'position': 'absolute', 'left': '120px', 'top':'6px'})
        self.sample_percent_complete.append(self.sample_percent_value)        
        self.sample_percent_bar_container = gui.Widget(width=200, height=25, style={'position':'absolute', 'top':'6px', 'left':'162px', 'display': 'block', 'overflow': 'auto', 'border-color': 'gray', 'border-width': '1px', 'border-style': 'solid'})
        self.sample_percent_bar = gui.Widget(width='23%', height='100%', style={'background-color':'green'})
        self.sample_percent_bar_container.append(self.sample_percent_bar)
        self.sample_percent_complete.append(self.sample_percent_bar_container)        
        self.sample_top_left.append(self.sample_percent_complete)
        
        # Output file name 
        self.sample_file_name = gui.Widget(width='100%', height=40, layout_orientation=gui.Widget.LAYOUT_HORIZONTAL, style={'position': 'relative', 'top': '0px', 'left': '0px', 'display': 'block', 'overflow': 'auto'})
        self.sample_file_name.append(gui.Label(' Output File =', height=25, style={'white-space': 'pre', 'position': 'relative', 'left': '10px', 'top':'6px'}))
        self.sample_file_name_entry = gui.TextInput(single_line=True, width=200, height=25, style={'line-height': '25px', 'text-align': 'center', 'position': 'absolute', 'left': '110px', 'top':'6px', 'border-color': 'gray', 'border-width': '1px', 'border-style': 'solid'})
        self.sample_file_name_entry.set_enabled(False)
        self.sample_file_name.append(self.sample_file_name_entry)
        self.sample_file_name_size = gui.Label('0kb', height=25, style={'white-space': 'pre', 'position': 'relative', 'left': '240px', 'top':'7px'})
        self.sample_file_name.append(self.sample_file_name_size)
        self.sample_top_right.append(self.sample_file_name)
        
        #--------------------------------------------------------------------------------------------------
        # Bottom Container 
        self.sample_bottom_container = gui.Widget(width='99%', height=430, layout_orientation=gui.Widget.LAYOUT_HORIZONTAL, margin='5px auto', style={'text-align': 'left', 'border-color': "#c0c0c0", 'border-width': '2px', 'border-style': 'solid'})                   
        
        # Setup left side 
        self.sample_bottom_left = gui.Widget(width='49%', height=420, style={'position':'relative', 'top':'3px', 'left':'3px', 'border-color': "#c0c0c0", 'border-width': '2px', 'border-style': 'solid'})
        
        # Setup bottom left heading 
        self.sample_bottom_left.append(gui.Label(" Real-time sensor data", width='100%', height=25, style={'display': 'block', 'overflow': 'auto', 'white-space': 'pre', 'text-align': 'left', 'color': 'white', 'background-color': '#009688', 'font-weight':'bold'}))
        
        # Real-time description heading
        self.realtime_description = gui.Widget(width='100%', height=30, layout_orientation=gui.Widget.LAYOUT_HORIZONTAL, style={'position': 'relative', 'top': '0px', 'left': '0px', 'display': 'block', 'overflow': 'auto', 'background-color': '#AAAAAA'}) 
        self.realtime_description.append(gui.Label("Port", style={'white-space': 'pre', 'position': 'absolute', 'left': '10px', 'top':'2px', 'color':'white'}))
        self.realtime_description.append(gui.Label("Sensor", style={'white-space': 'pre', 'position': 'absolute', 'left': '135px', 'top':'2px', 'color':'white'}))
        self.realtime_description.append(gui.Label("Data", style={'white-space': 'pre', 'position': 'absolute', 'left': '300px', 'top':'2px', 'color':'white'}))
        self.sample_bottom_left.append(self.realtime_description)
        
        # Build sensor list 
        self.realtime_objects = []
        for i in range(2): self.realtime_objects.append(realTimeDataFactory())
        self.sample_bottom_left.append(self.realtime_objects[0].container)
        self.sample_bottom_left.append(self.realtime_objects[1].container)
        
        # Setup right side 
        self.sample_bottom_right = gui.Widget(width='49%', height=420, style={'position':'relative', 'top':'3px', 'left':'6px', 'border-color': "#c0c0c0", 'border-width': '2px', 'border-style': 'solid'})
        
        # Setup bottom right heading 
        self.sample_bottom_right.append(gui.Label(" File output", width='100%', height=25, style={'display': 'block', 'overflow': 'auto', 'white-space': 'pre', 'text-align': 'left', 'color': 'white', 'background-color': '#009688', 'font-weight':'bold'}))
        
        # Setup text field for file output 
        self.sample_file_output = gui.TextInput(width=400, height=380, style={'overflow':'auto', 'white-space':'nowrap', 'position':'relative', 'top':'5px', 'left':'5px', 'border-color': "#c0c0c0", 'border-width': '2px', 'border-style': 'solid'})
        # tag = gui.Tag(_type='script')
        # tag.add_child("javascript", """setInterval(function(){try{var temp=document.getElementById('%s'); temp.scrollTop = temp.scrollHeight;}catch(e){}}, 50);""" % (str(gui.uid(self.sample_file_output))))
        # self.vertical_container.add_child('text_area_update', tag)
        self.sample_bottom_right.append(self.sample_file_output)
        
        #--------------------------------------------------------------------------------------------------
        # Bottom sample button bar
        self.sample_button_container = gui.Widget(width='99%', height=45, margin='5px auto', layout_orientation=gui.Widget.LAYOUT_HORIZONTAL, style={'border-color': "#c0c0c0", 'border-width': '2px', 'border-style': 'solid'})
        self.sample_cancel_button = gui.Button("Cancel", width=300, height=30, style={'line-height': '25px', 'text-align': 'center', 'position': 'relative', 'left': '80px', 'top':'7px', 'border-color': 'gray', 'border-width': '1px', 'border-style': 'solid', 'font-size':'18px', 'font-weight':'bold'})
        self.sample_cancel_button.set_on_click_listener(self.on_sample_cancel_click)
        self.sample_start_button = gui.Button("Start Now", width=300, height=30, style={'line-height': '25px', 'text-align': 'center', 'position': 'relative', 'left': '150px', 'top':'7px', 'border-color': 'gray', 'border-width': '1px', 'border-style': 'solid', 'font-size':'18px', 'font-weight':'bold'})
        self.sample_start_button.set_on_click_listener(self.on_sample_start_click)
        self.sample_button_container.append(self.sample_cancel_button)
        self.sample_button_container.append(self.sample_start_button)
        
        #--------------------------------------------------------------------------------------------------
        # Append sample containers
        self.sample_container.append(self.sample_top_container)
        self.sample_top_container.append(self.sample_top_left)
        self.sample_top_container.append(self.sample_top_right)
        self.sample_container.append(self.sample_bottom_container)
        self.sample_bottom_container.append(self.sample_bottom_left, key='realTimeWindow')
        self.sample_bottom_container.append(self.sample_bottom_right, key='fileOutputWindow')
        self.sample_container.append(self.sample_button_container)
        
        # Return application container
        return self.vertical_container;
    
    def on_profile_new_click(self, widget):
        try:
            self.set_root_widget(self.vertical_container)        
            self.setup_start_entry.set_value('00:00:00') 
            self.setup_duration_entry.set_value('00:00:00')
            self.setup_period_entry.set_value('0.1') 
            self.setup_filesize_entry.set_value('32000000')
            self.setup_column_checkbox.set_value(False)
            self.setup_quote_checkbox.set_value(False)
            self.setup_delimiter_dropdown.set_value('Tab') 
            
            for i in range(len(self.sensor_objects)):
                    self.sensor_objects[i].checkbox.set_value(False)
                    self.sensor_objects[i].port.set_value('select')
                    self.sensor_objects[i].on_port_change(None, None)
                    self.sensor_objects[i].sensor.set_value('')
                    self.sensor_objects[i].on_sensor_change(None, None)
                    self.sensor_objects[i].function.set_value('')
        except:
            print traceback.format_exc(1)
            
        return;
    
    def on_profile_save_click(self, widget):
        if(self.verify_user_inputs(file_name=False) == False): return; 
        self.profile_save_dialog = gui.InputDialog('Save Profile', 'Save the new profile as:', width=500, height=160)
        self.profile_save_dialog.set_on_confirm_value_listener(self.on_profile_save_confirm)
        self.profile_save_dialog.show(self)
        
    def on_profile_save_confirm(self, widget, value):
        try:
            illegal_char = '<>:"/\|?* '
            for i in range(len(illegal_char)):
                if illegal_char[i] in value:
                    value.replace(illegal_char[i], '')
            if(value == ''): raise ValueError
        except:
            print traceback.format_exc(1) 
            if(value == ''):
                self.notification_message("", 'Please enter a filename...', "")
                self.profile_save_dialog.show(self)
            return;
            
        value_path = self.user_file_path + '/' + str(value)+'.profile'
        if(os.path.isfile(value_path) == True):
            self.notification_message("", str(value) + '.profile already exists', "")
            self.profile_save_dialog.show(self)
        
        with open(value_path, 'w') as outF:  
            outF.write('setup_start_entry|' + str(self.setup_start_entry.get_text()) + '\n')      
            outF.write('setup_duration_entry|' + str(self.setup_duration_entry.get_text()) + '\n')
            outF.write('setup_period_entry|' + str(self.setup_period_entry.get_text()) + '\n')
            outF.write('setup_filesize_entry|' + str(self.setup_filesize_entry.get_text()) + '\n')
            outF.write('setup_column_checkbox|' + str(self.setup_column_checkbox.get_value()) + '\n')
            outF.write('setup_quote_checkbox|' + str(self.setup_quote_checkbox.get_value()) + '\n')
            outF.write('setup_delimiter_dropdown|' + str(self.setup_delimiter_dropdown.get_value()) + '\n') 
            for i in range(len(self.sensor_objects)):
                outF.write('sensor_objects[' + str(i) + ']|' + str(self.sensor_objects[i].checkbox.get_value()) + '|' + str(self.sensor_objects[i].port.get_value()) + '|' + str(self.sensor_objects[i].sensor.get_value()) + '|' + str(self.sensor_objects[i].function.get_value()) + '\n')

    def on_profile_load_click(self, widget):
        self.profile_load_dialog = gui.GenericDialog(title='Load Profile', message='Select a profile to load:', width='500px')
        try:
            temp = os.listdir(self.user_file_path)
            profiles = []
            for i in range(len(temp)):
                if '.profile' in temp[i]: 
                    profiles.append(temp[i])
        except:
            print traceback.format_exc(1)
            return;
        self.profile_load_list = gui.ListView.new_from_list(profiles, width=500, height=130)
        self.profile_load_dialog.add_field('loadList', self.profile_load_list)
        self.profile_load_dialog.set_on_confirm_dialog_listener(self.profile_load_list_on_confirm)
        self.profile_load_dialog.show(self)
        
    def profile_load_list_on_confirm(self, widget):
        if(self.profile_load_list.get_value() == None):
            self.notification_message("", "No profile selected...", "")
            self.profile_load_dialog.show(self)
        self.set_root_widget(self.vertical_container)
        try:
            file_name = self.user_file_path + '/' + str(self.profile_load_list.get_value())
            value_array = []
            with open(file_name, 'r') as inF:
                for line in inF:
                    temp = line.replace('\n', '')
                    temp = temp.replace('None', '')
                    value_array.append(temp.split('|'))
            
            for i in range(len(value_array)):
                if 'setup_start_entry' in value_array[i]: self.setup_start_entry.set_value(value_array[i][1]) 
                if 'setup_duration_entry' in value_array[i]: self.setup_duration_entry.set_value(value_array[i][1])
                if 'setup_period_entry' in value_array[i]: self.setup_period_entry.set_value(value_array[i][1]) 
                if 'setup_filesize_entry' in value_array[i]: self.setup_filesize_entry.set_value(value_array[i][1])
                if 'setup_column_checkbox' in value_array[i]: self.setup_column_checkbox.set_value(strToBool(value_array[i][1]))
                if 'setup_quote_checkbox' in value_array[i]: self.setup_quote_checkbox.set_value(strToBool(value_array[i][1]))
                if 'setup_delimiter_dropdown' in value_array[i]: self.setup_delimiter_dropdown.set_value(value_array[i][1]) 
                if 'sensor_objects' in value_array[i][0]: 
                    if '[0]' in value_array[i][0]: index = 0 
                    if '[1]' in value_array[i][0]: index = 1 
                    if '[2]' in value_array[i][0]: index = 2 
                    if '[3]' in value_array[i][0]: index = 3 
                    if '[4]' in value_array[i][0]: index = 4 
                    if '[5]' in value_array[i][0]: index = 5 
                    if '[6]' in value_array[i][0]: index = 6 
                    if '[7]' in value_array[i][0]: index = 7     
                    
                    self.sensor_objects[index].checkbox.set_value(strToBool(value_array[i][1]))
                    self.sensor_objects[index].port.set_value(value_array[i][2])
                    self.sensor_objects[index].on_port_change(None, None)
                    self.sensor_objects[index].sensor.set_value(value_array[i][3])
                    self.sensor_objects[index].on_sensor_change(None, None)
                    self.sensor_objects[index].function.set_value(value_array[i][4])
            self.verify_user_inputs(file_name=False)
            
        except:
            print traceback.format_exc(1)
            self.notification_message("", "Error loading "+str(self.profile_load_list.get_value()), "")
            return;
            
    def on_export_click(self, widget):
        self.export_dialog = gui.GenericDialog(title='Export files', message='Select file:', width='500px')
        self.file_download = gui.FileDownloader('', '') 
        try:
            temp = os.listdir(self.user_file_path)
            profiles = []
            for i in range(len(temp)):
                if ('.profile' in temp[i]) or ('.txt' in temp[i]): 
                    profiles.append(temp[i])
        except:
            print traceback.format_exc(1)
            
        self.export_list = gui.ListView.new_from_list(temp, width=500, height=130)
        self.export_list.set_on_selection_listener(self.on_export_list_change)
        self.export_dialog.add_field('expList', self.export_list)        
        self.export_dialog.add_field('yeah', self.file_download)
        self.export_dialog.conf.set_text("Export")
        file_id = str(id(self.file_download))
        self.export_dialog.conf.attributes[self.export_dialog.EVENT_ONCLICK] = "document.getElementById('%s').click(); sendCallback('%s','%s');" % (file_id, self.export_dialog.identifier, self.export_dialog.EVENT_ONCONFIRM)
        self.export_dialog.show(self)
        
    def on_export_list_change(self, widget, value):
        self.file_download._filename = self.user_file_path+'/'+self.export_list.get_value()
    
    def on_delete_click(self, widget):  
        self.delete_dialog = gui.GenericDialog(title='Delete files', message='Select file:', width='500px')
        try:
            temp = os.listdir(self.user_file_path)
            profiles = []
            for i in range(len(temp)):
                if ('.profile' in temp[i]) or ('.txt' in temp[i]): 
                    profiles.append(temp[i])
        except:
            print traceback.format_exc(1)
            
        self.delete_list = gui.ListView.new_from_list(temp, width=500, height=130)
        self.delete_dialog.add_field('delLeist', self.delete_list)        
        self.delete_dialog.set_on_confirm_dialog_listener(self.delete_list_on_confirm)
        self.delete_dialog.show(self)       
        
    def delete_list_on_confirm(self, widget):
        try:
            os.remove(self.user_file_path+'/'+str(self.delete_list.get_value()))
        except:
            print traceback.format_exc(1)
            self.notification_message("", "Error deleting file "+str(self.delete_list.get_value()), "")
        
    def on_setup_start_entry_blur(self, widget):
        try:    
            self.setup_start_entry.style['background-color'] = 'white'
            temp = self.setup_start_entry.get_text().split(':')
            if(len(temp) > 3):
                self.setup_start_entry.style['background-color'] = '#FF9999'
                return;
            if(len(temp) < 3):
                pre = []
                for i in range(3-len(temp)): pre += [0]
                temp = pre + temp
            if(int(temp[0]) > 24): raise ValueError 
            if(int(temp[1]) > 60): raise ValueError 
            if(int(temp[2]) > 60): raise ValueError
            self.setup_start_entry.set_text(str(temp[0]).zfill(2) + ':' + str(temp[1]).zfill(2) + ':' + str(temp[2]).zfill(2))
        except:
            print traceback.format_exc(1)
            self.setup_start_entry.style['background-color'] = '#FF9999'
            return;
            
    def on_setup_duration_entry_blur(self, widget):
        try:
            self.setup_duration_entry.style['background-color'] = 'white'
            temp = self.setup_duration_entry.get_text().split(':')
        
            if(len(temp) > 3):
                self.setup_duration_entry.style['background-color'] = '#FF9999'
                return;
            if(len(temp) < 3):
                pre = []
                for i in range(3-len(temp)): pre += [0]
                temp = pre + temp
            if(int(temp[0]) > 24): raise ValueError 
            if(int(temp[1]) > 60): raise ValueError 
            if(int(temp[2]) > 60): raise ValueError
            self.setup_duration_entry.set_text(str(temp[0]).zfill(2) + ':' + str(temp[1]).zfill(2) + ':' + str(temp[2]).zfill(2))
        except:
            print traceback.format_exc(1)
            self.setup_duration_entry.style['background-color'] = '#FF9999'
            return;
    
    def on_setup_period_entry_blur(self, widget):
        try:
            self.setup_period_entry.style['background-color'] = 'white'
            temp = float(self.setup_period_entry.get_text())
            if(temp < 0.1): self.setup_period_entry.set_text('0.1')
        except:
            print traceback.format_exc(1)
            self.setup_period_entry.style['background-color'] = '#FF9999'
            return;
    
    def on_setup_file_entry_blur(self, widget):
        try:
            self.setup_file_entry.style['background-color'] = 'white'
            illegal_char = '<>:"/\|?* '
            for i in range(len(illegal_char)):
                if illegal_char[i] in self.setup_file_entry.get_text():
                    temp = self.setup_file_entry.get_text()                
                    self.setup_file_entry.set_text(temp.replace(illegal_char[i], ''))
        except:
            print traceback.format_exc(1) 
            self.setup_file_entry.style['background-color'] = '#FF9999'
            return;
            
    def on_setup_filesize_entry_blur(self, widget):
        try:
            self.setup_filesize_entry.style['background-color'] = 'white'
            temp = int(self.setup_filesize_entry.get_text())
        except:
            print traceback.format_exc(1)
            self.setup_filesize_entry.style['background-color'] = '#FF9999'
            return;
    
    def verify_user_inputs(self, start=True, duration=True, period=True, file_size=True, file_name=True, sensors=True):
        # Verify all entered values are correct 
        error_count = 0
        
        #----------------------------------------------------------------------
        # Start_time 
        if(start == True):
            try:    
                self.setup_start_entry.style['background-color'] = 'white'
                temp = self.setup_start_entry.get_text().split(':')
                if(len(temp) > 3):
                    self.setup_start_entry.style['background-color'] = '#FF9999'
                    return;
                if(len(temp) < 3):
                    pre = []
                    for i in range(3-len(temp)): pre += [0]
                    temp = pre + temp
                if(int(temp[0]) > 24): raise ValueError 
                if(int(temp[1]) > 60): raise ValueError 
                if(int(temp[2]) > 60): raise ValueError
                self.setup_start_entry.set_text(str(temp[0]).zfill(2) + ':' + str(temp[1]).zfill(2) + ':' + str(temp[2]).zfill(2))
            except:
                print traceback.format_exc(1)
                self.setup_start_entry.style['background-color'] = '#FF9999'
                error_count += 1

        #----------------------------------------------------------------------
        # Duration 
        if(duration == True):
            try:
                self.setup_duration_entry.style['background-color'] = 'white'
                temp = self.setup_duration_entry.get_text().split(':')
            
                if(len(temp) > 3):
                    self.setup_duration_entry.style['background-color'] = '#FF9999'
                    return;
                if(len(temp) < 3):
                    pre = []
                    for i in range(3-len(temp)): pre += [0]
                    temp = pre + temp
                if(int(temp[0]) > 24): raise ValueError 
                if(int(temp[1]) > 60): raise ValueError 
                if(int(temp[2]) > 60): raise ValueError
                if((int(temp[0])+int(temp[1])+int(temp[2])) == 0): raise ValueError
                
            except:
                print traceback.format_exc(1)
                self.setup_duration_entry.style['background-color'] = '#FF9999'
                error_count += 1
            
        # ---------------------------------------------------------------------
        # Period 
        if(period == True):
            try:
                self.setup_period_entry.style['background-color'] = 'white'
                temp = float(self.setup_period_entry.get_text())
                if(temp < 0.1): self.setup_period_entry.set_text('0.1')
            except:
                print traceback.format_exc(1)
                self.setup_period_entry.style['background-color'] = '#FF9999'
                error_count += 1
        
        # ---------------------------------------------------------------------
        # File size 
        if(file_size == True):
            try:
                self.setup_filesize_entry.style['background-color'] = 'white'
                temp = int(self.setup_filesize_entry.get_text())
            except:
                print traceback.format_exc(1)
                self.setup_filesize_entry.style['background-color'] = '#FF9999'
                error_count += 1
        
        # ---------------------------------------------------------------------
        # File entry
        if(file_name == True):
            try:
                self.setup_file_entry.style['background-color'] = 'white'
                illegal_char = '<>:"/\|?* '
                for i in range(len(illegal_char)):
                    if illegal_char[i] in self.setup_file_entry.get_text():
                        temp = self.setup_file_entry.get_text()                
                        self.setup_file_entry.set_text(temp.replace(illegal_char[i], ''))
                if(self.setup_file_entry.get_text() == ''): raise ValueError
            except:
                print traceback.format_exc(1) 
                self.setup_file_entry.style['background-color'] = '#FF9999'
                error_count += 1
            
        # ---------------------------------------------------------------------
        # Sensor inputs
        if(sensors == True):
            for i in range(len(self.sensor_objects)):
                self.sensor_objects[i].port.style['background-color'] = 'white'
                self.sensor_objects[i].sensor.style['background-color'] = 'white'
                self.sensor_objects[i].function.style['background-color'] = 'white'
            
            for i in range(len(self.sensor_objects)):
                try:
                    if(self.sensor_objects[i].checkbox.get_value() == True):
                        if(self.sensor_objects[i].port.get_value() == 'select'): 
                            self.sensor_objects[i].port.style['background-color'] = '#FF9999'
                            error_count += 1
                except:
                    print traceback.format_exc(1)
                    error_count += 1
        
        if(error_count != 0): return False;
        else: return True;
        
    def parse_sample_window_inputs(self):
        self.sample_countdown_entry.set_text(self.setup_start_entry.get_text())
        self.sample_time_remaining_entry.set_text(self.setup_duration_entry.get_text())
        self.sample_file_name_entry.set_text(self.setup_file_entry.get_text()+'.txt')
        self.set_percent_bar(0)
        
        # ---------------------------------------------------------------------
        # Parse enabled sensors 
        self.enabled_sensors = []
        for i in range(len(self.sensor_objects)):
            if(self.sensor_objects[i].checkbox.get_value() == True):
                self.enabled_sensors.append([self.sensor_objects[i].port.get_value(), self.sensor_objects[i].sensor.get_value(), self.sensor_objects[i].function.get_value()])
                        
        # Setup left side 
        self.sample_bottom_left = gui.Widget(width='49%', height=420, style={'position':'relative', 'top':'3px', 'left':'3px', 'border-color': "#c0c0c0", 'border-width': '2px', 'border-style': 'solid'})
        
        # Setup bottom left heading 
        self.sample_bottom_left.append(gui.Label(" Real-time sensor data", width='100%', height=25, style={'display': 'block', 'overflow': 'auto', 'white-space': 'pre', 'text-align': 'left', 'color': 'white', 'background-color': '#009688', 'font-weight':'bold'}))
        
        # Real-time description heading
        self.realtime_description = gui.Widget(width='100%', height=30, layout_orientation=gui.Widget.LAYOUT_HORIZONTAL, style={'position': 'relative', 'top': '0px', 'left': '0px', 'display': 'block', 'overflow': 'auto', 'background-color': '#AAAAAA'}) 
        self.realtime_description.append(gui.Label("Port", style={'white-space': 'pre', 'position': 'relative', 'left': '18px', 'top':'2px', 'color':'white'}))
        self.realtime_description.append(gui.Label("Sensor", style={'white-space': 'pre', 'position': 'absolute', 'left': '160px', 'top':'2px', 'color':'white'}))
        self.realtime_description.append(gui.Label("Data", style={'white-space': 'pre', 'position': 'absolute', 'left': '340px', 'top':'2px', 'color':'white'}))
        self.sample_bottom_left.append(self.realtime_description)
        
        # Build sensor list 
        self.realtime_objects = []
        for i in range(len(self.enabled_sensors)): 
            self.realtime_objects.append(realTimeDataFactory())
            self.realtime_objects[i].port.set_value(self.enabled_sensors[i][0])
            self.realtime_objects[i].sensor.set_value(str(self.enabled_sensors[i][1])+' ('+str(self.enabled_sensors[i][2])+')')            
            self.sample_bottom_left.append(self.realtime_objects[i].container)
            
        self.sample_bottom_container.append(self.sample_bottom_left, key='realTimeWindow')
        self.sample_bottom_container.append(self.sample_bottom_right, key='fileOutputWindow')
    
    def on_begin_pressed(self, widget):
        if(self.verify_user_inputs() == False): return;
        if(self.parse_sample_window_inputs() == False): return;        
        
        self.sample_start_button.set_enabled(True)
        self.countdown_var = strToSec(self.setup_start_entry.get_value())
        self.duration_var = strToSec(self.setup_duration_entry.get_value())
        self.start_time_var = time.time()
        
        self.sample_update = True
        self.write_file = False
        self.sampleUpdateThread()
        self.set_root_widget(self.sample_container)
       
    def on_sample_cancel_click(self,widget):
        self.sample_update = False
        self.write_file = False
        self.set_root_widget(self.vertical_container)
        
    def on_sample_start_click(self, widget):
        if(self.write_file == False):
            self.start_time_var = self.countdown_var
            self.sample_countdown_entry.set_value(secToStr(0))
            self.sample_start_button.set_enabled(False)
            
    def set_percent_bar(self, percent):
        if(percent > 100): percent = 100
        elif(percent < 0): percent = 0
        self.sample_percent_bar.style['width'] = str(percent)+'%'
        self.sample_percent_value.set_text(str(percent)+'%')
        return;
    
    def sampleUpdateThread(self):        
        # Run while sample_update variable is true, false kills thread 
        if(self.sample_update == True):
            # Start countdown if necessary 
            if(self.write_file == False):
                if(time.time() >= (self.start_time_var + self.countdown_var)): 
                    if(self.setup_delimiter_dropdown.get_value() == 'Tab'): self.file_delimiter = chr(0x09)
                    elif(self.setup_delimiter_dropdown.get_value() == 'Comma'): self.file_delimiter = ','
                    else: self.file_delimiter = ';'
                    
                    if(self.setup_column_checkbox.get_value() == True):
                        outString = '' 
                        if(self.setup_quote_checkbox.get_value() == True):
                            with open(self.user_file_path+'/'+self.sample_file_name_entry.get_value(), 'wb') as outF:
                                outF.write('"time"')
                                for i in range(len(self.enabled_sensors)): 
                                    outF.write(self.file_delimiter+'"'+str(self.enabled_sensors[i][1])+' ('+str(self.enabled_sensors[i][2])+')"')
                                outF.write('\r\n')
                        else:                            
                            with open(self.user_file_path+'/'+self.sample_file_name_entry.get_value(), 'wb') as outF:
                                outF.write('time')
                                for i in range(len(self.enabled_sensors)): 
                                    outF.write(self.file_delimiter+str(self.enabled_sensors[i][1])+' ('+str(self.enabled_sensors[i][2])+')')
                                outF.write('\r\n')
                        with open(self.user_file_path+'/'+self.sample_file_name_entry.get_value(), 'rb') as inF: self.sample_file_output.set_text(inF.read())
                    else:
                        with open(self.user_file_path+'/'+self.sample_file_name_entry.get_value(), 'wb') as outF: outF.write('')
                    
                    # Make a time=0 entry in the file 
                    data = [] 
                    data.append('0.0')
                    for i in range(len(self.enabled_sensors)):
                        func_string = self.enabled_sensors[i][2]
                        if 'D' in self.enabled_sensors[i][0]:
                           port = int(str(self.enabled_sensors[i][0]).replace('D', ''))
                           data.append(str(s.functions[func_string](port)))
                        elif 'A' in self.enabled_sensors[i][0]:
                            port = int(str(self.enabled_sensors[i][0]).replace('A', ''))
                            data.append(str(s.functions[func_string](port)))
                        else:
                            data.append(str(s.functions[func_string]()))

                    with open(self.user_file_path+'/'+self.sample_file_name_entry.get_value(), 'ab') as outF:
                        for i in range(len(data)): 
                            if(i==0):outF.write(str(data[i]))
                            else:outF.write(self.file_delimiter+str(data[i]))
                        outF.write('\r\n')
                    
                    self.write_file = True
                    self.time_var = 0.0
                    self.file_size_var = 0 
                    self.writeSampleThread()
                    self.start_time_var = time.time()
                    self.sample_start_button.set_enabled(False)
                else:
                    self.sample_countdown_entry.set_value(secToStr((self.start_time_var+self.countdown_var)-time.time()))
            
            # If countdown is complete, begin countdown of duration
            else:
                if(time.time() >= self.start_time_var + self.duration_var): 
                    self.write_file = False
                    self.sample_update = False 
                    self.set_percent_bar(100)
                    time.sleep(0.5)
                    self.notification_message("", "Logging file complete! Press OK to continue...", "")
                    self.set_root_widget(self.vertical_container)
                # Parse the duration value, percent completion, and file size 
                else:
                    self.sample_time_remaining_entry.set_value(secToStr((self.start_time_var+self.duration_var)-time.time()))
                    self.set_percent_bar(int(float(((time.time()-self.start_time_var)/self.duration_var)*100)))
                    self.sample_file_name_size.set_text(str(self.file_size_var)+' B')
                    try: self.sample_file_output.set_text(subprocess.check_output(['tail', '-24', self.user_file_path+'/'+self.sample_file_name_entry.get_value()]))
                    except: pass 
                    
                    if(self.file_size_var >= int(self.setup_filesize_entry.get_value())):
                        self.write_file = False
                        self.sample_update = False 
                        self.set_percent_bar(100)
                        time.sleep(0.5)
                        self.notification_message("", "Logging file exceeded maximum size! Press OK to continue...", "")
                        self.set_root_widget(self.vertical_container)
            
            # Parse the read time data readings 
            for i in range(len(self.realtime_objects)):
                try:
                    func_string = self.enabled_sensors[i][2]
                    if 'D' in self.enabled_sensors[i][0]:
                        port = int(str(self.enabled_sensors[i][0]).replace('D', ''))
                        self.realtime_objects[i].data.set_value(str(s.functions[func_string](port)))
                    elif 'A' in self.enabled_sensors[i][0]:
                        port = int(str(self.enabled_sensors[i][0]).replace('A', ''))
                        self.realtime_objects[i].data.set_value(str(s.functions[func_string](port)))
                    else:
                        self.realtime_objects[i].data.set_value(str(s.functions[func_string]()))
                except:
                    print traceback.format_exc(1)
            Timer(0.01, self.sampleUpdateThread).start()
    
    def writeSampleThread(self):
        # Run while write_file is true, false kills thread 
        if(self.write_file == True):
            temp = time.time()
            if(temp >= self.next_sample):
                self.next_sample = temp + float(self.setup_period_entry.get_value())
                self.time_var += float(self.setup_period_entry.get_value())
                data = [] 
                data.append(str(self.time_var))
                for i in range(len(self.enabled_sensors)):
                    func_string = self.enabled_sensors[i][2]
                    if 'D' in self.enabled_sensors[i][0]:
                       port = int(str(self.enabled_sensors[i][0]).replace('D', ''))
                       data.append(str(s.functions[func_string](port)))
                    elif 'A' in self.enabled_sensors[i][0]:
                        port = int(str(self.enabled_sensors[i][0]).replace('A', ''))
                        data.append(str(s.functions[func_string](port)))
                    else:
                        data.append(str(s.functions[func_string]()))

                with open(self.user_file_path+'/'+self.sample_file_name_entry.get_value(), 'ab') as outF:
                    for i in range(len(data)): 
                        if(i==0):outF.write(str(data[i]))
                        else:outF.write(self.file_delimiter+str(data[i]))
                    outF.write('\r\n')
                
                # with open(self.user_file_path+'/'+self.sample_file_name_entry.get_value(), 'rb') as inF: self.sample_file_output.set_text(inF.read())    
                
                                
                self.file_size_var = os.stat(self.user_file_path+'/'+self.sample_file_name_entry.get_value()).st_size
            Thread(None, self.writeSampleThread).start() 