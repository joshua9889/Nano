"""
lineScan.py - LineScan sensor class for the Fusion system
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

class lineScan:
    obj = None 
    addr = None 
    
    BLACK_LINE = 0x00
    WHITE_LINE = 0x80
    ENABLE_AUTO = 0x00
    DISABLE_AUTO = 0x01
    
    def __init__(self, main_obj, i2c_addr=0x40):
        self.obj = main_obj
        self.addr = i2c_addr
        
    #def __del__(self):

    def setMode(self, value):
        self.obj.i2cWrite(self.addr, 0x03, [value])
        return;
        
    def secondLeftReading(self):
        value = self.obj.i2cRead(self.addr, 0x04, 1)
        value += self.obj.i2cRead(self.addr, 0x09, 1)
        return value;
        
    def firstLeftReading(self):
        value = self.obj.i2cRead(self.addr, 0x05, 1)
        value += self.obj.i2cRead(self.addr, 0x0A, 1)
        return value;
    
    def centerReading(self):
        value = self.obj.i2cRead(self.addr, 0x06, 1)
        value += self.obj.i2cRead(self.addr, 0x0B, 1)
        return value;
        
    def firstRightReading(self):
        value = self.obj.i2cRead(self.addr, 0x07, 1)
        value += self.obj.i2cRead(self.addr, 0x0C, 1)
        return value;
        
    def secondRightReading(self):
        value = self.obj.i2cRead(self.addr, 0x08, 1)
        value += self.obj.i2cRead(self.addr, 0x0D, 1)
        return value;
        
    def currentMaxBrightness(self):
        return self.obj.i2cRead(self.addr, 0x0E, 1)[0]
        
    def currentFrameTimer(self):
        return self.obj.i2cRead(self.addr, 0x0F, 1)[0]
    
    def rawPixels(self):
        value = self.obj.i2cRead(self.addr, 0x80, 0x10)
        value += self.obj.i2cRead(self.addr, 0x90, 0x10)
        value += self.obj.i2cRead(self.addr, 0xA0, 0x10)
        value += self.obj.i2cRead(self.addr, 0xB0, 0x10)
        value += self.obj.i2cRead(self.addr, 0xC0, 0x10)
        value += self.obj.i2cRead(self.addr, 0xD0, 0x10)
        value += self.obj.i2cRead(self.addr, 0xE0, 0x10)
        value += self.obj.i2cRead(self.addr, 0xF0, 0x10)
        return value
