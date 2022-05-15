from tkinter import W
import cv2
import numpy as np


#Read the image to the image variable 
image = cv2.imread("images/testImage.jpg", cv2.IMREAD_COLOR)

#Resize the image to make it easier to work with
#Create aspect ratio for our image that we want to resize
#Grab the width and height of the shape
(h, w) = image.shape[:2]
resize_value = 400

#Create our actual aspect ratio
ratio = resize_value/w
dim = (resize_value, int(h * ratio))

#Resize the image to a manageable size
resized_image = cv2.resize(image, dim)

#Actually display the resized image
cv2.imshow("Resized_Image", resized_image)

# #Provide a wait time for the image to be displayed 0 so it is displayed indefinitely
# cv2.waitKey(0)

# #Make a copy of the original image and then display a rectangle on it 
# drawn_output = resized_image.copy()
# rectangle = cv2.rectangle(drawn_output, (100,50),(50, 10), (255, 0, 0), 2)

# #Display the new image with the rectangle
# cv2.imshow("Drawn Image", drawn_output)
# cv2.waitKey(0)

#Detect the edges of our image and then display the image of edges

#Create an edges variable that is the mapped edges of our image
edges = cv2.Canny(resized_image, 100, 200)

#Display the image with all of the detected edges
cv2.imshow("Image Edges", edges)
cv2.waitKey(0)
