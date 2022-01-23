import cv2
import os

dirname = "boli_fan_2021.9.10"

def change_img_ext(dirname):
    img_li = sorted(os.listdir(dirname))
    img_li = [x for x in img_li if x[-3:] == "bmp"]
    for imgfn in img_li:
        basename = imgfn.split(".")[0]
        img = cv2.imread(os.path.join(dirname, imgfn))
        cv2.imwrite(os.path.join(dirname, basename+'.jpg'),img)
        print(imgfn," done.")




if __name__ == "__main__":
    change_img_ext(dirname)