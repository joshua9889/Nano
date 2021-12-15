"""
ht_Compass.py - HiTechnic Compass sensor library for core legacy module
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
import time 

class ht_Compass:
    def __init__(self, main_obj, port_loc):
        self.obj = main_obj
        self.port = port_loc
        self.addr = 0x02
        
    def __del__(self): pass 
    
    def hardIronCalibration(self, state):
        if(state == True): 
            self.obj.i2cWrite(self.port, self.addr, 0x41, [0x43])
            time.sleep(0.1)
            return self.obj.i2cRead(self.port, self.addr, 0x41, 1)[0]
        else:
            self.obj.i2cWrite(self.port, self.addr, 0x41, [0x00])
            time.sleep(0.1)
            return self.obj.i2cRead(self.port, self.addr, 0x41, 1)[0]
    
    def getHeading(self):
        data = self.obj.i2cRead(self.port, self.addr, 0x42, 2)
        value = (data[0] << 1) | data[1]
        return value;