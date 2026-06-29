import ffmpeg
import numpy as np
from PIL import Image
from collections.abc import Iterator


def get_video_size(video_path: str) -> tuple[int, int]:
    probe = ffmpeg.probe(video_path)
    video_stream = next(
        (
            stream
            for stream in probe["streams"]
            if stream["codec_type"] == "video"
        ),
        None,
    )
    return int(video_stream["width"]), int(video_stream["height"])


def iter_frames(video_path: str) -> Iterator[Image]:
    width, height = get_video_size(video_path)
    frame_size_in_bytes = width * height * 3

    video_reading_process = (
        ffmpeg.input(video_path)
        .output("pipe:", format="rawvideo", pix_fmt="rgb24")
        .run_async(pipe_stdout=True)
    )

    while True:
        frame_bytes = video_reading_process.stdout.read(frame_size_in_bytes)

        if len(frame_bytes) != frame_size_in_bytes:
            break

        frame_array = np.frombuffer(frame_bytes, np.uint8).reshape(
            [height, width, 3]
        )
        yield Image.fromarray(frame_array)
