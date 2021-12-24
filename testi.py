import cv2
import numpy as np
import math
import pygame
import imutils
import matplotlib.pyplot as plt
from array import *
import collections
import time
import collections 
from PIL import Image

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
imgr = imutils.rotate_bound(img,angle)
# **************************
# print("shape : ",imgr.shape) era shafi kdad bekraya
# for i in range(imgr.shape[0]):
#     for j in range(imgr.shape[1]):
#         if (imgr[i][j]==1):
#             print("cordinates : ",i,j)


cv2.imshow("rotated img", imgr)

#count white pixels in rows 
arrayrow = []
# imgr=imutils.rotate_bound(img,angle)
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
    arrayrow.append(count)
#plt.plot(arrayrow,color = 'navy',marker='o')
print("arrayrow", arrayrow)
   
    

counters=[]
flag = True
counts = 0
for j in range(len(arrayrow)):
    if(flag):
        if(arrayrow[j] < 5): #threshhold ra ax 5 ta check mna
            
            counts = counts + 1
            flag = False    
    else:
        if(temp[j] > 25):
            flag = True
            


counters.append(counts)
print("counters",counters)
rowbow,colmol= imgr.shape
print("rowbow",rowbow) 
index=[]
for i in range(0,len(arrayrow)): #threshhold ra ax 13 ta bad mila
    if(arrayrow[i]!=0):
        if (arrayrow[i]<13):
            
            index.append(i)
    
print(len(index))
X=[]
for j in range(0,len(index)):
    
    startpoint=(0,index[j])
    endpoint=(colmol,index[j])
    picture=cv2.line(imgr,startpoint,endpoint,(255,0,0),1)
    row,col=picture.shape
    print("index array ",index)
    print("rows picture", row)
    print("col picture: ", col)
    ln= len(index)
    print("length", ln)
    if (index[j]== index[ln-1]):
        f_ind=index[j]
        sec_ind=row
    else:
        f_ind= index[j]
        sec_ind= index[j+1]
    print("ind : ",f_ind)
    print("ind  2nd: ",sec_ind)
#     print("roi size",(imgr[f_ind:sec_ind,10:120]).shape)
    roi = imgr[f_ind:sec_ind,10:120] #image ra cut kdi sirf crop shi mny roi eshti
    cv2.imshow("picture",picture)    
    X.append(roi)
# for i in range(0,len(X)):
#     cv2.imshow(" image ",X[i])
#     time.sleep(2)
# cv2.imshow("1st image",X[0])
cv2.imshow("2nd image",X[1])
# cv2.imshow("3rd image",X[2])
# cv2.imshow("4rth image",X[3])
# cv2.imshow("picture",picture)
# cv2.imshow("picture2",crop_image)
expiry=X[1]
menufacture=X[2]
rows,cols = expiry.shape
# print("expiry row",ex_row)
# print("expiry col",ex_col)
cv2.imshow("expiry",expiry)
print("expiry ",expiry)
#image pixels of cols
arraycoln=[]
for c in range(0,cols):
    count=0
    flag = False
    for r in range(1,rows):
        pixel = expiry[r:r+1,c:c+1]
        if cv2.countNonZero(pixel)!=0:
            if(flag == False):
                    #flag = True
                count = count + 1
        else:
            flag = False
    arraycoln.append(count)

plt.plot(arraycoln,color = 'navy',marker='o')
print("arraycoln ", arraycoln)

colwhite=[]
for x in range(0,len(arraycoln)):
    if(x+1!=len(arraycoln)):
        if(arraycoln[x]==0 and arraycoln[x+1] > 0 or arraycoln[x]>0 and arraycoln[x]<=3 and arraycoln[x+1] >= 0 ):
            colwhite.append(x)
    else:
        pass
print(len(colwhite))
print("white pixles of col:",colwhite)
Y=[]
for j in range(0,len(colwhite)):
    startpoint=(colwhite[j],0)
    endpoint=(colwhite[j],rows)
    picture=cv2.line(expiry,startpoint,endpoint,(255,0,0),1)
    ln= len(colwhite)
    row,col=picture.shape
#     print("length", ln)
    if (colwhite[j]== colwhite[ln-1]):
        f_ind=colwhite[j]
        sec_ind=col
    else:
        f_ind= colwhite[j]
        sec_ind= colwhite[j+1]
    roi = expiry[0:row,f_ind:sec_ind]
    Y.append(roi)
# cv2.imshow("Croped 1 ",Y[1])
# cv2.imshow("Croped 2",Y[2])
# cv2.imshow("Croped 3",Y[3])
# cv2.imshow("Croped 3",Y[4])
# cv2.imshow("Croped 4",Y[5])
# cv2.imshow("Croped 5",Y[6])
# cv2.imshow("Croped 6",Y[7])
# cv2.imshow("new",picture)
# plt.title("angle: "+str(0) )
# plt.show()

#axi bad nia

# print("colnarray:",colarr) 
cv2.imshow("digit 1",expiry[0:row,0:Y[0]])
cv2.imshow("digit 2",expiry[0:row,Y[0]:Y[1]])
cv2.imshow("digit 3",expiry[0:row,Y[1]:Y[2]])
cv2.imshow("digit 4",expiry[0:row,Y[2]:Y[3]])
cv2.imshow("digit 5",expiry[0:row,Y[3]:Y[4]])
cv2.imshow("digit 6",expiry[0:row,Y[4]:Y[5]])
cv2.imshow("digit 7",expiry[0:row,Y[5]:Y[6]])
cv2.imshow("digit 8",expiry[0:row,Y[6]:Y[7]])
plt.title("angle: "+str(0) )
plt.show()

cv2.waitKey()


