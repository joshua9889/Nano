"""
sound.py - Sound Generator class for the Fusion system
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

class sound:
    obj = None 
    addr = None 
    
    LOW     = 0x00 
    MED     = 0x01 
    HIGH    = 0x02 
    MAX     = 0x03 
    
    index = 0
    number = [0x00, 0x01]
    letter = [0x00, 0x01]
    
    def __init__(self, main_obj, i2c_addr=0x34):
        self.obj = main_obj
        self.addr = i2c_addr
        
    #def __del__(self):
    
    def setSound(self, level, freq, length):
        if((level < 0) or (level > 3) or (freq < 1) or (freq > 5000) or (length < 1) or (length > 2550)): return;
        lsb = freq & 0x00FF 
        msb = (freq & 0xFF00) >> 8
        self.obj.i2cWrite(self.addr, 0x04, [level, lsb, msb, int(length/10)])
        return;
    
    def setSoundBlocking(self, level, freq, length, post_pause=0):
        if((level < 0) or (level > 3) or (freq < 1) or (freq > 5000) or (length < 1)): return;
        lsb = freq & 0x00FF 
        msb = (freq & 0xFF00) >> 8
        while (length):            
            while (self.getDuration() > 20): pass 
            if (length >= 2550):
                length -= 2550 
                temp = 255
            else:
                temp = length/10 
                length = 0
            self.obj.i2cWrite(self.addr, 0x04, [level, lsb, msb, temp])
        while (self.getDuration() != 0): pass
        time.sleep(post_pause/1000.0)
        return;
        
    def setVolume(self, level):
        if((level < 0) or (level > 3)): return;
        self.obj.i2cWrite(self.addr, 0x04, [level])
        return;
    
    def setPitch(self, freq):
        if((freq < 1) or (freq > 5000)): return;
        lsb = freq & 0x00FF 
        msb = (freq & 0xFF00) >> 8
        self.obj.i2cWrite(self.addr, 0x05, [lsb, msb])
        return;
    
    def setDuration(self, length):
        if((length < 1) or (length > 2550)): return;
        self.obj.i2cWrite(self.addr, 0x07, [int(length/10)])
        return;
        
    def getDuration(self):
        return self.obj.i2cRead(self.addr, 0x07, 1)[0];