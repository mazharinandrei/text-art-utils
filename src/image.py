from PIL import Image, ImageOps
from terminal import get_optimal_art_size, convert_pixels_to_characters


def grayify(image: Image):
    return image.convert("L")


def invert_image(image: Image):
    return ImageOps.invert(image)


def process_image(
    image: Image,
    preferred_width: int | None = None,
    preferred_height: int | None = None,
    characters: str = "@#S%?*+;:,. ",
    invert: bool = False,
):
    characters = characters or "@#S%?*+;:,. "

    optimal_width, optimal_height = get_optimal_art_size(
        image=image,
        preferred_width=preferred_width,
        preferred_height=preferred_height,
    )

    image = image.resize((optimal_width, optimal_height))
    image = grayify(image)

    if invert:
        image = invert_image(image)

    image = convert_pixels_to_characters(image, characters)

    return "\n".join(
        image[i : i + optimal_width]
        for i in range(0, len(image), optimal_width)
    )
