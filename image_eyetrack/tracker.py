import atexit
import os

import grpc
from tobii_remote.tobii_remote_pb2 import (
    GazePosOnScreen,
    google_dot_protobuf_dot_empty__pb2,
)
from tobii_remote.tobii_remote_pb2_grpc import TobiiRemoteStub


class Tracker:
    def __init__(self, grpc_server_hostname: str, grpc_server_port: int):
        grpc_server = grpc_server_hostname + ":" + str(grpc_server_port)

        self.grpc_channel = grpc.insecure_channel(grpc_server)
        self.tracker = TobiiRemoteStub(self.grpc_channel)

        atexit.register(self._close_grpc_channel)

    def get_gaze_pos(self) -> GazePosOnScreen:
        empty = google_dot_protobuf_dot_empty__pb2.Empty()
        gaze_pos: GazePosOnScreen = self.tracker.GetGazePosOnScreen(empty)
        return gaze_pos

    def _close_grpc_channel(self):
        self.grpc_channel.close()
        print("Closed gRPC channel")
