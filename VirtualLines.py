import cv2
import numpy as np

def setVirtualLines(frame, left_line, right_line, width, height):
    frameCopy = frame.copy()
    left_top_x = int((0 - left_line[0]) / left_line[1]) if abs((0 - left_line[0]) / left_line[1]) < 1e8 else 0
    left_bottom_x = int((height - left_line[0]) / left_line[1]) if abs((height - left_line[0]) / left_line[1]) < 1e8 else 0
    right_top_x = int((0 - right_line[0]) / right_line[1]) if abs((0 - right_line[0]) / right_line[1]) < 1e8 else 0
    right_bottom_x = int((height - right_line[0]) / right_line[1]) if abs((height - right_line[0]) / right_line[1]) < 1e8 else 0

    left_top_x = left_top_x if left_top_x else left_top_x if left_top_x else left_top_x
    left_bottom_x = left_bottom_x if left_bottom_x else left_bottom_x
    right_top_x = right_top_x if right_top_x else right_top_x
    right_bottom_x = right_bottom_x if right_bottom_x else right_bottom_x

    left_top = (left_top_x, 0)
    left_bottom = (left_bottom_x, height)
    right_top = (right_top_x + width // 2, 0)
    right_bottom = (right_bottom_x + width // 2, height)
    laneCoordinates = (left_top, right_top, left_bottom, right_bottom)

    cv2.line(frameCopy, left_top, left_bottom, (200, 0, 0), 5)
    cv2.line(frameCopy, right_top, right_bottom, (100, 0, 0), 5)
    cv2.line(frameCopy, (width // 2, 0), (width // 2, height), (255, 0, 0), 1)

    return frameCopy, laneCoordinates
