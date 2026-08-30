import argparse
from PIL import Image
from src.image import process_image


def main():
    parser = argparse.ArgumentParser(
        description="Generate ASCII/character art from an image",
    )

    parser.add_argument(
        "-p",
        "--image-path",
        required=True,
        help="Path to the input image file (required)",
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
        help="Width of the output text art in characters.\nDefault: auto-calculated from image and terminal aspect ratio",
        type=int,
    )

    parser.add_argument(
        "-H",
        "--output-height",
        required=False,
        help="Height of the output text art in characters.\nDefault: auto-calculated from image and terminal aspect ratio",
        type=int,
    )

    parser.add_argument(
        "-i",
        "--invert",
        help="Invert the brightness mapping",
        action="store_true",
    )
    # TODO: --colored

    args = parser.parse_args()
    image = Image.open(args.image_path)

    result = process_image(
        image=image,
        preferred_width=args.output_width,
        preferred_height=args.output_height,
        characters=args.characters,
        invert=args.invert,
    )

    print(result)


if __name__ == "__main__":
    main()
