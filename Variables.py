# We are using this file to save all the variables we are going to use later
import numpy

# These are the new values for the resized window
width = 1920 // 3
height = 1080 // 4

# We set some coordinates we're going to use later for task 4
topLeft = (int(0.45 * width), int(0.75 * height))
bottomLeft = (0, height)
topRight = (int(0.55 * width), int(0.75 * height))
bottomRight = (width, height)

# Using the coordinates above we create a trapezoid shape and contour for task 4
trapezoidShape = numpy.array([topLeft, bottomLeft, bottomRight, topRight])
trapezoidContour = numpy.array([(0, 0), (0, height), (width, height), (width, 0)])

# We are going to create a kernel for blurring
kernel = 3

# We create these values for our Sobel method
edgeVertical = numpy.float32([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
edgeHorizontal = numpy.transpose(edgeVertical)