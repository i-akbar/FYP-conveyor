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
#rows = int(rows / 2)
col = int(cols/2)
rows=int(rows/2)

roi3 = roi
daterow1 = 0
while True:
    print(rows," ",col )
    roi3 = roi[rows:rows+1,col-8:col+8]
    #print(roi[rows:rows+1,col-8:col+8])
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
    return int(endx1), int(endy1),int(endx2),int( endy2)

height,width = roi.shape
col3=int(width/4)
col4=int(width/3)
# endx1, endy1, endx2, endy2 =get_coords(col,rows+1,10,imwidth , imheight)

for x in range(1,21,5):
    #for y in range(1,5):
    endx1, endy1, endx2, endy2 =get_coords(col,rows+1,x,width,height)
#        print(endx1, endy1, endx2, endy2)
    print("angle",x)
    hmm=cv2.line(roi,(endx1,endy1),(endx2,endy2),(0,255,0),(1))
    cv2.imshow("img",hmm)
    hihi=imutils.rotate_bound(hmm,-10)
    cv2.imshow("hmm",hihi)
    print("x and y asta")
    X = (endx1-endx2)
    Y = (endy1-endy2)
    print("X",X)
    print("Y",Y)
    M = Y/X
    print("slope m is :",M)
    Yarray = []
    print("width",width)
    for z in range(0,width):
        yaxis = M*z
        Yarray.append(yaxis)
    print("Y axis", Yarray)
    plt.plot(Yarray)
    plt.show()
    

    
        
#endx1, endy1, endx2, endy2 =get_coords(col,rows+1,y,width ,height)
        
#hmm=cv2.line(roi,(endx1,endy1),(endx2,endy2),(0,255,0),(1))
#hmm=hmm[endx1:endy1,endx2:endy2]
#for(i in range(1,20))

    

# print("x and y asta")
# X = (endx1-endx2)
# Y = (endy1-endy2)
# print("X",X)
# print("Y",Y)
# M = Y/X
# print("slope m is :",M)
# mid = int(height/2)
# Yarray = []
# print("width",width)
# for z in range(0,width):
#     yaxis = M*z
#     Yarray.append(yaxis)
# print("Y axis", Yarray)
# plt.plot(Yarray)
# plt.show()

    
#for x in range()
# print(hmm)
# x=np.arange(endx1,endx2,1)
# y=np.arange(endy1,endy2,-1)
# plt.scatter(x,y)
# plt.show()
# 
# pixles=[]
# for x in range(endx2, endx1):
#     for y in range(endy2, endy1):
#         pass
#         #print(x)
#         #pixles.append(hmm[x][y])
# print(pixles)
#          
#                  
# coordinate = []
# x = endx1
# y = endy1
# while y < endy2: #many axi hi munm
#     while x < endx2:
#         coordinate.append((x,y))
#         x += 1Roi
#     coordinate.append((x,y))
#     y += 1
#     print(coordinate)
#cv2.imwrite(roi)
#cv2.imshow("hmm",hmm)
cv2.waitKey(0)