from PIL import Image
from shutil import get_terminal_size


def convert_pixels_to_characters(image: Image, characters: str) -> str:
    return "".join(
        (
            characters[pixel * len(characters) // 256]
            for pixel in image.get_flattened_data()
        )
    )


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
