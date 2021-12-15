"""
locator360.py - IR Locator 360 sensor class for the Fusion system
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

class locator360:
    obj = None 
    addr = None 
    
    def __init__(self, main_obj, i2c_addr=0x1C):
        self.obj = main_obj
        self.addr = i2c_addr
        
    #def __del__(self):
    
    def getHeading(self, freq):
        if(freq == 1200): return self.obj.i2cRead(self.addr, 0x04, 1)[0];
        elif(freq == 600): return self.obj.i2cRead(self.addr, 0x06, 1)[0];
        else: return -1;
    
    def getIntensity(self, freq):
        if(freq == 1200): return self.obj.i2cRead(self.addr, 0x05, 1)[0];
        elif(freq == 600): return self.obj.i2cRead(self.addr, 0x07, 1)[0];
        else: return -1;