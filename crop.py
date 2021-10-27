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
col = 20
rows=30

roi3 = roi
count = 0
daterow1 = 0
daterow2 = 0
flag = False
while True:
    print(rows," ",col )
    roi3 = roi[rows:rows+1,0:col]
    
    if cv2.countNonZero(roi3)==0:
        if flag:
            if(daterow1 == 0):
                print("Image is black")
                daterow1 = rows
                flag = False
            else:
                print(daterow1)
                daterow2 = rows+3
                break;
            
        rows = rows +1
    else:
       print ("coloured image")
       flag = True
       rows=rows+1
date = roi[daterow1:daterow2,0:120]
cv2.imshow("Date", date)
row,col = date.shape
col = 0
colarr = []
i = 0 
flag = False 
while i < 8:
    roi4 = date[0:row,col:col+1]
    if(cv2.countNonZero(roi4)==0):
        if flag:
            print("ds")
            flag = False
            print(col,i)
            
            colarr.append(col)
            i = i+1
    else:
        flag = True
    
    col = col +1
i =0
# #while i < len(colarr):
# cv2.imshow("digit 1",date[0:row,0:colarr[0]])
# cv2.imshow("digit 2",date[0:row,colarr[0]:colarr[1]])
# cv2.imshow("digit 3",date[0:row,colarr[1]:colarr[2]])
# cv2.imshow("digit 4",date[0:row,colarr[2]:colarr[3]])
# cv2.imshow("digit 5",date[0:row,colarr[3]:colarr[4]])
# cv2.imshow("digit 6",date[0:row,colarr[4]:colarr[5]])
# cv2.imshow("digit 7",date[0:row,colarr[5]:colarr[6]])
# cv2.imshow("digit 8",date[0:row,colarr[6]:colarr[7]])

# angle = 25
# length = 50
# Point P1(30,50)
# Point P2;
# 
# P2.x = (int)round (P1.x + lenght * cos(angle * CV_PI / 180.0))
# P2.y = (int)round (P1.y + lenght * sin(angle * CV_PI / 180.0))
imheight,imwidth = roi.shape
print(imheight,imwidth)
# x=60
# y=30
# angle=25

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
#     print("endx1",endx1)
#     print("endy1",endy1)
#     print("endx2",endx2)
#     print("endy2",endy2)
    return endx1, endy1, endx2, endy2
#get_coords(60,30,25,imwidth , imheight)
print(get_coords(60,30,20,imwidth , imheight))
hmm=cv2.line(roi,(198,80),(-55,-12),(0,255,0),(3))
#lakir=cv2.line(img,(0,500),(500,0),(0,200,200),(10))
#axi taa na msha
# coordinate = []
# x = 0
# y = 0
# while y < 60: #many axi hi munm
#     while x < 120:
#         coordinate.append((x,y))
#         x += 1
#     coordinate.append((x,y))
#     y += 1
# print(coordinate)


cv2.imshow("img",roi)
cv2.waitKey(0)
