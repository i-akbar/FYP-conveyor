import cv2

img = cv2.imread("4.0005.jpg", 0)
ret, img = cv2.threshold(img, 115, 255, cv2.THRESH_BINARY)
cv2.imwrite(r"C:\Users\akbar\Desktop\FYP\FYP-conveyor\Database\chnage\4.0005.jpg", img)