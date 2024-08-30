import cv2
from tkinter import Tk
from tkinter import filedialog


def show_image():
    image_Path = 'lolo.jpeg'
    imag_pat='lala.jpeg'


    image = cv2.imread(image_Path)
    img = cv2.imread(imag_pat)
    imgEE = cv2.imread('5b738129b1ded9d6c9178efe641e7537.jpg')
    imghh=cv2.imread('fruit-pictures-60gh8bz2qgbbzoy5.jpg')
    gray_image = applay(image)
    gray_imag = applay(img)
    gray_ima = applay(imgEE)
    gray_im = applay(imghh)
    cv2.imshow("gray_image", gray_image)
    cv2.imshow("gray_image1", gray_imag)
    cv2.imshow("gray_image2", gray_ima)
    cv2.imshow("gray_image3", gray_im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def applay(image):
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    return gray








'''
def get_path():
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    image_path = filedialog.askopenfilename(title="Select image", filetypes=(("image", "*.jpg"), ("all files", "*.*")))

    if image_path == "":
        print=("No image selected")
        return
'''


if __name__ == '__main__':

    show_image()