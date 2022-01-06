import cv2
import imutils  # to make IP function, translation, rotation, resizing, displaying matplotlib images
import matplotlib.pyplot as plt
import collections

# img = cv2.imread(r"C:\Users\akbar\Desktop\FYP\FYP-conveyor\FYPdatabase\10.jpg", 0)  # Akbar pc
img = cv2.imread(r"D:\semester7\FYP1\FYP-conveyor\FYPdatabase\9.jpg", 0)  # Cheeni pc
ret, bw = cv2.threshold(img, 110, 255, cv2.THRESH_BINARY)  # setting threshold

img = 255 - bw
# cv2.imshow('img0',img)

# cv2.waitKey()
# img = img[215:258, 280:365]  # crop for pic4
# img = img[200:260,290:430]
# img = img[135:174,310:450]  #crop for pic1 (uper,lower,left,right)
# img = img[150:210,230:350]   #crop for juice
#img = img[185:250,200:305]  #for Db 1,threshold-100
#img = img[210:280,120:305]  #for Db 2, threshold-110
#img = img[175:240,180:330]  #for Db 3, threshold-125
#img = img[120:174,300:410]   # db 4 , threshhold 120  Rthrshold 30 for 4-4-4
#img = img[185:240,200:320] #for Db 5,threshold-110
# img = img[210:280,150:305] #for Db 6, threshold-100
# img = img[150:225,230:350] #for Db 7, threshold-100
# img = img[130:180,290:400] #DB 8
img = img[120:180, 270:380] # DB 9 10
# img = img[110:160, 280:400] #DB 11
# img = img[110:170, 280:400] #DB 12 thrshhold 100
# img = img[120:170, 280:380] #DB 12-12 and bd 12-12-12 thshhold 90
# img = img[100:160, 280:400] #DB 13 thshhold 100
#img = img[100:160, 280:400] #DB 13 thshhold 100


# img = img[135:174,310:450]  #crop for pic1 (uper,lower,left,right)
# img = img[150:210,230:350]   #crop for juice

cv2.imshow('img', img)
cv2.waitKey()
rows, cols = img.shape
# ---------count white pixels in rows ------------------
arr = []
arr2 = []

for angle in range(-10, 11, 1):
    # y = i/2
    arrrow = []
    imgr = imutils.rotate_bound(img, angle)
    for r in range(0, rows):
        count = 0
        flag = False
        for c in range(0, cols):
            pixel = imgr[r:r + 1, c:c + 1]
            if cv2.countNonZero(pixel) != 0:
                if (flag == False):
                    # flag = True
                    count = count + 1
            else:
                flag = False

        # print("angle:" , angle , "row:" , r , "white:",count)
        angleIndex = int((angle / 5) + 2)
        arrrow.append(count)
    arr.append(arrrow)

    arrcol = []
    imgr = imutils.rotate_bound(img, angle)
    for c in range(0, cols):
        count = 0
        flag = False
        for r in range(0, rows):
            pixel = imgr[r:r + 1, c:c + 1]
            if cv2.countNonZero(pixel) != 0:
                if (flag == False):
                    # flag = True
                    count = count + 1
            else:
                flag = False

        # print("angle:" , angle , "row:" , r , "white:",count)
        # angleIndex = int((angle/5)+2)
        arrcol.append(count)
    arr2.append(arrcol)

counter = []
flag = True
for i in range(0, 21):
    temp = arr[i]
    count = 0
    for j in range(len(temp)):
        if (flag):
            if (temp[j] < 5):
                count = count + 1

                #                 print("value count :",count)
                flag = False
        else:
            if (temp[j] > 25):
                flag = True
    counter.append(count)

print(counter)
maxValue = max(counter)

maxIndex = counter.index(maxValue)
angle = maxIndex - 10
print(maxValue, angle)
imgr = imutils.rotate_bound(img, angle)

cv2.imshow("rotated img", imgr)

# count white pixels in rows
arrayrow = []
#  imgr=imutils.rotate_bound(img,angle)
for r in range(0, rows):
    count = 0
    flag = False
    for c in range(0, cols):
        pixel = imgr[r:r + 1, c:c + 1]
        if cv2.countNonZero(pixel) != 0:
            if (flag == False):
                # flag = True
                count = count + 1
        else:
            flag = False
    arrayrow.append(count)
plt.plot(arrayrow,color = 'navy',marker='o')
plt.show()
print("arrayrow", arrayrow)

counters = []
flag = False
counts = 0
index = []
for j in range(len(arrayrow)):
    if flag:
        print(flag)
        if j + 1 < len(arrayrow):
            if arrayrow[j + 1] > arrayrow[j] <8:  # threshhold ra ax 5 ta check mna
                index.append(j)
                flag = False
                print(flag)
    else:
        if arrayrow[j] > 18:
            flag = True

# counters.append(counts)
# print("counters", counters)
# -------------------------
rowbow, colmol = imgr.shape
# print("rowbow", rowbow)
# index = []
# for i in range(0, len(arrayrow)):  # threshhold ra ax 13 ta bad mila
#     if (arrayrow[i] != 0):
#         if (arrayrow[i] < 13):
#             index.append(i)

