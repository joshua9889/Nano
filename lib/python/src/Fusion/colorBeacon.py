"""
colorBeacon.py - ColorBeacon class for the Fusion system
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

class colorBeacon:
    obj = None 
    addr = None 
    
    OFF     = 0x00
    RED     = 0x01
    GREEN   = 0x02
    YELLOW  = 0x03
    BLUE    = 0x04
    PURPLE  = 0x05
    TEAL    = 0x06
    WHITE   = 0x07
   
    
    def __init__(self, main_obj, i2c_addr=0x4C):
        self.obj = main_obj
        self.addr = i2c_addr
        
    def __del__(self):
        self.obj.i2cWrite(self.addr, 0x04,[0x00]*6)
        
    def setColor(self, color):
        self.obj.i2cWrite(self.addr, 0x04,[color, 0x00, 0x00, 0x00])
        return;
         
    def setCustomColor(self, red, green, blue):
        self.obj.i2cWrite(self.addr, 0x04, [0x08, red, green, blue])
        return;