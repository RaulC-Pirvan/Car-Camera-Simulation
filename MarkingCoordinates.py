import numpy
from Variables import width


# Using this method we are going to create the Markings Coordinates
def setMarkingCoordinates(frame):
    frameCopy = frame.copy()
    leftHalf = frameCopy[:, :int(width / 2)]
    rightHalf = frameCopy[:, int(width / 2):]

    leftCoordinates = numpy.argwhere(leftHalf > 1)
    rightCoordinates = numpy.argwhere(rightHalf > 1)
    leftX, leftY = leftCoordinates[:, 1], leftCoordinates[:, 0]

    if rightCoordinates.size > 0 and len(rightCoordinates.shape) > 1 and rightCoordinates.shape[1] > 1:
        rightX, rightY = rightCoordinates[:, 1], rightCoordinates[:, 0]
    else:
        rightX, rightY = [], []  # Empty arrays if rightCoordinates doesn't have expected structure

    markingCoordinates = (leftX, leftY, rightX, rightY)

    return frameCopy, markingCoordinates
