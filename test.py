import cv2
import imutils
import math

img = cv2.imread("juice.jpg",0)
img = img[150:210,230:350]

for angle in range(-10,11,1):
    imgr=imutils.rotate_bound(img,angle)
    
    cv2.line(imgr, (0,39), (150,39), (0,255,0), 3)
    cv2.line(imgr, (0,7), (150,7), (0,255,0), 3)
    cv2.imshow("Frame",imgr)
    cv2.waitKey()