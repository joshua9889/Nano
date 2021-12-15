"""
pidLoop.py - PID Loop class for the Fusion system
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

from threading import Thread
import time  

class pidLoop:
    def __init__(self):
        self.PID = None
        self.interval = None
        self.set_point = None 
        self.input = None
        self.output = None 
        
        self.errSum = 0.0
        self.lastError = 0.0
        self.output = 0.0 
        self.last_time = 0.0
        
        self.thread_instance = None 
                
    def __del__(self):
        pass 
                
    def startLoop(self):
        try:
            if(self.thread_instance.isAlive() == True): return; 
        except: 
            pass 
        
        if((self.PID == None) or (self.interval == None) or (self.set_point == None) or (self.input == None) or (self.output == None)):
            raise ValueError
        
        self.thread_instance = Thread(target=self.pidFunction)
        self.thread_instance.daemon = True
        self.thread_instance.start()   
        print self.thread_instance.isAlive()
        return;
            
    def pauseLoop(self):pass
        
    def stopLoop(self):pass
        
    def pidFunction(self):
        self.last_time = time.time()
        while True:            
            time.sleep(self.interval)
            now = time.time()
            time_change = now - self.last_time
            
            error = self.set_point - self.input
            self.errSum += (error * time_change)
            dErr = (error - self.lastError) / time_change;
            
            self.output = (self.PID[0]*error) + (self.PID[1]*self.errSum) + (self.PID[2]*dErr)
            self.lastError = error 
            self.last_time = now