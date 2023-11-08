# We are using this file to save all the variables we are going to use later
import numpy
# These are the new values for the resized window
width = 1920 // 3
height = 1080 // 4

topLeft = (int(0.45 * width), int(0.75 * height))
bottomLeft = (0, height)
topRight = (int(0.55 * width), int(0.75 * height))
bottomRight = (width, height)

#trapezoidShape = numpy.array([topLeft, bottomLeft, bottomRight, topRight], dtype=numpy.int32)
#contour = numpy.array([(0, 0), (0, height), (width, height), (width, 0)], dtype=numpy.int32)

trapezoidShape = numpy.array([topLeft, topRight, bottomRight, bottomLeft])
contour = numpy.array([(0, height), (width, height), (width, 0), (0, 0)])
