import cv2
import numpy
from Variables import width, height

def setMarkingCoordinates(frame):
    frameCopy = frame.copy()

    frameCopy[:int(height*0.05), :width] = 0
    frameCopy[(int(height*0.95)):height, :width] = 0
    frameCopy[:height, :(int(width*0.05))] = 0
    frameCopy[:height, (int(width*0.95)):width] = 0

    leftHalf = frameCopy[:height, :(int(width/3))]
    rightHalf = frameCopy[:height, (int(width/3)):width]

    leftCoordinates = numpy.argwhere(leftHalf > 1)
    rightCoordinates = numpy.argwhere(rightHalf > 1)
    rightCoordinates[:, 1] = rightCoordinates[:, 1] + width/3

    leftX = leftCoordinates[:, 1]
    leftY = leftCoordinates[:, 0]
    rightX = rightCoordinates[:, 1]
    rightY = rightCoordinates[:, 0]

    markingCoordinates = (leftX, leftY, rightX, rightY)

    return frameCopy, markingCoordinates
