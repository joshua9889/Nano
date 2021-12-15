"""
coreServoController.py - Core servo controller class for the Fusion system
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

import serial

class coreServoController:
    S1      = 0x01
    S2      = 0x02 
    S3      = 0x03 
    S4      = 0x04 
    S5      = 0x05 
    S6      = 0x06
    
    def __init__(self, driver, dev_id):
        self.driver = driver 
        self.dev_id = dev_id 
        dev_index = self.driver.serial_numbers.index(self.dev_id)
        self.PORT = serial.Serial("/dev/" + self.driver.port_list[dev_index], baudrate=250000)
        self.PORT.close()
        self.PORT.open()
        
    def __del__(self):
        self.driver.FTDI_WRITE(0x00, [0x00]*0x49, self.PORT)    
        self.driver.FTDI_WRITE(0x48, [0xFF], self.PORT)
        self.PORT.close()   
        
    # ---------------------------------------------------------------------------
    def servoTarget(self, servo, position):
        if (servo < 1): servo = 1 
        elif (servo > 6): servo = 6 
        temp_buf = [position]
        self.driver.FTDI_WRITE(0x41+servo, temp_buf, self.PORT)
        return;
        
    # ---------------------------------------------------------------------------
    def pwmEnable(self, enable=False):
        if(enable == False): temp = 0xFF 
        else: temp = 0x00
        self.driver.FTDI_WRITE(0x48, [temp], self.PORT)
        return;

    # ---------------------------------------------------------------------------   
    def extendedModeEnable(self, servo, mode=None):
        if (servo < 1): servo = 1 
        elif (servo > 6): servo = 6 
        
        if ((mode != 0x00) and (mode != 0x01)): return;

        temp = self.driver.FTDI_READ(0x49+servo, [0x00], self.PORT)[0]
        if (temp != mode): 
            self.driver.FTDI_WRITE(0x49 + servo, [mode], self.PORT)          
        return;