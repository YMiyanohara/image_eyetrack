import sys
from datetime import datetime
from time import sleep

import cv2
import numpy as np
import yaml
from recorder import Recorder
from tracker import Tracker
from viewer import Viewer

TOBII_REMOTE_HOST = "localhost"
TOBII_REMOTE_PORT = 50051

WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080
FULLSCREEN = False

DATA_DIR = "./data"
IMG_PATH = ""


def main():
    tracker = Tracker(TOBII_REMOTE_HOST, TOBII_REMOTE_PORT)
    recorder = Recorder(DATA_DIR)
    viewer = Viewer(WINDOW_WIDTH, WINDOW_HEIGHT, FULLSCREEN)

    img: np.ndarray = cv2.imread(IMG_PATH)
    viewer.show(img)

    # stop = False
    print("Crtl-C or press a key to stop")
    while True:
        gaze = tracker.get_gaze_pos()
        recorder.record(datetime.now(), gaze)
        if cv2.waitKey(1) != -1:
            sys.exit(0)


if __name__ == "__main__":
    with open("./config.yaml", "r") as f:
        conf = yaml.safe_load(f)

    # global TOBII_REMOTE_HOST, TOBII_REMOTE_PORT, DATA_DIR, IMG_PATH, WINDOW_HEIGHT, WINDOW_WIDTH, FULLSCREEN

    TOBII_REMOTE_HOST = conf["TOBII_REMOTE_HOST"]
    TOBII_REMOTE_PORT = conf["TOBII_REMOTE_PORT"]
    DATA_DIR = conf["DATA_DIR"]
    IMG_PATH = conf["IMG_PATH"]
    WINDOW_WIDTH = conf["WINDOW_WIDTH"]
    WINDOW_HEIGHT = conf["WINDOW_HEIGHT"]
    FULLSCREEN = conf["FULLSCREEN"]

    main()
