"""
nxt_Light.py - NXT Light sensor library for core legacy module
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

class nxt_Light:
    def __init__(self, main_obj, port_loc):
        self.obj = main_obj
        self.port = port_loc
        
    def __del__(self): pass 
    
    def read(self):
        return self.obj.analogRead(self.port);
        
    def ledEnable(self, value=False):
        if(value == True):
            self.obj.digitalEnable(self.port, 0, 1)
        else:
            self.obj.digitalEnable(self.port, 0, 0)
