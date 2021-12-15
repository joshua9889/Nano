"""
ht_Angle.py - HiTechnic Angle sensor library for core legacy module
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

import time

class ht_Angle:
    def __init__(self, main_obj, port_loc):
        self.obj = main_obj
        self.port = port_loc
        self.addr = 0x02
        
    def __del__(self): pass 
    
    def resetAbsolute(self):
        self.obj.i2cWrite(self.port, self.addr, 0x41, [0x52])
        while (self.obj.i2cRead(self.port, self.addr, 0x41, 1)[0] != 0x00): pass 
        return;
        
    def calibrate(self):
        self.obj.i2cWrite(self.port, self.addr, 0x41, [0x43])
        time.sleep(0.025)
        while (self.obj.i2cRead(self.port, self.addr, 0x41, 1)[0] != 0x00): pass 
        return;
    
    def getAngle(self):
        data = self.obj.i2cRead(self.port, self.addr, 0x42, 2)
        value = (data[0] << 1) | data[1]
        return value;
        
    def getAbsolute(self):
        data = self.obj.i2cRead(self.port, self.addr, 0x44, 4)
        value = (data[0] << 24) | (data[1] << 16) | (data[2] << 8) | data[3]
        if(value > 0x80000000): value -= 0x100000000
        return value;
    
    def getRPM(self):
        data = self.obj.i2cRead(self.port, self.addr, 0x48, 2)
        value = (data[0] << 8) | data[1]
        if (value > 0x8000): value -= 0x10000
        return value;