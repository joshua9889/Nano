"""
compass.py - Compass sensor class for the Fusion system
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

class compass:
    obj = None 
    addr = None 
        
    def __init__(self, main_obj, i2c_addr=0x24):
        self.obj = main_obj
        self.addr = i2c_addr
                
    #def __del__(self):

    def hardIronCalibration(self):
        self.obj.i2cWrite(self.addr, 0x03, [0x43])
        time.sleep(5)
        self.obj.i2cWrite(self.addr, 0x03, [0x00])
        time.sleep(0.1)
        return self.obj.i2cRead(self.addr, 0x03, 1)[0]
        
    def getHeading(self):
        self.obj.i2cWrite(self.addr, 0x22, [0x00, 0x01, 0x00, 0x01])
        data = self.obj.i2cRead(self.addr, 0x04, 2)
        return ((data[1] << 8) | data[0]);
    
    def nullAccelerometer(self, axis):        
        if (axis == 'X'): self.obj.i2cWrite(self.addr, 0x03, [0x58])
        elif(axis == 'Y'): self.obj.i2cWrite(self.addr, 0x03, [0x59])
        elif(axis == 'Z'): self.obj.i2cWrite(self.addr, 0x03, [0x5A])
        while (self.obj.i2cRead(self.addr, 0x03, 1)[0] != 0x00): pass
        return;
    
    def getAccelerometer(self):
        data = self.obj.i2cRead(self.addr, 0x06, 6)
        x = (data[1] << 8) | data[0]
        if(x >= 0x8000): x -= 65536        
        y = (data[3] << 8) | data[2]
        if(y >= 0x8000): y -= 65536        
        z = (data[5] << 8) | data[4]
        if(z >= 0x8000): z -= 65536        
        return [x, y, z];
        
    def tiltUp(self):
        self.obj.i2cWrite(self.addr, 0x03, [0x55])
        while(self.obj.i2cRead(self.addr, 0x03, 1)[0] == 0x55): pass 
        return;
        
    def tiltDown(self):
        self.obj.i2cWrite(self.addr, 0x03, [0x44])
        while(self.obj.i2cRead(self.addr, 0x03, 1)[0] == 0x44): pass 
        return;
    
    def getMagnetometer(self):
        data = self.obj.i2cRead(self.addr, 0x0C, 6)
        x = (data[1] << 8) | data[0]
        if(x >= 0x8000): x -= 65536        
        y = (data[3] << 8) | data[2]
        if(y >= 0x8000): y -= 65536        
        z = (data[5] << 8) | data[4]
        if(z >= 0x8000): z -= 65536          
        return [x, y, z];
        
    def scaleAccelerometer(self):
        temp = self.obj.i2cRead(self.addr, 0x06, 2)
        x = (temp[1] << 8) | temp[0]
        try: scale = (1000/x)*256 
        except: return False;          
        lsb = (scale & 0xFF00) >> 8 
        fsb = scale & 0x00FF 
        self.obj.i2cWrite(self.addr, 0x20, [fsb, lsb])
        time.sleep(0.01)
        self.obj.i2cWrite(self.addr, 0x03, [0x57])
        while(self.obj.i2cRead(self.addr, 0x03, 1)[0] == 0x57): pass
        return True;
