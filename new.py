import cv2
import numpy as np
import math
import pygame

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
#rows = int(rows / 2)
col = int(cols/2)
rows=int(rows/2)

roi3 = roi
daterow1 = 0
while True:
    print(rows," ",col )
    roi3 = roi[rows:rows+1,col-8:col+8]
    
    if cv2.countNonZero(roi3)==0:
        print("Image is black at row" , rows, " col " , col)
        daterow1 = rows
        break;

    else:
        print ("coloured image")
        rows=rows+1
date = roi[daterow1:daterow1+1,col-8:col+8]
cv2.imshow("Date", date)

def get_coords(x, y, angle, imwidth, imheight):

    x1_length = (x-imwidth) / math.cos(angle)
    y1_length = (y-imheight) / math.sin(angle)
    length = max(abs(x1_length), abs(y1_length))
    endx1 = x + length * math.cos(math.radians(angle))
    endy1 = y + length * math.sin(math.radians(angle))

    x2_length = (x-imwidth) / math.cos(angle+180)
    y2_length = (y-imheight) / math.sin(angle+180)
    length = max(abs(x2_length), abs(y2_length))
    endx2 = x + length * math.cos(math.radians(angle+180))
    endy2 = y + length * math.sin(math.radians(angle+180))
    return endx1, endy1, endx2, endy2

imheight,imwidth = roi.shape
print(get_coords(col,rows+1,5,imwidth , imheight))
hmm=cv2.line(roi,(270,54),(-9,30),(0,255,0),(1))
cv2.imshow("img",roi)
cv2.waitKey(0)