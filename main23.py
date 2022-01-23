import cv2
import numpy as np
import matplotlib
from PIL import  Image

'''img1 = cv2.imread('l.jpg', cv2.IMREAD_UNCHANGED)
b,g,r = (img1[100, 100])
print (r)
print (g)
print (b)

cv2.waitKey(0)
cv2.destroyAllWindows()'''

#from PIL import Image

im = Image.open('l.jpg')
im_grey = im.convert('LA') # convert to grayscale
width, height = im.size

total = 0
for i in range(0, width):
    for j in range(0, height):
        total += im_grey.getpixel((i,j))[0]

mean = total / (width * height)
print(mean)
