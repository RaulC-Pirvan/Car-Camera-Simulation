import cv2
import numpy
from Variables import width, height

def setMarkingCoordinates(frame):
    frameCopy = frame.copy()
    frameCopy[:, :int(width*0.05)] = 0
    frameCopy[:, :int(width*0.95)] = 0
    leftHalf = frameCopy[:, :width//2]
    rightHalf = frameCopy[:, :width//2:]
    leftCoordinates = numpy.argwhere(leftHalf == 255)
    rightCoordinates = numpy.argwhere(rightHalf == 255)
    leftX, leftY = leftCoordinates[:, 1], leftCoordinates[:, 0]
    rightX, rightY = rightCoordinates[:, 1] + (width//2), rightCoordinates[:, 0]
    markingCoordinates = (leftX, leftY, rightX, rightY)
    return markingCoordinates
