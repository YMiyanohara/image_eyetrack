import atexit
import csv
import datetime
from pathlib import Path
from sys import platform

from tobii_remote.tobii_remote_pb2 import GazePosOnScreen


class Recorder:
    def __init__(self, data_dir: Path | str) -> None:
        if isinstance(data_dir, str):
            data_dir = Path(data_dir)
            data_dir.mkdir(parents=True, exist_ok=True)
        filepath = (
            str(data_dir)
            + "/"
            + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
            + ".csv"
        )
        if platform == "win32":
            self.csv_file = open(filepath, "w", newline="")
        else:
            self.csv_file = open(filepath, "w")
        self.writer = csv.writer(self.csv_file)

        # flags
        self.init_timestamp = None
        self.header_written = False

        atexit.register(self._close_file_desc)

    def record(self, timestamp: datetime.datetime | int, gaze_pos: GazePosOnScreen):
        if isinstance(timestamp, datetime.datetime):
            if not self.header_written:
                self.writer.writerow(["timestamp", "diff", "pos_x", "pos_y"])
                self.header_written = True

            if self.init_timestamp is None:
                self.init_timestamp = timestamp

            diff_ms = (timestamp - self.init_timestamp).total_seconds() * 1000
            timestamp = timestamp.isoformat()
            self.writer.writerow([timestamp, diff_ms, gaze_pos.pos_x, gaze_pos.pos_y])

        else:
            if not self.header_written:
                self.writer.writerow(["timestmap", "pos_x", "pos_y"])

            self.writer.writerow(timestamp, gaze_pos.pos_x, gaze_pos.pos_y)

    def _close_file_desc(self):
        self.csv_file.close()
