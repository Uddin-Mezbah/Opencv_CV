import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('1.png')
cv2.imshow('original',img)
gray = cv2.cvtColor(0,cv2.color_BGR2GRAY)
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
image,contours,heirarchy = cv2.findContours(binary,cv2.RETER_LIST,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(o.contours[0],-1,(0,0,255),3)
cntArea = cv2.contourArea((contours[0]))

equiDiameter = np.sqrt(4*cntArea/np.pi)
print(equiDiameter )
cv2.circle(img,(100,100), int(equiDiameter/2),(0,0,255),3)
cv2.imshow("result", img)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.dwstroyAllwindows()
cv2.waitkey()