from filters.grayscale import grayscale
from filters.invert import invert
from filters.brightness import brightness
from utils.io import load_image, save_image


def main():
    img = load_image("images/input.jpg")

    print("Image shape:", img.shape)
    print("Sample pixel:", img[0, 0])

    gray_img = grayscale(img)
    invert_img = invert(img)
    bright_img = brightness(img, 1.3)

    save_image(gray_img, "images/output_gray.jpg")
    save_image(invert_img, "images/output_invert.jpg")
    save_image(bright_img, "images/output_bright.jpg")

    print("Done! Images saved.")


if __name__ == "__main__":
    main()
