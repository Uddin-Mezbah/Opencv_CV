import cv2
import numpy as np
import os

canvas = np.ones((600, 600, 3), dtype="uint8")
canvas *= 255


cv2.ellpipse(img=canvas,center=(256,256), axes=(100,50), angle=0, startAngle=0, endAngle=360, color=(100, 200, 0), thickness=-1)
cv2.ellpipse2(img=canvas,center = (356,456), axes = (200,100), angle = 0, startAngle = 0, endAngle=360, color=(100,200,0), thickness = -1)

cv2.imshow("draw_ellpipse", canvas)
cv2.imshow("draw_ellpipse2", canvas)
#cv2.imwrite("draw_ellipse.png", canvas)
cv2.waitKey(0)