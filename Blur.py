import cv2
from Variables import kernel


# This method blurs the image
def setBlur(frame):
    blur = cv2.blur(frame, ksize=(kernel, kernel))
    return blur
