import PIL.Image, PIL.ImageOps
import argparse
from shutil import get_terminal_size


def grayify(image):
    return image.convert("L")


def pixels_to_characters(image, characters: str) -> str:
    return "".join(
        (characters[pixel * len(characters) // 256 ] for pixel in image.get_flattened_data())
    )


def invert_image(image):
    return PIL.ImageOps.invert(image)


def get_optimal_art_size(
    image,
    preferred_width: int | None = None,
    preferred_height: int | None = None,
) -> tuple[int, int]:
    """ """
    if preferred_width is not None and preferred_height is not None:
        return preferred_width, preferred_height

    image_ratio = image.width / image.height

    if preferred_width is not None:
        return preferred_width, int(preferred_width / image_ratio)

    if preferred_height is not None:
        return int(image_ratio * preferred_height) * 3, preferred_height

    terminal = get_terminal_size()
    terminal_ratio = terminal.columns / terminal.lines

    if image_ratio >= terminal_ratio:
        return terminal.columns, int(terminal.columns / image_ratio)
    else:
        return int(image_ratio * terminal.lines) * 3, terminal.lines


def process_image(
    image_path: str,
    preferred_width: int | None = None,
    preferred_height: int | None = None,
    characters: str = "@#S%?*+;:,. ",
    invert: bool = False,
):
    characters = characters or "@#S%?*+;:,. "
    image = PIL.Image.open(image_path)

    optimal_width, optimal_height = get_optimal_art_size(
        image=image,
        preferred_width=preferred_width,
        preferred_height=preferred_height,
    )

    image = image.resize((optimal_width, optimal_height))
    image = grayify(image)

    if invert:
        image = invert_image(image)

    image = pixels_to_characters(image, characters)

    return "\n".join(
        image[i : i + optimal_width]
        for i in range(0, len(image), optimal_width)
    )


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
        help="Character set for drawing, ordered from darkest to brightest.\nDefault: \" .:-=+*#%%@\"",
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
        "-i", "--invert", help="Invert the brightness mapping", action="store_true"
    )
    # TODO: --colored

    args = parser.parse_args()

    # print(args.characters)
    result = process_image(
        image_path=args.image_path,
        preferred_width=args.output_width,
        preferred_height=args.output_height,
        characters=args.characters,
        invert=args.invert,
    )

    print(result)


if __name__ == "__main__":
    main()
