import cv2
import numpy
from Variables import width, height, kernel

# This method blurs the image
def setBlur(frame):
    blur = cv2.blur(frame, ksize=(kernel, kernel))
    return blur