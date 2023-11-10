import cv2
from Resize import resizeWindow
from Grayscale import toGray
from RoadOnly import toTrapezoid
from TopDown import toTopDown
from Blur import setBlur
from EdgeDetection import edgeDetection
import numpy

cam = cv2.VideoCapture('Lane Detection Test Video-01.mp4')

while True:
    # ret (bool): Returns if the "read" operation was successful or not
    # frame (array) : The actual frame as an array
    #                 If the image is color, we have Height x Width x 3 (BGR)
    #                 If we have a grayscale image, we have Height x Width
    # cam.read() : Reads the next frame from the video source (i.e. Lane Detection Test Video-01.mp4)
    #              And it continues processing frames until there are no more frames to read
    ret, frame = cam.read()

    # If ret == false that means our operation has failed, i.e. we cannot read the camera
    if ret is False:
        break

    resizedWindow = resizeWindow(frame)
    grayWindow = toGray(resizedWindow)
    trapezoidWindow = toTrapezoid(grayWindow)
    topDownWindow = toTopDown(trapezoidWindow * grayWindow)
    blurWindow = setBlur(topDownWindow)
    edgeDetectionWindow = edgeDetection(blurWindow)

    # The syntax of the command is as followed: cv2.imshow(window_name, image)
    # Here we are going to create all the windows
    cv2.imshow('Resized Window', resizedWindow)                     # TASK 2
    cv2.imshow('Grayscale Window', grayWindow)                      # TASK 3
    cv2.imshow("Road-Only Window", trapezoidWindow * grayWindow)    # TASK 4
    cv2.imshow("Top-Down Window", topDownWindow)                    # TASK 5
    cv2.imshow("Blurred Window", blurWindow)                        # TASK 6
    #cv2.imshow("Edge-Detection Window", edgeDetectionWindow)        # TASK 7
    # Here we use the "q" key to close the windows
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# We use cam.release() to close the file we are reading from
cam.release()

# We use destroyAllWindows() to close all the OpenCV windows
cv2.destroyAllWindows()