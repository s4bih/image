import cv2
from tkinter import Tk
from tkinter import filedialog


def show_image():
    image_Path = 'th.jpeg'
    image = cv2.imread(image_Path)
    cv2.imshow("image",image)

    apply = applay(image)
    cv2.imshow("image", apply)
    cv2.waitKey(0)
    cv2.destroyAllWindows()




def applay(image):
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    return gray


if __name__ == '__main__':
    show_image()