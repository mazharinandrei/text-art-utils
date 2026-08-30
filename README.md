## How to use

-  Generate ASCII/character art from an image

```sh
uv run -m src.cli.generate_image [-h] -p IMAGE_PATH [-c CHARACTERS] [-w OUTPUT_WIDTH] [-H OUTPUT_HEIGHT] [-i]
```

```
options:
  -h, --help            show this help message and exit
  -p, --image-path IMAGE_PATH
                        Path to the input image file (required)
  -c, --characters CHARACTERS
                        Character set for drawing, ordered from darkest to brightest. Default: " .:-=+*#%@"
  -w, --output-width OUTPUT_WIDTH
                        Width of the output text art in characters. Default: auto-calculated from image and terminal aspect ratio
  -H, --output-height OUTPUT_HEIGHT
                        Height of the output text art in characters. Default: auto-calculated from image and terminal aspect ratio
  -i, --invert          Invert the brightness mapping
```

- Generate ASCII/character animation from a video
```sh
uv -m src.cli.generate_animation [-h] -p VIDEO_PATH [-f FPS] [-l] [-c CHARACTERS] [-w OUTPUT_WIDTH] [-H OUTPUT_HEIGHT] [-i]
```

```
options:
  -h, --help            show this help message and exit
  -p, --video-path VIDEO_PATH
                        Path to the input video file (required)
  -f, --fps FPS         FPS of output animation
  -l, --loop            Loop video
  -c, --characters CHARACTERS
                        Character set for drawing, ordered from darkest to brightest. Default: " .:-=+*#%@"
  -w, --output-width OUTPUT_WIDTH
                        Width of the output animation in characters. Default: auto-calculated from video and terminal aspect ratio
  -H, --output-height OUTPUT_HEIGHT
                        Height of the output text animation in characters. Default: auto-calculated from video and terminal aspect ratio
  -i, --invert          Invert the brightness mapping
```
