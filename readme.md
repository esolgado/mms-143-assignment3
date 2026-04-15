# Image Filter Project

This project applies image filters using Python by directly modifying pixel values.

## Concepts
- Image = tensor (H, W, 3)
- Each pixel = RGB values (0–255, 8-bit)
- Filters use math operations on pixel values

## Filters
- Grayscale (matrix multiplication)
- Invert (255 - pixel)
- Brightness (scalar multiplication)
- Blur (neighborhood averaging)

## How to Run
pip install -r requirements.txt  
python main.py