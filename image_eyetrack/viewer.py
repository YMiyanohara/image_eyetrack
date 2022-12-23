import atexit

import cv2
import numpy as np

WINDOW_NAME = "Image Viewer"


class Viewer:
    def __init__(self, width: int, height: int, fullscreen: bool = False) -> None:
        cv2.namedWindow(WINDOW_NAME, cv2.WINDOW_NORMAL)
        if fullscreen:
            cv2.setWindowProperty(
                WINDOW_NAME, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN
            )
        self.width = width
        self.height = height
        atexit.register(self._close)

    def show(self, img: np.ndarray):
        cv2.resize(img, (self.height, self.width))
        cv2.imshow(WINDOW_NAME, img)
        cv2.waitKey(1)

    def _close(self):
        cv2.destroyWindow(WINDOW_NAME)
