import cv2 as cv

def draw_circle(event, x, y, flags, param):
    pass

    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img, center=(x, y), radius=5,
                  color=(255, 0, 0), thickness=-1)

    elif event == cv.EVENT_RBUTTONDOWN:
        cv.circle(img, center=(x, y), radius=5,
                  color=(0, 255, 0), thickness=1)


img = cv.imread('8.png')

cv.namedWindow(winname='drawing')
cv.setMouseCallback('drawing', draw_circle)

while True:
    cv.imshow('drawing', img)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()