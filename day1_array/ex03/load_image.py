import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:

    """
    Loads an image, prints its format, and its pixels
    content in RGB format.

    Handles JPG and JPEG.
    """
    try:
        with Image.open(path) as img:
            assert img is not None, ("Cannot load image")
            assert img.format in ("JPG", "JPEG"), ("Provide JPG or JPEG only")

            print(f"The shape of the {img.format} image is: "
                  f"({img.height}, {img.width}, {len(img.mode)})")
            return (np.array(img))

    except Exception as e:
        print(f"Error: {e}")
        return []


def main():
    pass


if __name__ == "__main__":
    main()
