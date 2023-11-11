import cv2
import numpy
from Variables import height, width

def setVirtualLines(frame, tuple):
    leftLane = numpy.polynomial.polynomial.polyfit(tuple[0], tuple[1], 1)
    righLane = numpy.polynomial.polynomial.polyfit(tuple[2], tuple[3], 1)
    leftTopY = 0
    leftTopX = (0 - leftLane[0]) / leftLane[1]
    leftBottomY = height
    leftBottomX = (height - leftLane[0]) / leftLane[1]
    rightTopY = 0
    rightTopX = (0 - righLane[0]) / righLane[1]
    rightBottomY = height
    rightBottomX = (height - righLane[0]) / righLane[1]
    leftTop = (int(leftTopX), int(leftTopY))
    rightTop = (int(rightTopX), int(rightTopY))
    leftBottom = (int(leftBottomY), int(leftBottomX))
    rightBottom = (int(rightBottomX), int(rightBottomY))
    cv2.line(frame, leftTop, leftBottom, (100, 0, 0), 5)
    cv2.line(frame, rightTop, rightBottom, (200, 0, 0), 5)
    coordinates = (leftTop, rightTop, leftBottom, rightBottom)
    return frame, coordinates