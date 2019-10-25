import cv2
import numpy as np
cap = cv2.VideoCapture(0)
#just an iterator for naming images
i=1
# Read until video is completed
while(cap.isOpened()):
  ret, frame = cap.read()
  if ret == True:
    cv2.imshow('Frame',frame)
    if (cv2.waitKey(1)!=-1):
        cv2.imwrite('captured_images/image'+str(i)+'.png', frame)
        i = i+1
    # Press Q on keyboard to  exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

# When everything done, release the video capture object
cap.release()
cv2.destroyAllWindows()
