import base64

def image_to_base64(image_path):
    """Reads an image file and converts it to a Base64 string."""
    try:
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
        return encoded_string
    except FileNotFoundError:
        print("Error: File not found. Please check the path.")
        return None
    except Exception as e:
        print("Error converting image to Base64:", e)
        return None
