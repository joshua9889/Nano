"""
usbCamera.py - Object Tracking class for the Fusion system
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

import numpy as np
import cv2 
import traceback 
from threading import Thread
import time 

class camera:
    def __init__(self, camera=0, resolution=(320,240)):
        # Initialize variables and constants
        self.RESOLUTION = [resolution[0], resolution[1]]
        self.FRAME_AVAILABLE = False        
        self.FRAME_TIME = 1
        self.FPS = 0
        self.KEY_PRESS = None
        self.FRAME = None
        
        try: 
            self.CAMERA = cv2.VideoCapture(camera)
            self.CAMERA.set(3, self.RESOLUTION[0])
            self.CAMERA.set(4, self.RESOLUTION[1])
            self.STOPPED = False 
            
            self.update_stream = Thread(target=self.update, args=())
            self.update_stream.daemon = True 
            self.update_stream.start()
            
        except:
            print traceback.format_exc(1)
            
    def __del__(self):
        self.STOPPED = True
        try:
            self.CAMERA.release()
            cv2.destroyAllWindows()
        except: 
            print traceback.format_exc(1)
            
    def update(self):
        while True: 
            if self.STOPPED: return
            start = time.time()
            (self.grabbed, self.FRAME) = self.CAMERA.read()
            self.FRAME_TIME = time.time() - start
            self.FPS = int(1/self.FRAME_TIME)
            self.FRAME_AVAILABLE = True
            
    def trackObject(self, hsv_thresh=((0,0,0),(255,255,255)), num_iterations=2, min_radius=10, cam_enable=False):
        if self.STOPPED: return
        if (self.FRAME_AVAILABLE == False): return(None, None, None);
        
        hsv = cv2.cvtColor(self.FRAME, cv2.COLOR_BGR2HSV)        
        mask = cv2.inRange(hsv, hsv_thresh[0], hsv_thresh[1])        
        mask = cv2.erode(mask, None, iterations=num_iterations)        
        mask = cv2.dilate(mask, None, iterations=num_iterations)        
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
        center = None
        if (len(cnts) > 0):
            c = max(cnts, key=cv2.contourArea)
            ((x,y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            
            if (radius < min_radius): center = None 
        
        if(cam_enable == True):
            cv2.imshow("Filtered Output", mask)
            cv2.imshow("Cam Output", self.FRAME)
        
        self.KEY_PRESS = cv2.waitKey(1) & 0xFF
        if(center == None): 
            return (None,None,None);
        else: return (center[0], center[1], radius);
            
    def trackObjectMasked(self, hsv_thresh=((0,0,0),(255,255,255)), window=(0,0), num_iterations=2, min_radius=10, cam_enable=False):
        if self.STOPPED: return
        if (self.FRAME_AVAILABLE == False): return(None, None, None);
        
        mask_temp = np.zeros((self.RESOLUTION[1], self.RESOLUTION[0]), np.uint8)
        cv2.rectangle(mask_temp, (self.RESOLUTION[0],self.RESOLUTION[1]-window[0]), (0,self.RESOLUTION[1]-window[1]), (255,255,255), -1)
        masked_data = cv2.bitwise_and(self.FRAME, self.FRAME, mask=mask_temp)
        
        hsv = cv2.cvtColor(masked_data, cv2.COLOR_BGR2HSV)        
        mask = cv2.inRange(hsv, hsv_thresh[0], hsv_thresh[1]) 
        
        mask = cv2.erode(mask, None, iterations=num_iterations)        
        mask = cv2.dilate(mask, None, iterations=num_iterations)        
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
        center = None
        if (len(cnts) > 0):
            c = max(cnts, key=cv2.contourArea)
            ((x,y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            
            if (radius < min_radius): center = None 
        
        if(cam_enable == True):
            cv2.imshow("Filtered Output", mask)
            cv2.imshow("Cam Output", masked_data)
        
        self.KEY_PRESS = cv2.waitKey(1) & 0xFF
        if(center == None): 
            return (None,None,None);
        else: return (center[0], center[1], radius);