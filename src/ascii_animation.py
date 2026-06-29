import ffmpeg
import numpy as np
from PIL import Image
from time import sleep
from main import process_image
from characters import STYLE_2


def get_video_size(video_path: str):
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


def generate_frames_from_video(video_path: str, fps: int):
    width, height = get_video_size(video_path)
    frame_size = width * height * 3

    video_reading_process = (
        ffmpeg.input(video_path)
        .output("pipe:", format="rawvideo", pix_fmt="rgb24")
        .run_async(pipe_stdout=True)
    )

    while True:
        frame_bytes = video_reading_process.stdout.read(frame_size)
        if len(frame_bytes) != frame_size:
            break
        frame_array = np.frombuffer(frame_bytes, np.uint8).reshape([height, width, 3])
        out_frame = process_image(
            image=Image.fromarray(frame_array), characters=STYLE_2, invert=True
        )
        print(out_frame)
        sleep(1 / fps)


def print_animation_from_files() -> None:
    files = (
        f"./alien_frames/output_{str(i).rjust(4, '0')}.png"
        for i in range(1, 242)
    )
    for file_name in files:
        frame = process_image(
            image=Image.open(file_name), characters=STYLE_2, invert=True
        )
        print(frame)
        sleep(1 / 30)

while True:
    generate_frames_from_video(video_path="./assets/alien.mp4", fps=60)

