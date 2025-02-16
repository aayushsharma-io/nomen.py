import base64

def text_to_base64(text):
    """Encodes text to Base64."""
    encoded_bytes = base64.b64encode(text.encode('utf-8'))
    return encoded_bytes.decode('utf-8')
