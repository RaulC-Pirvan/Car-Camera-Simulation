import cv2
import numpy
from Variables import width, height, trapezoidShape

def toTrapezoid(frame):
    # We create a black shape
    trapezoid = numpy.zeros((height, width), dtype=numpy.uint8)

    # Here we want to modify the shape from a box to a trapezoid, and we do that with our second argument
    # Moving forward we are going to fill it with the colour White (1
    trapezoid = cv2.fillConvexPoly(trapezoid, trapezoidShape, 1)
    return trapezoid
