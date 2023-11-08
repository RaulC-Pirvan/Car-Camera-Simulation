import cv2
import numpy
from Variables import width, height

# This method resized the window to our specified values
def resizeWindow(frame):
    resizedWindow = cv2.resize(frame, (width, height))
    return resizedWindow