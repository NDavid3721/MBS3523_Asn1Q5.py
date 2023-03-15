import cv2
import numpy as np

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

cv2.namedWindow('Adjust Line')


def update_line_position(x):
    img = np.zeros((WINDOW_HEIGHT, WINDOW_WIDTH, 3), np.uint8)

    line_position = x * WINDOW_WIDTH // 100
    cv2.line(img, (line_position, 0), (line_position, WINDOW_HEIGHT), (0, 255, 0), 2)

    cv2.imshow('Adjust Line', img)


cv2.createTrackbar('Line Position', 'Adjust Line', 0, 100, update_line_position)

cv2.imshow('Adjust Line', np.zeros((WINDOW_HEIGHT, WINDOW_WIDTH, 3), np.uint8))

cv2.waitKey(0)

cv2.destroyAllWindows()

