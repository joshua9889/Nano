"""
ht_Accelerometer.py - HiTechnic Accelerometer sensor library for core legacy module
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

class ht_Accelerometer:
    def __init__(self, main_obj, port_loc):
        self.obj = main_obj
        self.port = port_loc
        self.addr = 0x02
        
    def __del__(self): pass 
    
    def getAccelerometer(self):
        data = self.obj.i2cRead(self.port, self.addr, 0x42, 6)
        x_value = (data[0] << 2) | data[3]
        if (x_value > 0x0200): x_value -= 0x0400
        y_value = (data[1] << 2) | data[4]
        if (y_value > 0x0200): y_value -= 0x0400
        z_value = (data[2] << 2) | data[5]
        if (z_value > 0x0200): z_value -= 0x0400
        return [x_value, y_value, z_value];
    
    def nullAccelerometer(self):
        self.obj.i2cWrite(self.port, self.addr, 0x41, [ord('X')])
        while (self.obj.i2cRead(self.port, self.addr, 0x41, 1)[0] != 0x00): pass 
        
        self.obj.i2cWrite(self.port, self.addr, 0x41, [ord('Y')])
        while (self.obj.i2cRead(self.port, self.addr, 0x41, 1)[0] != 0x00): pass 
        
        self.obj.i2cWrite(self.port, self.addr, 0x41, [ord('Z')])
        while (self.obj.i2cRead(self.port, self.addr, 0x41, 1)[0] != 0x00): pass 
        
        return;