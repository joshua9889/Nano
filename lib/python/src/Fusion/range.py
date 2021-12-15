"""
range.py - Range sensor class for the Fusion system
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

class range:
    obj = None 
    addr = None 
    
    def __init__(self, main_obj, i2c_addr=0x28):
        self.obj = main_obj
        self.addr = i2c_addr
        
    #def __del__(self):
        
    def ultrasonic(self):
        return self.obj.i2cRead(self.addr, 0x04, 1)[0]
        
    def optical(self):
        return self.obj.i2cRead(self.addr, 0x05, 1)[0]