import cv2
import numpy as np

img = cv2.imread("/home/pi/juice.jpg",0)
ret, bw =cv2.threshold(img,74,255,cv2.THRESH_BINARY)
img = 255 - bw 
cv2.imshow("Binary",bw)
r1 = 150
r2 = 210
c1 = 235
c2 = 350
cut_image = img[r1:r2,c1:c2]
cv2.imshow("cut image", cut_image)
cut = cut_image
row, col = cut_image.shape
row = int(row / 2)
while True:
    print(row," ",col )
    col = 20
    cut = cut_image[row:row+1,0:col]
    cv2.imshow("row", cut)
    if cv2.countNonZero(cut)==0:
        print("Image is black")
        break
    else:
        print ("coloured image")
        row = row +1 
print("image is black")
    
cv2.waitKey(0)