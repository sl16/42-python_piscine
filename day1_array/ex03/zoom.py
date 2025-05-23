import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from PIL import Image
from load_image import ft_load

matplotlib.use('TkAgg')  # To enable plt.show() to open windows on WSL2


def zoom(path: str, size: int) -> np.ndarray:
    """
    Loads an image, zooms in on the middle [SIZE] pixels area,
    prints the resulting format, its pixels content in RGB format,
    and finally plots the image on a scale. Opens the image also.

    Handles JPG and JPEG.
    """

    try:
        # Open the image with the 'with' keyword so it closes automatically
        with Image.open(path) as img:
            assert img is not None, ("Cannot load image")
            assert img.format in ("JPG", "JPEG"), ("Provide JPG or JPEG only")
            assert size > 0, ("The zoom area must be bigger than 0")
            assert size <= img.width and size <= img.height, (
                "The zoom area cannot be bigger than the image provided"
                )

            # Calculate the zoom area (zoom in the middle)
            crop_area = (img.width // 2 - size // 2,
                         img.height // 2 - size // 2,
                         img.width // 2 + size // 2,
                         img.height // 2 + size // 2)

            # Crop and convert the image to grayscale
            zoomed_img = img.crop(crop_area)
            zoomed_img = zoomed_img.convert("L")

            # Add a scale to the image
            img_array = np.array(zoomed_img)
            plt.imshow(img_array, cmap="gray")
            plt.show()

            print(f"New shape after slicing: "
                  f"({zoomed_img.height}, {zoomed_img.width}, "
                  f"{len(zoomed_img.mode)})")
            return (np.array(zoomed_img))

    except Exception as e:
        print(f"Error: {e}")
        return []


def main():
    print(ft_load("animal.jpeg"))
    print(zoom("animal.jpeg", 400))


if __name__ == "__main__":
    main()
