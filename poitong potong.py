import cv2

image = "th.jpeg"

image_path = cv2.imread(image)
'''
def crop_image(image,x,y,w,h):
    # cropping image
    crop_img = image[y:y+h, x:x+w]
    return crop_img
cropped_image = crop_image(image_path, 0, 0, 100, 100)
cv2.imshow('Original Image', image_path)
cv2.imshow('Cropped Image', cropped_image)

def resize_image(image,scale_precentage):
    # resizing image
    width = int(image.shape[1] * scale_precentage / 100)
    height = int(image.shape[0] * scale_precentage / 100)
    resized_image = cv2.resize(image, (width, height))
    return resized_image
rezized_image = resize_image(image_path, 50)

cv2.imshow('Resized Image', rezized_image)





cv2.waitKey(0)
cv2.destroyAllWindows()
'''
def rotate_image(image, angle):
    center = (image.shape[1] // 2, image.shape[0] // 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (image.shape[1], image.shape[0]))
    return rotated_image

rotated_image = rotate_image(image_path, 180)
cv2.imshow ('Original Image', image_path)
cv2.imshow('Rotated Image', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()




