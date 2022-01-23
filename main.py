import cv2
import numpy as np


kernal = np.ones((10,10),np.uint8)
print(kernal)

path =('l.jpg')
img = cv2.imread(path)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
imgBlur = cv2.GaussianBlur(imgGray, (17, 17), 0)
imgCanny = cv2.Canny(imgBlur, 100, 100)
imgDilation = cv2.dilate(imgCanny, kernal, iterations= 1)
imgEroded = cv2.erode(imgDilation, kernal, iterations=1)
imgLine = cv2.line(img,(0,0),(img.shape[0]),(0,255,0),2)
thresh = cv2.threshold(imgBlur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

contours, hierarchy = cv2.findContours(imgCanny,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

cv2.imshow('Canny Edges After Contouring', imgCanny)
cv2.waitKey(0)
print("Number of Contours found = " + str(len(contours)))

cv2.drawContours(img, contours, -3, (1, 255, 1), 5)

cv2.imshow('Contours', img)


cv2.imshow('l.jpg', img)
cv2.imshow('GrayScale', imgGray)
cv2.imshow('Img Blur', imgBlur)
cv2.imshow('Img Canny', imgCanny)
cv2.imshow('Img Dilation', imgDilation)
cv2.imshow('Img Eroded', imgEroded)
cv2.imshow('Img Line ', imgLine)
cv2.imshow("thresh", thresh)



imgCanny2 = cv2.Canny(imgGray, 100, 100)
imgDilation2 = cv2.dilate(imgCanny2, kernal, iterations= 1)
imgEroded2 = cv2.erode(imgDilation2, kernal, iterations=1)




cv2.imshow('Img Canny2', imgCanny)
cv2.imshow('Img Dilation2', imgDilation)
cv2.imshow('Img Eroded2', imgEroded)
cv2.imageshow('Img Erodede3' , imgEroded)

cv2.waitKey(0)

