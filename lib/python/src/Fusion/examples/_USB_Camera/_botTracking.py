# import the necessary packages
from collections import deque
import numpy as np
import argparse
import imutils
import cv2
                
# Define the lower and upper boundaries of the "green"
# ball in the HSV color space, then initialize the
# list of tracked points
greenLower = (18, 18, 33)
greenUpper = (45, 206, 231)

#greenLower = (50, 12, 63)
#greenUpper = (95, 183, 247)


camera = cv2.VideoCapture(-1)
camera.set(3, 320)
camera.set(4, 240)

# Keep looping
while True:
    # Grab the current frame
    (grabbed, frame) = camera.read()
    
    # Resize the frame, blur it, and convert it to the HSV
    # color space.
    #frame = imutils.resize(frame, width=600)
    # blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Construct a mask for the color "green", then perform
    # a series of dialations and erosions to remove and small
    # blobs left in the mask
    mask = cv2.inRange(hsv, greenLower, greenUpper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    # Find contours in the mask and initalize the current
    # (x,y) center of the ball
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None

    # Only procede if at least one contour was found
    if (len(cnts) > 0):
        # Find the largest contour in the mask, then use
        # it to compute the minimum enclosing circle and
        # centroid
        c = max(cnts, key=cv2.contourArea)
        ((x,y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        #if radius > 10:
        cv2.circle(frame, (int(x), int(y)), int(radius), (0,255,255), 2)
        cv2.circle(frame, center, 5, (0,0,255), -1)

    # Show the frame to our screen
    cv2.imshow("Frame", frame)
    cv2.imshow("output", mask)
    key = cv2.waitKey(1) & 0xFF

    print center

    # If the 'q' key is pressed, stop the loop
    if key == ord("q"):
        break;

# Cleanup the camera and close any open windows
camera.release()
cv2.destroyAllWindows()