print("indeeeex", len(index))
X = []
for j in range(0, len(index)):

    startpoint = (0, index[j])
    endpoint = (colmol, index[j])
    picture = imgr
    # picture = cv2.line(imgr, startpoint, endpoint, (255, 0, 0), 1)

    row, col = picture.shape
    print("index array ", index)
    print("rows picture", row)
    print("col picture: ", col)
    ln = len(index)
    print("length", ln)
    if index[j] == index[ln - 1]:
        f_ind = index[j]
        sec_ind = row
    else:
        f_ind = index[j]
        sec_ind = index[j + 1]
    print("ind : ", f_ind)
    print("ind  2nd: ", sec_ind)
    #     print("roi size",(imgr[f_ind:sec_ind,10:120]).shape)
    roi = imgr[f_ind:sec_ind, 0:col]  # image ra cut kdi sirf crop shi mny roi eshti
    cv2.imshow("picture", picture)
    X.append(roi)
# for i in range(0,len(X)):
#     cv2.imshow(" image ",X[i])
#     time.sleep(2)
cv2.imshow("1st image", X[0])  # for pic4
# cv2.imshow("2nd image",X[1])
#  cv2.imshow("3rd image",X[2])
#  cv2.imshow("4rth image",X[3])
#  cv2.imshow("picture",picture)
# cv2.imshow("picture2",crop_image)
expiry = X[1]
menufacture = X[0]
rows, cols = expiry.shape
# print("expiry row",ex_row)
# print("expiry col",ex_col)
cv2.imshow("expiry", expiry)
 # image pixels of cols
arraycoln = []
for c in range(0, cols):
    count = 0
    flag = False
    for r in range(1, rows):
        pixel = expiry[r:r + 1, c:c + 1]
        if cv2.countNonZero(pixel) != 0:
            if (flag == False):
                # flag = True
                count = count + 1
        else:
            flag = False
    arraycoln.append(count)

plt.plot(arraycoln, color='navy', marker='o')
print("arraycoln ", arraycoln)
flag = False
colwhite = []
px = 7
for x in range(0, len(arraycoln)):
    if x + 1 != len(arraycoln):

        # if(flag):
        if px > 6:
            # if (arraycoln[x] < arraycoln[x + 1] and arraycoln[x+1] != 0):
            if (arraycoln[x] < arraycoln[x + 1] != 0
                    and arraycoln[x] <= 8):  # for juice last condition x+1=>0
                colwhite.append(x)
                flag = False
                px = 0
        else:
            #             pass

            if arraycoln[x] > 0:
                flag = True

            if flag:
                px = px + 1
        # if(arraycoln[x]>7):

        # flag = True
    else:
        pass
print(len(colwhite))
print("white pixles of col:", colwhite)
Y = []
for j in range(0, len(colwhite)):
    startpoint = (colwhite[j], 0)
    endpoint = (colwhite[j], rows)
    # picture = cv2.line(expiry, startpoint, endpoint, (255, 0, 0), 1)
    ln = len(colwhite)
    row, col = picture.shape
    #     print("length", ln)
    if (colwhite[j] == colwhite[ln - 1]):
        f_ind = colwhite[j]
        sec_ind = col
    else:
        f_ind = colwhite[j]
        sec_ind = colwhite[j + 1]
    roi = expiry[0:row, f_ind:sec_ind]
    #     cv2.imshow("me",roi)
    coords = cv2.findNonZero(roi)  # Find all non-zero points (text)
    x, y, w, h = cv2.boundingRect(coords)  # Find minimum spanning bounding box
    rect = roi[y:y + h, x:x + w]
    resized = cv2.resize(rect, (20, 30), interpolation=cv2.INTER_AREA)

    Y.append(resized)
cv2.imshow("Crop 0", Y[0])
cv2.imshow("Croped 1 ", Y[1])
cv2.imshow("Croped 2", Y[2])
cv2.imshow("Croped 3", Y[3])
cv2.imshow("Croped 4", Y[4])
cv2.imshow("Croped 5", Y[5])
cv2.imshow("Croped 6", Y[6])
cv2.imshow("Croped 7", Y[7])
cv2.imwrite("1.0003.jpg",Y[0])
cv2.imwrite("1.0004.jpg",Y[1])
cv2.imwrite("1.0005.jpg",Y[3])
cv2.imwrite("1.0006.jpg",Y[4])
cv2.imwrite("2.0011.jpg",Y[6])
cv2.imwrite("1.0007.jpg",Y[7])
# cv2.imshow("Croped 8", Y[8])
# cv2.imshow("Croped 9",Y[9])
#  cv2.imshow("Croped 10",Y[10])
#  cv2.imshow("Croped 11",Y[11])
#  cv2.imshow("Croped 12",Y[12])
#  cv2.imshow("Croped 13",Y[13])
cv2.imshow("new", picture)
print("length of Y:", (len(Y)))
plt.title("Expiry")
plt.show()

cv2.waitKey()
cv2.waitKey()
