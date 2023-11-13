import cv2
import numpy
from Variables import width, height, trapezoidShape, trapezoidContour


# With this method we are going to generate our Final Output
def finalOutput(laneCoordinates):
    output = numpy.zeros((height, width, 3), dtype=numpy.uint8)
    cv2.line(output, laneCoordinates[0], laneCoordinates[2], (255, 0, 0), 5)
    cv2.line(output, laneCoordinates[1], laneCoordinates[3], (0, 255, 0), 5)

    contour = numpy.float32(trapezoidContour)
    shape = numpy.float32(trapezoidShape)

    bounds = cv2.getPerspectiveTransform(contour, shape)
    output = cv2.warpPerspective(output, bounds, (width, height))

    return output
