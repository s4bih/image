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
def get_path():
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    image_path = filedialog.askopenfilename(title="Select image", filetypes=(("image", "*.jpg"), ("all files", "*.*")))

    if image_path == "":
        print=("No image selected")
        return

    image=cv2.imread(image_path)
    cv2.imshow("image",image)

    gray_image=applay(image)
    cv2.imshow("gray_image",gray_image)


    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':

    get_path()