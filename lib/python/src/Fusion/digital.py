"""
digital.py - Digital wrapper class for the Fusion system
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

class digital:

    def __init__(self, main_obj, port_loc):
        self.obj = main_obj
        self.port = port_loc
        
    def read (self):
        self.obj.digitalState(self.port, self.obj.INPUT)
        return self.obj.digitalRead(self.port)
        
    def write (self, value):
        self.obj.digitalState(self.port, self.obj.OUTPUT)
        self.obj.digitalWrite(self.port, value)
        return;