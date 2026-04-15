import numpy as np

def grayscale(img):
    # Weighted average (matrix math)
    weights = np.array([0.299, 0.587, 0.114])
    gray = np.dot(img, weights)

    # Convert back to 3-channel RGB
    return np.stack([gray, gray, gray], axis=-1)
