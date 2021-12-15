"""
ht_IRseekerV2.py - HiTechnic IR Seeker V2 sensor library for core legacy module
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

class ht_IRseekerV2:
    def __init__(self, main_obj, port_loc):
        self.obj = main_obj
        self.port = port_loc
        self.addr = 0x10
        
    def __del__(self): pass 
    
    def getDirection_DC(self):
        return self.obj.i2cRead(self.port, self.addr, 0x42, 1)[0];
    
    def getSignalStrength_DC(self):
        return self.obj.i2cRead(self.port, self.addr, 0x43, 5);
    
    def getMean_DC(self):
        return self.obj.i2cRead(self.port, self.addr, 0x48, 1)[0];
    
    def getDirection_AC(self):
        return self.obj.i2cRead(self.port, self.addr, 0x49, 1)[0];
    
    def getSignalStregnth_AC(self):
        return self.obj.i2cRead(self.port, self.addr, 0x4A, 5);