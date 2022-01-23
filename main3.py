import cv2
import numpy as np
#from import imghow


# img = np.zeros((100,100,3),np.uint8)
# print(img)
#
# cv2.imgshow("image", img)
#
#
# cv2.waitKey(0)
# cv2.destroyAllWindows(0)

img = np.zeros((1000, 1000, 3), np.uint8)
print(img)
#img[:] = 255, 0,0
cv2.namedWindow('img', cv2.WINDOW_NORMAL)
#cv2.resizeWindow('img', 800, 600)

#cv2.line(img,(0,0),(100,100),(0,255,0),2)
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),2)
cv2.rectangle(img,(300,100),(450,200),(0,0,255),cv2.FILLED)
cv2.circle(img,"Draw Shape",(75,50),cv2.FONT)


cv2.imshow('img',img)
cv2.waitKey(0)
# cv2.destroyWindow(0)
# print(img)
