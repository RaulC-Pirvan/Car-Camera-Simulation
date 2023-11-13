import cv2


# We use this method to convert each pixel either to complete black or complete white
def toBinary(frame):
    initialThreshold = int(255/2)
    _, binarizedFrame = cv2.threshold(frame, initialThreshold, 255, cv2.THRESH_BINARY)
    return binarizedFrame
