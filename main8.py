import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('2.png')


templete = cv2.imread('1.png')
temp,temp1 = templete.shape[:2]
rv = cv2.matchTemplate(img,templete,cv2.TM_SQDIFF)
minval,maxval,minloc,maxloc = cv2.minMaxLoc(rv)

topLeft = minloc
bottomRight = (topLeft[0] + temp1, topLeft[1] + temp)
cv2.rectangle(img,topLeft,bottomRight,255,2)
plt.subplot(121),plt.imshow(rv,cmap = 'gray')
plt.title('Matching Result'), plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(rv,cmap = 'gray')
plt.title('Detectected Point')
plt.xticks('')
plt.yticks('')

plt.show()