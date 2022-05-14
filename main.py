from tkinter import W
import cv2


#Read the image to the image variable to do operations on it
image = cv2.imread("images/testImage.jpg", cv2.IMREAD_COLOR)

#Resize the image to make it easier to work with
#Create aspect ratio for our image that we want to resize
#Grab the width and height of the shape
(h, w) = image.shape[:2]
resize_value = 400

#Create our actual aspect ratio
ratio = resize_valuet/w
dim = (resize_value, int(h * ratio))

#Resize the image to a manageable size
resized_image = cv2.resize(image, dim)

#Actually display the image
cv2.imshow("Resized_Image",resized_image)

#Provide a wait time for the image to be displayed 0 so it is continuously displayed
cv2.waitKey(0)


