# import the necessary packages
import numpy as np
#import imutils
import cv2
import time

RESOLUTION      = (320,240)
TARGET_RADIUS   = 60
H_BAND          = 10
S_BAND          = 50
V_BAND          = 255 
ITERATIONS      = 2 

# Set up camera and set base resolution
camera = cv2.VideoCapture(-1)
camera.set(3, RESOLUTION[0])
camera.set(4, RESOLUTION[1])

def callback(value): pass

# Keep looping
while True:
    print "Fill the circle with the target color and press enter..."
    cv2.namedWindow("Trackbars", 0)
    cv2.createTrackbar("Target Radius", "Trackbars", TARGET_RADIUS, 120, callback)
    cv2.createTrackbar("H Bandwidth", "Trackbars", H_BAND, 255, callback)
    cv2.createTrackbar("S Bandwidth", "Trackbars", S_BAND, 255, callback)
    cv2.createTrackbar("V Bandwidth", "Trackbars", V_BAND, 255, callback)
    cv2.createTrackbar("Iterations", "Trackbars", ITERATIONS, 10, callback)
    while True:
        # Grab the current frame
        (grabbed, frame) = camera.read()        

        mask_temp = np.zeros((RESOLUTION[1], RESOLUTION[0]), np.uint8)
        cv2.rectangle(mask_temp, RESOLUTION, (0,0), (0,0,0), -1)
        cv2.circle(mask_temp, (int(RESOLUTION[0]/2), int(RESOLUTION[1]/2)), TARGET_RADIUS, (255,255,255), -1)

        masked_data = cv2.bitwise_and(frame, frame, mask=mask_temp)
        
        # Show the frame to our screen
        cv2.imshow("Target Detector 1.0", masked_data)
        key = cv2.waitKey(1) & 0xFF
        
        if (key == 10): break;
        TARGET_RADIUS = cv2.getTrackbarPos("Target Radius", "Trackbars")
        H_BAND = cv2.getTrackbarPos("H Bandwidth", "Trackbars")
        S_BAND = cv2.getTrackbarPos("S Bandwidth", "Trackbars")
        V_BAND = cv2.getTrackbarPos("V Bandwidth", "Trackbars")
        ITERATIONS = cv2.getTrackbarPos("Iterations", "Trackbars")
        
        
    # Convert the frame to HSV
    hsv = cv2.cvtColor(masked_data, cv2.COLOR_BGR2HSV) 
    
    average_counts = 0 
    average_hsv = [0, 0, 0]   
    
    for y in range(RESOLUTION[1]):
        temp = hsv.copy()
        cv2.line(temp, (0, y), (RESOLUTION[0], y), (0, 0, 255), 2)
        cv2.imshow("Target Detector 1.0", temp)
        key = cv2.waitKey(1) & 0xFF
        
        for x in range(RESOLUTION[0]):
            if ((hsv[y,x] == (0, 0, 0)).all()): pass 
            else: 
                average_counts += 1 
                average_hsv[0] += hsv[y,x][0]
                average_hsv[1] += hsv[y,x][1]
                average_hsv[2] += hsv[y,x][2]                
    average_hsv[0] = average_hsv[0] / average_counts
    average_hsv[1] = average_hsv[1] / average_counts
    average_hsv[2] = average_hsv[2] / average_counts
    print average_hsv
    
    HSV = [[0,0,0],[255,255,255]]
    
    HSV[0][0] = average_hsv[0] - H_BAND
    if(HSV[0][0] < 0): HSV[0][0] = 0
    
    HSV[0][1] = average_hsv[1] - S_BAND
    if(HSV[0][1] < 0): HSV[0][1] = 0
    
    HSV[0][2] = average_hsv[2] - V_BAND
    if(HSV[0][2] < 0): HSV[0][2] = 0
    
    HSV[1][0] = average_hsv[0] + H_BAND
    if(HSV[1][0] > 255): HSV[1][0] = 255
    
    HSV[1][1] = average_hsv[1] + S_BAND
    if(HSV[1][1] > 255): HSV[1][1] = 255
    
    HSV[1][2] = average_hsv[2] + V_BAND
    if(HSV[1][2] > 255): HSV[1][2] = 255
    
    print HSV
    
    
    
    while True:
        # Grab the current frame
        (grabbed, frame) = camera.read()        
        
        # Display to user the hsv threshold output image to determine useability
        output = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
        mask = cv2.inRange(output, (HSV[0][0], HSV[0][1], HSV[0][2]), (HSV[1][0], HSV[1][1], HSV[1][2]))
        mask = cv2.erode(mask, None, iterations=ITERATIONS)        
        mask = cv2.dilate(mask, None, iterations=ITERATIONS) 
        
        # Show the frame to our screen
        cv2.imshow("Target Detector 1.0", frame)
        cv2.imshow("Output", mask)
        key = cv2.waitKey(1) & 0xFF
        
        if (key == 10): break;
    
# Cleanup the camera and close any open windows
camera.release()
cv2.destroyAllWindows()
