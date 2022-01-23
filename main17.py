import cv2
import numpy as np

canvas = np.ones((400, 400, 3), dtype="uint8")
canvas *= 255

font = cv2.FONT_HERSHEY_SIMPLEX

cv2.putText(canvas, text="HelloWorld", org=(50, 200), fontFace=font, fontScale=2, thickness=1, lineType=cv2.LINE_AA, color=(0, 0, 255))

cv2.imwrite("draw_text.png", canvas)
cv2.imwrite("draw_text.png",canvas)

