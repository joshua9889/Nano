"""
usbGamepad.py - USB Gamepad class for the Fusion system
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

import pygame
import traceback

class usbGamepad:
    obj = None 
    name = None
    num_axes = None 
    num_buttons = None 
    num_hats = None 
    events = None 
    
    def __init__(self, pad_num=0):
        try:            
            pygame.init()
            pygame.joystick.init()
            self.obj = pygame.joystick.Joystick(pad_num)
            self.obj.init()
            self.name = self.obj.get_name()
            self.num_axes = self.obj.get_numaxes()
            self.num_buttons = self.obj.get_numbuttons()
            self.num_hats = self.obj.get_numhats()                        
        except:
            print traceback.format_exc(1)
        
    def __del__(self):
        self.obj.quit() 
        pygame.quit()
        
    def readAxis(self, axis, inv=False):
        pygame.event.clear()         
        if((0 <= axis) and (axis <= self.num_axes-1)):
            if(inv == False): return int(self.obj.get_axis(axis)*100)
            else: return (int(self.obj.get_axis(axis)*-100))
        else:
            print "Axis selection out of range 0 to " + str(self.num_axes-1)
            raise ValueError;
    
    def readAxisFloat(self, axis, inv=False):
        pygame.event.clear()         
        if((0 <= axis) and (axis <= self.num_axes-1)):
            if(inv == False): return self.obj.get_axis(axis)
            else: return self.obj.get_axis(axis)*-1.0
        else:
            print "Axis selection out of range 0 to " + str(self.num_axes-1)
            raise ValueError;
            
    def mixer(self, x_axis, y_axis, x_inv=False, y_inv=False):
        x = self.readAxis(x_axis)
        if(x_inv == True): x *= -1
        
        y = self.readAxis(y_axis)
        if(y_inv == True): y *= -1
        
        left_motor = y - x
        right_motor = y + x 
                
        if(left_motor >= 100): left_motor = 100
        elif (left_motor <= -100): left_motor = -100
        
        if(right_motor >= 100): right_motor = 100 
        elif(right_motor <= -100): right_motor = -100
        
        return (left_motor, right_motor);
    
    def readButton(self, button):
        pygame.event.clear() 
        if((0 <= button) and (button <= self.num_buttons-1)):
            return self.obj.get_button(button) 
        else:
            print "Button selection out of range 0 to " + str(self.num_buttons-1)
            raise ValueError;
            
    def readHat(self, hat=0):
        pygame.event.clear()
        if((0 <= hat) and (hat <= self.num_hats-1)):
            return self.obj.get_hat(hat);
        else:
            print "Hat selection out of range 0 to " + str(self.num_hats-1)
            raise ValueError;