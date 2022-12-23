# Setup

## Requirements

### External System

- A server with Tobii Pro trackers that running [`tobii-grpc-server`](https://github.com/YMiyanohara/tobii-grpc-server)

Note: You can run `tobii-grpc-server` and this software at the same computer.

### Software

- python (^3.10)
- pyenv (recommended)
- poetry (recommended)

# Usage

## Install

Run
`poetry install`
at the root of repository.

You may need to run `pyenv shell 3.XX.YY` then `poetry env use python` to specify which python version to be used by poetry.

## Configure

Please refer `config.yaml` to see available parameters.

Note: By default, configured to call `tobii-grpc-server` running at `localhost:50051`.

## Start appliaction

Run
`poetry run python image_eyetrack/runner.py`
at the root of repository.

---

Sample image from: https://www.pexels.com/ja-jp/photo/276724/
