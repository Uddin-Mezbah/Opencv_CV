import cv2
import  numpy as np

img_1 = cv2.imread("2.png",1)
img_2 = cv2.imread("2.png",1)
img_3 = img_1 + img_2
cv2.imshow("horizontal",img_2)
cv2.imshow("vertical",img_1)
cv2.imshow("Added image", img_3)

cv2.waitKey(10000)
cv2.destroyAllWindows