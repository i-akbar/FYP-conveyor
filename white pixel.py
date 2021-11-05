import cv2
import numpy as np
import math
import pygame
import imutils
import matplotlib.pyplot as plt

img = cv2.imread("/home/pi/juice.jpg",0)
ret, bw =cv2.threshold(img,74,255,cv2.THRESH_BINARY)
# cv2.imshow("ds",img)
img = 255 - bw

rows, cols = img.shape
print("Rows", rows)
print("Cols", cols)

cut_image = img[150: 480,50:640]
cv2.rectangle(img, (230,150), (350,210), (0,255,0), 3) #line cropped img wala asta

#cv2.imshow("Cut image",cut_image)

roi = img[150:210,230:350] #image ra cut kdi sirf crop shi mny roi eshti
cv2.rectangle(roi,(10,49),(20,49),(0,255,0),1)
cv2.imshow("Roi",roi)
#cv2.waitkey(0)
# 
rows, cols = roi.shape
print("Rows", rows)
print("Cols",cols)
#cv2.rectangle(roi,(10,33),(30,34),(0,255,0),6)
#roi2 = roi[33:34,10:110]

rows, cols = roi.shape
rows = int(rows / 2)
col = int(cols/2)

roi3 = roi
daterow1 = 0
pixles=[]
while True:
    #print(rows," ",col )
    roi3 = roi[rows:rows+1,col-8:col+8]
    #print(roi[rows:rows+1,col-8:col+8])
    if cv2.countNonZero(roi3)==0:
        print("Image is black at row" , rows, " col " , col)
        daterow1 = rows
        print(daterow1)
        break;

    else:
        print ("coloured image")
        rows=rows+1
for i in range(0,16,5):
    #y = i/2
    roi3=imutils.rotate(roi,i)
    #rows=int(rows/2)
    rows = 0

    #roi3 = roi
   
    
    #while(rows < 59):
    #print(rows," ",col )
    white = 0
    for j in range(0,120):
        roi4 = roi3[daterow1:daterow1+1,j:j+1]
        
        #cv2.imshow("roi",roi3)
        #print(roi[rows:rows+1,col-8:col+8])
        
        if cv2.countNonZero(roi4)!=0:
            #print("Image is black at row" , rows, " col 1 -" , 80, "Angle " , y)
            
            #print ("coloured image")
            white = white+1
    print("White: ",white , "row num", daterow1, "angle" , i)
    pixles.append(white)
print("white pixles in array:",pixles)
plt.plot(pixles)
plt.show()
    
date = roi[daterow1:daterow1+1,1:120]
#cv2.imshow("Date", date)
