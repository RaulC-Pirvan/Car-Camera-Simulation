import cv2
import numpy
from Variables import width, height, edgeVertical, edgeHorizontal

def edgeDetection(frame):
    vertical = cv2.filter2D(numpy.float32(frame), -1, edgeVertical)
    horizontal = cv2.filter2D(numpy.float32(frame), -1, edgeHorizontal)

    result = numpy.sqrt((vertical**2)+(horizontal**2))

    return cv2.convertScaleAbs(result)