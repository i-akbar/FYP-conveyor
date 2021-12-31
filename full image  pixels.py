import cv2
import numpy as np
import math
import pygame
import imutils
import matplotlib.pyplot as plt
from array import *
import collections

img = cv2.imread("juice.jpg",0)
ret, bw =cv2.threshold(img,70,255,cv2.THRESH_BINARY)
# cv2.imshow("ds",img)
img = 255 - bw
#cv2.imshow('img0',img)

#cv2.waitKey()
#img = img[215:258,280:365]
#img = img[200:260,290:430]
img = img[150:210,230:350]
cv2.imshow('img',img)
rows, cols = img.shape
#---------count white pixels in rows ------------------
arr= []
arr2=[]

for angle in range(-10,11,1):
    #y = i/2
    arrrow = []
    imgr=imutils.rotate_bound(img,angle)
    for r in range(0,rows):
        count=0
        flag = False
        for c in range(0,cols):
            pixel = imgr[r:r+1,c:c+1]
            if cv2.countNonZero(pixel)!=0:
                if(flag == False):
                    #flag = True
                    count = count + 1
            else:
                flag = False
            
        #print("angle:" , angle , "row:" , r , "white:",count)
        angleIndex = int((angle/5)+2)
        arrrow.append(count)
    arr.append(arrrow)
    
    arrcol = []
    imgr=imutils.rotate_bound(img,angle)
    for c in range(0,cols):
        count=0
        flag = False
        for r in range(0,rows):
            pixel = imgr[r:r+1,c:c+1]
            if cv2.countNonZero(pixel)!=0:
                if(flag == False):
                    #flag = True
                    count = count + 1
            else:
                flag = False
            
        #print("angle:" , angle , "row:" , r , "white:",count)
        #angleIndex = int((angle/5)+2)
        arrcol.append(count)
    arr2.append(arrcol)
    
    
    
# print("--------row--------")
# for r in arr:
#     
#     #print((r-2)*5 , " ")
#     for c in r:
#         print(c, end =" ")
#     print()

#---------count white pixels in cloumns ------------------
# arr2= []
# 
# for angle in range(-10,11,5):
#     #y = i/2
#     arrcol = []
#     imgr=imutils.rotate_bound(img,angle)
#     for c in range(0,cols):
#         count=0
#         flag = False
#         for r in range(0,rows):
#             pixel = imgr[r:r+1,c:c+1]
#             if cv2.countNonZero(pixel)!=0:
#                 if(flag == False):
#                     #flag = True
#                     count = count + 1
#             else:
#                 flag = False
#             
#         #print("angle:" , angle , "row:" , r , "white:",count)
#         angleIndex = int((angle/5)+2)
#         arrcol.append(count)
#     arr2.insert(angleIndex,arrcol)
#print("--------col-------")



# for r in arr2:
#     
#     #print((r-2)*5 , " ")
#     for c in r:
#         print(c, end =" ")
#     print()




#img2 = img[41:42,0:84]

counter=[]
flag = True
for i in range(0,21):
    temp = arr[i]
    count = 0
    for j in range(len(temp)):
        if(flag):
            if(temp[j] < 5):
                count = count + 1
#                 print("value count :",count)
                flag = False
        else:
            if(temp[j] > 25):
                flag = True
    counter.append(count)

print(counter)
maxValue = max(counter)

maxIndex = counter.index(maxValue)
angle = maxIndex -10
print(maxValue,angle)



# for i in range(0,21):
#     #freq = collections.Counter(arr[i])
#     #freq = collections.OrderedDict(freq.most_common())
#     plt.plot(arr[i],color = 'navy',marker='o')
#     #print(freq)
#     plt.title("angle: "+str(i-10) )
#     plt.show()
# for i in range(0,21):
#     #freq = collections.Counter(arr2[i])
#     #freq = collections.OrderedDict(fre.most_common())
#     plt.plot(arr2[i],color = 'navy',marker='o')
#     plt.title("angle: "+str(i-10) )
#     plt.show()

# for i in range(0,21):
#     freq = collections.Counter(arr[i])
#     freq = collections.OrderedDict(freq.most_common())
#     #print(freq.most_common()[0])
# #     if freq[0]
# #         print(freq[1])
#     plt.plot(freq.keys(),freq.values())
#     plt.title("angle: "+str(i-10) )
#     plt.show()
imgr = imutils.rotate_bound(img,angle)
cv2.imshow("check", imgr)
cv2.waitKey()
