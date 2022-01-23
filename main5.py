import cv2
import numpy as np

# Let's load a simple image with 3 black squares
image = cv2.imread('l.jpg')
img1 = cv2.imread('l.jpg')
print(image)
cv2.waitKey(0)

# Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Find Canny edges
edged = cv2.Canny(gray, 300, 150)
edged = cv2.Canny(gray,400,150)
cv2.waitKey(0)

# Finding Contours

contours, hierarchy = cv2.findContours(edged,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)


cv2.imshow('Canny Edges After Contouring', edged)
cv2.waitKey(0)

print("Number of Contours found = " + str(len(contours)))
# Draw all contours
# #cv2.drawContours(img1, contours, -1, (0, 255, 0), 3)
# cv2.drawContours(img1, contours, -3, (1, 255, 1), 5)

# x ,y, w, h = cv2.boundingRect(thresh)
# #cv2.rectangle(image, (x, y), (x + w, y + h), (36,255,12), 2)
# cv2.rectangle(image, (x, y), (x + w, y + h), (36,255,12), 2)
# cv2.putText(image, "w={},h={}".format(w,h), (x,y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (39,255,12), 2)
# cv2.imshow("thresh", thresh)

# x,y,w,h = cv2.boundingRect(contours)
# image = cv2.rectangle(image, (x, y), (x + w, y + h), (36, 255, 12), 1)
# cv2.putText(image, 'Fedex', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)


rect = cv2.minAreaRect(contours[0])
rect_pts = cv2.boxPoints(rect)
rect_pts = np.int0(rect_pts)
print("rect_points ",rect_pts)
rect_img = cv2.drawContours(img1, [rect_pts], 0, (36, 255, 12), 2)
#rect_img = cv2.drawContours(img1, [rect_pts], -0, (-46, -50, -130), -1)

cv2.imshow('Contours', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

