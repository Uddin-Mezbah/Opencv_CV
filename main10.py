import cv2
import numpy as np
import os

dirname = "obj_train_data"


def change_img_ext(dirname):
    img_li = sorted(os.listdir(dirname))
    img_li = [x for x in img_li if x[-3:] == "bmp"]
    for imgfn in img_li:
        basename = imgfn.split(".")[0]
        img = cv2.imread(os.path.join(dirname, imgfn))
        cv2.imwrite(os.path.join(dirname, basename+'.jpg'))




if __name__ == "__main__":
    change_img_ext(dirname)
# img_1 = cv2.imread("20210803101830860.jpg")
#
#
# # img_2 = cv2.imread("7.png")
# # img_3 = cv2.imread("2.png")
#
# # img_3 = img_1+img_2
# # img_4 = img_3 - img_2
#
# cv2.imshow("virtical", img_1)
# # cv2.imshow("horizontal", img_2)
# # cv2.imshow("Added image", img_3)
# # cv2.imshow("Subtract image", img_4)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()
