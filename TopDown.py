import cv2
import numpy
from Variables import width, height, trapezoidShape, trapezoidContour


# This method creates a Top-Down view for our camera
def toTopDown(frame):
    tpContour = numpy.float32(trapezoidContour)
    tpTrapezoidShape = numpy.float32(trapezoidShape)

    tpLimits = cv2.getPerspectiveTransform(tpTrapezoidShape, tpContour)
    tp = cv2.warpPerspective(frame, tpLimits, (width, height))

    return tp
