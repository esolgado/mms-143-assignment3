import numpy as np
from PIL import Image

def load_image(path):
    img = Image.open(path).convert("RGB")
    return np.array(img, dtype=np.float64)


def save_image(img_array, path):
    img_array = np.clip(img_array, 0, 255)
    img_array = img_array.astype(np.uint8)

    img = Image.fromarray(img_array)
    img.save(path)