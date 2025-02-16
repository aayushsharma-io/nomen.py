import base64
import os

def base64_to_image(base64_string, output_path):
    """Decodes a Base64 string back to an image and saves it."""
    try:
        image_data = base64.b64decode(base64_string)
        with open(output_path, "wb") as image_file:
            image_file.write(image_data)
        print(f"Image saved successfully: {output_path}")
    except Exception as e:
        print("Error saving image:", e)
