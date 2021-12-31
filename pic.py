
import cv2
vid = cv2.VideoCapture(0)  
# Capture the video frame
# by frame
ret, frame = vid.read()
# Display the resulting frame    cv2.imshow('frame', frame)
#cv2.imwrite("/home/pi/img.jpg",frame)
cv2.imshow('frame', frame)
# the 'q' button is set as the
# quitting button you may use any
# desired button of your choice
cv2.waitKey()
cv2.imwrite('pic2.jpg',frame)
# After the loop release the cap object
vid.release()
# Destroy all the windows
#cv2.destroyAllWindows()