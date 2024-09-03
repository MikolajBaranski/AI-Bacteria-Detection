import json
from PIL import Image
import os

def get_image_size(image_path):
    """
    Returns width and height of png or jpeg image

    Parameter:
    - path to image in png or jpeg format
    """
    with Image.open(image_path) as img:
        # Get image format (JPEG, PNG, etc.)
        image_format = img.format

        # Extract image size based on format
        if image_format == "JPEG":
            return img.width, img.height
        elif image_format == "PNG":
            # PNG format stores the width and height in the image info dictionary
            image_info = img.info
            if "png_ihdr" in image_info:
                width = image_info["png_ihdr"][0]  # Width is stored at index 0
                height = image_info["png_ihdr"][3]  # Height is stored at index 3
                return width, height
        else:
            raise ValueError("Unsupported image format")

def convert_to_yolo_format(json_path, image_width, image_height, option=None):
    """
    Convert JSON into txt in YOLO label format

    Parameter:
    - json_path -> path to JSON holding the labels
    - image_path -> path to image in png or jpeg format
    """
    # Open JSON and get data
    with open(json_path, "r") as f:
        data = json.load(f)
    
    lines = []
    for label in data["labels"]:

        # Calculate normalized coordinates
        x_center = (label["x"] + label["width"] / 2) / image_width
        y_center = (label["y"] + label["height"] / 2) / image_height
        width = label["width"] / image_width
        height = label["height"] / image_height
        
        # Add line to YOLO format
        line = f"{0} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}\n"
        lines.append(line)

    return lines