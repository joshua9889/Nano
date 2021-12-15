"""
lcs.py - I2C enabled LCD class for the Fusion system
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

class lcd:
    obj = None 
    addr = None 
    
    CLOCK_SPEED     = 62500
    DEFAULT_SPEED   = 100000
    
    def __init__(self, main_obj, i2c_addr=0x50):
        self.obj = main_obj
        self.addr = i2c_addr
        
    def __del__(self):
        self.clearScreen()
    
    def printLCD(self, buffer):
            self.bus.i2cWrite(self.addr, 0x00, buffer)
            return;

    def displayEN(self, state):
        if (state == True): self.bus.i2cWrite(self.addr, 0xFE, [0x41])
        else: self.bus.i2cWrite(self.addr, 0xFE, [0x42])
        return;
        
    def setCursor(self, x, y):
        if(x == 0): cursor_buffer = 0x00 + y
        elif(x == 1): cursor_buffer = 0x40 + y
        elif(x == 2): cursor_buffer = 0x14 + y
        elif(x == 3): cursor_buffer = 0x54 + y
        else: return;        
        self.obj.i2cWrite(self.addr, 0xFE, [0x45, cursor_buffer])
        return;
    
    def cursorHome(self):
        self.obj.i2cWrite(self.addr, 0xFE, [0x46])
        return;
    
    def underlineCursor(self, state):
        if(state == True): self.obj.i2cWrite(self.addr, 0xFE, [0x47])
        else: self.obj.i2cWrite(self.addr, 0xFE, [0x48])
        return;
    
    def cursorLeft(self, count):
        for i in range(count): self.obj.i2cWrite(self.addr, 0xFE, [0x49])
        return;
    
    def cursorRight(self, count):
        for i in range(count): self.obj.i2cWrite(self.addr, 0xFE, [0x4A])
        return;
    
    def blinkingCursor(self, state):
        if(state == True): self.obj.i2cWrite(self.addr, 0xFE, [0x4B])
        else: self.obj.i2cWrite(self.addr, 0xFE, [0x4C])
        return;
    
    def backspace(self, count):
        for i in range(count): self.obj.i2cWrite(self.addr, 0xFE, [0x4E])
        return;
    
    def clearScreen(self):
        self.obj.i2cWrite(self.addr, 0xFE, [0x51])
        time.sleep(0.003)
        self.obj.i2cWrite(self.addr, 0xFE, [0x46])
        time.sleep(0.002)
        return;
    
    def setContrast(self, value):
        self.obj.i2cWrite(self.addr, 0xFE, [0x52, value])
        return;
    
    def setBacklight(self, value):
        self.obj.i2cWrite(self.addr, 0xFE, [0x53, value])
        return;
    
    def displayLeft(self, count):
        for i in range(count): self.obj.i2cWrite(self.addr, 0xFE, [0x55])
        return;
    
    def displayRight(self, count):
        for i in range(count): self.obj.i2cWrite(self.addr, 0xFE, [0x56])
        return;
    
    def setAddress(self, addr):
        self.obj.i2cWrite(self.addr, 0xFE, [0x62, addr])
        time.sleep(0.004)
        return;