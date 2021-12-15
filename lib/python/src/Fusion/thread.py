"""
thread.py - Threading wrapper class for the Fusion system
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

#==============================================================================================================
# This article mentions that CPython's memory management is not thread-safe
#   https://blog.floydhub.com/multiprocessing-vs-threading-in-python-what-every-data-scientist-needs-to-know/
#==============================================================================================================



from threading import Timer, Thread
import time 

class thread:
    def __init__(self, func):
        self._function = func 
        self._thread_instance = None
        self._thread_running = False
        
    def __del__(self): pass
        
    def start(self, loop_time=None):  
        try: 
            if(self._thread_instance.isAlive() == True): return;
        except: pass 
        
        if(self._thread_running == True): return; 
        self._thread_running = True 
        if(loop_time == None):
            self._thread_instance = Thread(None, self._SingleThreadProcess)
            self._thread_instance.daemon = True
            self._thread_instance.start()
        elif(loop_time == 0.0):
            self._thread_instance = Thread(None, self._InfiniteThreadProcess)
            self._thread_instance.daemon = True
            self._thread_instance.start()
        elif(loop_time > 0.0):
            self._timervalue = loop_time
            self._thread_instance = Thread(None, self._TimedThreadProcess)
            self._thread_instance.daemon = True
            self._thread_instance.start()
        else: pass   
    
    def _SingleThreadProcess(self):
        self._function()
        self._thread_running = False; 
    
    def _InfiniteThreadProcess(self):
        self._function()
        if(self._thread_running == True):
            self._thread_instance = Thread(None, self._InfiniteThreadProcess)
            self._thread_instance.daemon = True
            self._thread_instance.start()
        else:
            self._thread_running = False 
            return;
            
    def _TimedThreadProcess(self):
        self._function()
        if(self._thread_running == True):
            self._thread_instance = Timer(self._timervalue, self._TimedThreadProcess)
            self._thread_instance.daemon = True
            self._thread_instance.start()
        else:
            self._thread_running = False 
            return;
    
    def isAlive(self):
        try:
            return self._thread_instance.isAlive();
        except:
            return False;
            
    def stop(self):
        self._thread_running = False
        return;