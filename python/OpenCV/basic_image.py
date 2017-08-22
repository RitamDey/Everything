import cv2
import numpy as np


# Loading the image
img = cv2.imread("pic.png")

# You can access a pixel value by its row and column coordinates.
# For BGR image, it returns an array of Blue, Green, Red values.
# For grayscale image, just corresponding intensity is returned.
px = img[100, 100]
print(px)


# Accessing only blue pixels
blue = img[100, 100, 0]
print(blue)

# We can modify the pixel values the same way
img[100, 100] = [255, 255, 255]
print(img[100, 100])
