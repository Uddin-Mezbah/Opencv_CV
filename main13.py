import cv2
import numpy as np

def draw_polylinnes():

    pass

    canvas = np.ones((500, 1000, 3), dtype="uint8")
    canvas *= 255

    points = np.array([[100,50],[200,300],[700,200],[500,100]], np.int32)
    #points = np.array([[100,100],[300,200],[400,200],[500,300]], np.int32)
    #points = np.array([[100,120],[300,220],[400,240],[500,260]], np.int32)
    #points = np.array([[100,150],[300,250],[400,350],[500,460]], np.int32)
    #points = np.array([[100,150],[300,250],[400,350],[500,460]], np.int32)
    points = np.array([[100,50],[200,300],[700,100],[500,177]], np.int32)
    points = np.array([[200,40],[300,30],[400,20],[500,100],[600,50], np.int32])


    points = points.reshape((-1,1,2))
    print("points after reshape")
    print(points)
# if __name__ == "__main__":
    cv2.polylines(canvas, pts=[points], isClosed=True, color=(0,0,255), thickness=3)

    cv2.imshow("polylines", canvas)
    cv2.imwrite("1.png", canvas)

    cv2.waitKey(0)

