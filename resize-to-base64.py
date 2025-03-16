#!/usr/bin/env python3

import base64
from io import BytesIO

try:
    from PIL import Image
except ImportError:
    print("Pillow not found. Install it: pip install Pillow")
    exit(1)

def resize_and_convert_to_base64(image_path, size=(20, 20)):
    with Image.open(image_path) as img:
        img = img.convert("RGBA")
        img = img.resize(size, Image.LANCZOS)
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        return base64.b64encode(buffer.getvalue()).decode("utf-8")

def main():
    image_path = input("Enter image path: ").strip()
    if not image_path:
        print("No image provided.")
        return

    size_str = input("Enter size (width,height), e.g. 20,20: ").strip()
    try:
        width, height = map(int, size_str.split(","))
    except ValueError:
        print("Invalid size. Using default 20x20.")
        width, height = 20, 20

    try:
        b64_str = resize_and_convert_to_base64(image_path, (width, height))
    except FileNotFoundError:
        print(f"File not found: {image_path}")
        return
    except Exception as e:
        print(f"Error processing image: {e}")
        return

    data_uri = f"data:image/png;base64,{b64_str}"
    print("\nResized image in Base64:")
    print(data_uri)

if __name__ == "__main__":
    main()
