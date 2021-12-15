import Fusion
import time 

camera      = 0                             # Selects first camera detected
resolution  = (320,240)                     # Set camera resolution (width,height)
hsv_value   = ((50,80,30),(80,255,255))    # Set lower/upper HSV boundaries
iterations  = 2                             # Cleanup Iterations (optional)
radius      = 10                             # Set the minimum pixel radius for detection 
cam_output  = True                         # See the camera output when in VNC or HDMI

# Constructor for the camera class 
cam = Fusion.usbCamera(camera, resolution, hsv_value, iterations, radius, cam_output)

while True:
    # Print the (x,y) coordinates of the centroid of the object
    # based on the resolution.
    print str(cam.COORDINATES) + "  " + str(cam.RADIUS)
    time.sleep(0.01)