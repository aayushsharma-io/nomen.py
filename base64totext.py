import base64

def base64_to_text(base64_string):
    """Decodes Base64 back to text."""
    decoded_bytes = base64.b64decode(base64_string)
    return decoded_bytes.decode('utf-8')
