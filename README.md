# Image EyeTrack app

## Setup

### External System

- A server with Tobii Pro trackers that running [`tobii-grpc-server`](https://github.com/YMiyanohara/tobii-grpc-server) example server.

Note: You can run `tobii-grpc-server`'s example server and this application at the same computer.

### Software Requirements

- python (^3.10)
- pyenv (recommended)
- poetry (recommended)

## Usage

### Install

Run
`poetry install`
at the root of repository.

You may need to run `pyenv shell 3.XX.YY` then `poetry env use python` to specify which python version to be used by poetry.

### Configure

Please refer `config.yaml` to see available parameters.

Note: By default, configured to call `tobii-grpc-server` running at `localhost:50051`.

### Start appliaction

Run
`poetry run python image_eyetrack/runner.py`
at the root of repository.

### Set your own image
Place images to use in `image` dir, then change config.yaml IMG_PATH accordingly.

---

Sample image from: https://www.pexels.com/ja-jp/photo/276724/
