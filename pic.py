
import cv2

vid = cv2.VideoCapture(0)  
# Capture the video frame
# by frame
ret, img = vid.read()
# Display the resulting frame    cv2.imshow('frame', frame)
#cv2.imwrite("/home/pi/img.jpg",frame)
cv2.imshow('image',img)
# the 'q' button is set as the
# quitting button you may use any
# desired button of your choice
#cv2.imread('img',frame)
cv2.imwrite("4-4-4.jpg",img)
cv2.waitKey(0)
# After the loop release the cap object

vid.release()
# Destroy all the windows
cv2.destroyAllWindows()