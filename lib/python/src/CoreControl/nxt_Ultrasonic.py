"""
nxt_Ultrasonic.py - NXT Ultrasonic sensor library for core legacy module
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

class nxt_Ultrasonic:
    def __init__(self, main_obj, port_loc):
        self.obj = main_obj
        self.port = port_loc
        
        self.obj.enable_9v(self.port, True)
        self.addr = 0x02
        
    def __del__(self): pass 
    
    def read(self):
        return self.obj.i2cRead(self.port, self.addr, 0x42, 1)[0]