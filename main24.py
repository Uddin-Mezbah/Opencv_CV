import cv2
import os

# dirname = "boli_fan_2021.9.10"
dirname = "boli_fan_2021.9.11/obj_train_data"


def change_img_ext(dirname):
    img_li = sorted(os.listdir(dirname))
    img_li = [x for x in img_li if x[-3:] == "bmp"]
    # img_li = [x for x in img_li if x[]]
    for imgfn in img_li:
        basename = imgfn.split(".")[0]
        img = cv2.imread(os.path.join(dirname, imgfn))
        cv2.imwrite(os.path.join(dirname, basename + '.jpg'), img)
        print(imgfn, " done")


def change_label(fname, src='4', target='1'):
    # pass
    label_1 = sorted(os.listdir(dirname))
    #label_2 = sorted(os.listdir(diename))
    print(label_1)


# label_1 = [x for x in label_1 if x[-3:]] == "src"]
#    label_1 = [x for x in label_1 if x[-3:]] == "target"]


def change_label_in_dir(dirname=".", src='4', target='1'):
    label_li = sorted(os.listdir(dirname))
    label_li = [x for x in label_li if x[-3:] == "txt"]
    for t in label_li:

        new_lines = []
        with open(os.path.join(dirname, t), 'r') as f:
            lines = f.readlines()
            for l in lines:
                if l[0] == src:
                    new_lines.append(target + l[1:])
                else:
                    new_lines.append(l)
        with open(os.path.join(dirname, t), 'w') as f:
            for l in new_lines:
                f.write(l)


# print(label_li)


if __name__ == "__main__":
    change_img_ext(dirname)
    change_label_in_dir(dirname=dirname, src='4', target='1')
    change_label_in_dir(dirname=dirname, src='5', target='2')
    # change_label_in_dir(dirname=dirname, src='6', target='3')
    # change_label_in_dir(dirname=dirname, src='7', target='4')
    # change_label_in_dir(dirname=dirname, src='8', target='5')
    # change_label_in_dir(dirname=dirname, src='9', target='6')
    # cahnge_label_in_dir(dirname=dirnaem, src='10', target='7')

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
