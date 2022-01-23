import cv2

path = ('7.png')
img = cv2.imread(path)
# print(img.shape)
# width = 1000
# height = 1000
# #right = 100
# imgResize = cv2.resize(img, (width, height))
# print(imgResize.shape)
#
# imgCropped = img[300:540, 430:480]
# #imgCropResize =cv2.resize (imgCropped,(img.shape[1],img.shape[0]))
#
# cv2.imshow("Davide",img)
# cv2.imshow("Davide Resize",imgResize)
# cv2.imshow("Davide Resize",imgCropped)
# #cv2.imshow("Davide Cropped Resize",imgCropResize)
#


cv2.waitKey()