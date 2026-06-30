import argparse
from time import sleep
from src.video import iter_frames
from src.image import process_image


def render_symbol_video(
    video_path: str,
    fps: int = 30,
    loop: bool = True,
    characters: str | None = None,
    preferred_width=None,
    preferred_height=None,
    invert: bool = False,
) -> None:
    for frame in iter_frames(video_path):
        print("\033[F" * 30, flush=True)
        print(
            process_image(
                image=frame,
                preferred_width=preferred_width,
                preferred_height=preferred_height,
                characters=characters if characters else "",
                invert=invert,
            ),
            flush=True,
        )
        sleep(1 / fps)
    if loop:
        render_symbol_video(
            video_path=video_path,
            fps=fps,
            loop=loop,
            characters=characters,
            preferred_width=preferred_width,
            preferred_height=preferred_height,
            invert=invert,
        )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate ASCII/character animation from a video",
    )

    parser.add_argument(
        "-p",
        "--video-path",
        required=True,
        help="Path to the input video file (required)",
    )

    parser.add_argument(
        "-f",
        "--fps",
        help="FPS of output animation",
    )

    parser.add_argument(
        "-l",
        "--loop",
        help="Loop video",
        action="store_true",
    )

    parser.add_argument(
        "-c",
        "--characters",
        required=False,
        help='Character set for drawing, ordered from darkest to brightest.\nDefault: " .:-=+*#%%@"',
    )

    parser.add_argument(
        "-w",
        "--output-width",
        required=False,
        help="Width of the output animation in characters.\nDefault: auto-calculated from video and terminal aspect ratio",
        type=int,
    )

    parser.add_argument(
        "-H",
        "--output-height",
        required=False,
        help="Height of the output text animation in characters.\nDefault: auto-calculated from video and terminal aspect ratio",
        type=int,
    )

    parser.add_argument(
        "-i",
        "--invert",
        help="Invert the brightness mapping",
        action="store_true",
    )
    args = parser.parse_args()
    render_symbol_video(
        video_path=args.video_path,
        fps=int(args.fps),
        loop=args.loop,
        characters=args.characters,
        preferred_width=args.output_width,
        preferred_height=args.output_height,
        invert=args.invert,
    )


if __name__ == "__main__":
    main()
