import cv2
import numpy
from Variables import width, height

# This method converts the image to grayscale
def toGray(frame):
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)