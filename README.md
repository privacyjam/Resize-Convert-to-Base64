# Resize & Convert to Base64

A simple Python script that resizes an image to a specified size and outputs it as a Base64-encoded PNG.

I needed to have small image logos on my website and wanted to use Base64, and needed an easy way to resize the images then print out the base64 string

## Requirements

- Python 3.x
- [Pillow](https://pypi.org/project/Pillow/) (Install using `pip install Pillow` or `sudo apt install python3-pillow)

## Usage

1. Download resize-to-base64.py
2. Run it with
```bash
python3 resize-to-base64.py
```
3. Input a path, enter, and a size, enter, and it will output the data string

# Example
```bash
python3 /home/pie/Documents/code/test.py
Enter the path to your high-resolution image: /home/pi/Downloads/1.png
Enter the desired size (width,height), e.g. 20,20: 5,5

Here is your resized image in Base64:

data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAA/cutofftherest
```

