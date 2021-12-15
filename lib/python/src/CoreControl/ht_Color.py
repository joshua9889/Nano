"""
ht_Color.py - HiTechnic Color sensor library for core legacy module
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

class ht_Color:
    def __init__(self, main_obj, port_loc):
        self.obj = main_obj
        self.port = port_loc
        self.addr = 0x02
        
    def __del__(self): pass 
    
    def whiteBalance(self):
        self.obj.i2cWrite(self.port, self.addr, 0x41, [0x43])
        while (self.obj.i2cRead(self.port, self.addr, 0x41, 1)[0] != 0): pass 
        return; 
        
    def blackBalance(self):
        self.obj.i2cWrite(self.port, self.addr, 0x41, [0x42])
        while (self.obj.i2cRead(self.port, self.addr, 0x41, 1)[0] != 0): pass 
        return; 
           
    def getColorNumber(self):
        return self.obj.i2cRead(self.port, self.addr, 0x42, 1)[0];
    
    def getColorReading(self):
        data = self.obj.i2cRead(self.port, self.addr, 0x46, 6);
        red = (data[1] << 8) | data [0]
        green = (data[3] << 8) | data[2]
        blue = (data[5] << 8) | data[4]
        return [red, green, blue];
        
    def getColorIndex(self):
        return self.obj.i2cRead(self.port, self.addr, 0x4C, 1)[0];
        
    def getColorNormalized(self):
        data = self.obj.i2cRead(self.port, self.addr, 0x4D, 6);
        return [data[0], data[1], data[2]];
    