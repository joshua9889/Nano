#!/usr/bin/python
from SimpleWebSocketServer import WebSocket, SimpleWebSocketServer
import time
import traceback
from threading import Thread
import socket
import SimpleHTTPServer
import SocketServer
import os
import commands   
import atexit 

# Exit function to ensure the video feed process has been killed 
def checkVideo():
    temp = commands.getoutput('pgrep mjpg')
    if temp: 
        try: os.system("kill " + str(temp))
        except: pass         

atexit.register(checkVideo)

# Get the absolute path for linking files and folders to module
abs_path = os.path.abspath(__file__)
if '__init__.' in abs_path:
    lib_path = abs_path[:abs_path.index('__init__.')]
    
# Global variables
incomming_data = ""
outgoing_buffer = [None]*20
outgoing_data = None
connected = False
data_array = []

class service:
    def __init__(self, cam=False, res=(320,240), fps=10, mode='YUV'):
        startServer(cam, res, fps, mode)
        
    def leftJoystick(self, mixer=False, x_inv=False, y_inv=False):
        global data_array
        time.sleep(0.001)
        
        invert = [1, 1]
        if(x_inv): invert[0] *= -1
        if(y_inv): invert[1] *= -1
        
        if(mixer):
            try:
                x = data_array[0]*2*invert[0]
                y = data_array[1]*2*invert[1]*-1
                                
                left_motor = y - x
                if(left_motor >= 100): left_motor = 100
                elif (left_motor <= -100): left_motor = -100
                
                right_motor = y + x
                if(right_motor >= 100): right_motor = 100 
                elif(right_motor <= -100): right_motor = -100
                
                return (left_motor, right_motor);                
            except:
                return(0, 0);
        else:
            try:
                return (data_array[0]*2*invert[0], data_array[1]*2*invert[1]*-1);
            except:
                return(0, 0);
                
    def rightJoystick(self, mixer=False, x_inv=False, y_inv=False):
        global data_array
        time.sleep(0.001)
        
        invert = [1, 1]
        if(x_inv): invert[0] *= -1
        if(y_inv): invert[1] *= -1 
        
        if(mixer):
            try:
                x = data_array[2]*2*invert[0]
                y = data_array[3]*2*invert[1]*-1
                
                left_motor = y - x
                if(left_motor >= 100): left_motor = 100
                elif (left_motor <= -100): left_motor = -100
                
                right_motor = y + x
                if(right_motor >= 100): right_motor = 100 
                elif(right_motor <= -100): right_motor = -100
                
                return (left_motor, right_motor);                
            except:
                return(0, 0);
        else:
            try:
                return (data_array[2]*2*invert[0], data_array[3]*2*invert[1]*-1);
            except:
                return(0, 0);
            
    def readButton(self, button):
        global data_array
        time.sleep(0.001)
        temp = 0        
        if(button == 'A'): temp = 0
        elif(button == 'B'): temp = 1     
        elif(button == 'X'): temp = 2 
        elif(button == 'Y'): temp = 3 
        elif((button==0) or (button==1) or (button==2) or (button==3)): temp = button
        else: return (-1)
        try:
            return data_array[4+temp]
        except:
            return 0;                    

    def telemetry(self, line, value):
        global outgoing_buffer
        outgoing_buffer[line] = value
        return;

class SimpleEcho(WebSocket):
  def handleMessage(self):
    global incomming_data, outgoing_data, outgoing_buffer
    global data_array
    
    incomming_data = self.data
    if(incomming_data != None):
        data_array = incomming_data.split()
        data_array = map(int, data_array)
      
    outgoing_data = ''
    for i in range(len(outgoing_buffer)):
        if(outgoing_buffer[i] != None):
            outgoing_data += str(outgoing_buffer[i]) + '<br />'
    if(outgoing_data != ''): self.sendMessage(outgoing_data)
    
  def handleConnected(self): 
    global connected 
    connected = True
    print self.address, 'connected'

  def handleClose(self):
    global connected 
    connected = False
    print self.address, 'closed'

def controlThread():
    global control_object
    try:
        control_object = SimpleWebSocketServer('', 12345, SimpleEcho)
        control_object.serveforever()
    except:
        print traceback.format_exc(1)
        control_object.close()

class MyTCPServer(SocketServer.TCPServer):
    def server_bind(self):
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(self.server_address)

class MyHTTPRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_my_headers()
        SimpleHTTPServer.SimpleHTTPRequestHandler.end_headers(self)

    def send_my_headers(self):
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        
    def translate_path(self,path):
        path = SimpleHTTPServer.SimpleHTTPRequestHandler.translate_path(self,path)
        if (os.path.isdir(path)):
            return lib_path 
        if '/misc' in path:
            return lib_path + path[path.find('misc'):];
        if '/css' in path:
            return lib_path + path[path.find('css'):];
        if '/js' in path:
            return lib_path + path[path.find('js'):];
        return path
        
def serverThread():
    s = MyHTTPRequestHandler
    httpd = MyTCPServer(("", 5000), s)
    httpd.serve_forever()
    
def startServer(camera, resolution, frame_rate, mode):
    try:        
        if(camera == True):
            if(mode == "MJPG"):
                os.system('LD_LIBRARY_PATH=' + lib_path + 'mjpg_streamer ' + lib_path + 'mjpg_streamer/mjpg_streamer -i "input_uvc.so -r ' + str(resolution[0]) + 'x' + str(resolution[1]) +' -f ' + str(frame_rate) + '" -o "output_http.so -p 9080" &')
            if(mode == "PICAM"):    
                os.system('LD_LIBRARY_PATH=' + lib_path + 'mjpg_streamer ' + lib_path + 'mjpg_streamer/mjpg_streamer -i "input_raspicam.so -fps '+ str(frame_rate) +' -x ' + str(resolution[0]) + ' -y ' + str(resolution[1]) +'" -o "output_http.so -p 9080" &')
            else:   
                os.system('LD_LIBRARY_PATH=' + lib_path + 'mjpg_streamer ' + lib_path + 'mjpg_streamer/mjpg_streamer -i "input_uvc.so -y -r ' + str(resolution[0]) + 'x' + str(resolution[1]) +' -f ' + str(frame_rate) + '" -o "output_http.so -p 9080" &')
        
        server_thread = Thread(target=serverThread, args=())
        server_thread.daemon = True 
        server_thread.start() 
        
        control_thread = Thread(target=controlThread, args=())
        control_thread.daemon = True
        control_thread.start()
        print "Server now running..."
        
    except:
        print traceback.format_exc(1)        
