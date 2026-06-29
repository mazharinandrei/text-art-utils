from time import sleep
from main import process_image
from characters import STYLE_2


def print_animation() -> None:
    files = (f"./alien_frames/output_{str(i).rjust(4, "0")}.png" for i in range(1, 242))
    for file_name in files:
        frame = process_image(
                image_path=file_name,
                characters=STYLE_2,
                invert=True)
        print(frame)
        sleep(1/30)

while True:
    print_animation()
