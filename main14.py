import cv2
import numpy as np
import os

CANVAS_SIZE = (600, 800)
#FINAL_LINE_COLOR = (255, 255, 255,255)
#WORKING_LINE_COLOR = (127, 127, 127,127)
FINAL_LINE_COLOR = (355,355)
WORKING_LINE_COLOR = (227,227)
#workin_line_color = (377,299)
canvas_size = (700,800)



class PolygonDrawer(object):
    def __init__(self, window_name):
        self.window_name = window_name
        self.done = False
        self.current = (0, 0)
        self.points = []  #2130130105


    def on_mouse(self, event, x, y, buttons, user_param):
        pass


        if self.done:
            return

        if event == cv2.EVENT_MOUSEMOVE:
            self.current = (x, y)

        elif event == cv2.EVENT_LBUTTONDOWN:
            self.points.append((x, y))
            print("Adding point #%d with position(%d,%d)" % (len(self.points), x, y))

        elif event == cv2.EVENT_RBUTTONDOWN:
            self.done = True
            print("Completing polygon with %d points." % len(self.points))


    def run_mouse(self):
        # cv2.namedWindow(self.window_name, flags=cv2.CV_WINDOW_AUTOSIZE)
        cv2.namedWindow(self.window_name, cv2.WINDOW_AUTOSIZE)
        cv2.imshow(self.window_name, np.zeros(CANVAS_SIZE, np.uint8))
        cv2.waitKey(1)
        cv2.cv2.SetMouseCallback(self.window_name, self.run_mouse)
        #cv2.setMouseCallback(windowName, onMouse[, userdata])
        #cv2.cv2.SetMouseCallBack(image,run_mouse)

        while(not self.done):
            canvas = np.zeros(CANVAS_SIZE, np.uint8)

            if (len(self.points) > 0):
                cv2.polylines(canvas, np.array([self.points]), False, FINAL_LINE_COLOR, 1)
                cv2.line(canvas, self.points[-1], self.current, WORKING_LINE_COLOR)
                cv2.imshow(self.window_name, canvas)

            if cv2.waitKey(50) == 27:
                self.done = True
                canvas = np.zeros(CANVAS_SIZE, np.uint8)

            if (len(self.points) > 0):
                cv2.fillPoly(canvas, np.array([self.points]), FINAL_LINE_COLOR)
                cv2.imshow(self.window_name, canvas)
                cv2.waitKey()
                cv2.destroyWindow(self.window_name)
                return canvas



if __name__ == "__main__":
    poly = PolygonDrawer("Polygon")
    image = poly.run_mouse()
    cv2.imwrite("Polygon.png", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    #print("Polygon = %s" % poly.points)
    #print("Polygon = %")
