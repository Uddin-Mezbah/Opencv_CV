import cv2
#import matplotlib
import matplotlib.pyplot as plt
import numpy as np





# Load image, grayscale, Gaussian blur, Otsu's threshold
image = cv2.imread("mask.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#red = cv2.cvtColor(image, cv2.COLOR_BGR2RED)

blur = cv2.GaussianBlur(gray, (5,5), 0)
thresh = cv2.threshold(blur, 1, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
thresh1 = cv2.threshold(gray, 2, 20, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
thresh2 = cv2.threshold(gray, 3, 150, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
print(thresh)
print(thresh1)
print(thresh2)

# Find bounding box
x ,y, w, h = cv2.boundingRect(thresh)
#cv2.rectangle(image, (x, y), (x + w, y + h), (36,255,12), 2)
cv2.rectangle(image, (x, y), (x + w, y + h), (36,255,12), 2)

cv2.putText(image, "w={},h={}".format(w,h), (x,y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (39,255,12), 2)

cv2.imshow("thresh", thresh)
cv2.imshow("thresh1", thresh1)
cv2.imshow("thresh2", thresh2)
cv2.imshow("image", image)
#plt.imshow()
cv2.waitKey()