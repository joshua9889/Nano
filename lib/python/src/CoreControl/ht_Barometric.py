"""
ht_Barometric.py - HiTechnic Barometric sensor library for core legacy module
Author: Justin Mathews
Copyright (c) 2018 Modern Robotics Inc.

Fusion Web Page: http://www.modernroboticsinc.com/fusion-controller

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

class ht_Barometric:
    def __init__(self, main_obj, port_loc):
        self.obj = main_obj
        self.port = port_loc
        self.addr = 0x02
        
    def __del__(self): pass 
    
    def setUserCalibration(self):
        self.obj.i2cWrite(self.port, self.addr, 0x40, [0x55, 0xAA])
        return; 
        
    def setFactoryCalibration(self):
        self.obj.i2cWrite(self.port, self.addr, 0x40, [0x3C, 0xC3])
        return;
        
    def restoreFactoryCalibration(self):
        self.obj.i2cWrite(self.port, self.addr, 0x40, [0xAA, 0x55])
        return;
    
    def getTemp(self):
        data = self.obj.i2cRead(self.port, self.addr, 0x42, 2)
        value = (data[0] << 8) | data[1]
        value /= 10;
        return value;
        
    def getTempRaw(self):
        data = self.obj.i2cRead(self.port, self.addr, 0x42, 2)
        value = (data[0] << 8) | data[1]
        return value;
        
    def getPressure(self):
        data = self.obj.i2cRead(self.port, self.addr, 0x44, 2)
        value = (data[0] << 8) | data[1]
        value /= 1000.0;
        return value;
        
    def getPressureRaw(self):
        data = self.obj.i2cRead(self.port, self.addr, 0x44, 2)
        value = (data[0] << 8) | data[1]
        return value;
        
    def setPressureCalibration(self, value):
        temp = [(value >> 8) & 0xFF, value & 0xFF]
        self.obj.i2cWrite(self.port, self.addr, 0x46, temp)
        return;