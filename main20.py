import cv2

cap = cv2.VideoCapture(1)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

cap.set(3,180)
cap.set(5,180)