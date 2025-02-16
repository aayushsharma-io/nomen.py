from texttobase64 import text_to_base64
from base64totext import base64_to_text
from imagetobase64 import image_to_base64
from base64toimage import base64_to_image

def main():
    ascii_art = r"""
 ________   ________  _____ ______   _______   ________      
|\   ___  \|\   __  \|\   _ \  _   \|\  ___ \ |\   ___  \    
\ \  \\ \  \ \  \|\  \ \  \\\__\ \  \ \   __/|\ \  \\ \  \   
 \ \  \\ \  \ \  \\\  \ \  \\|__| \  \ \  \_|/_\ \  \\ \  \  
  \ \  \\ \  \ \  \\\  \ \  \    \ \  \ \  \_|\ \ \  \\ \  \ 
   \ \__\\ \__\ \_______\ \__\    \ \__\ \_______\ \__\\ \__\
    \|__| \|__|\|_______|\|__|     \|__|\|_______|\|__| \|__|
                                                             
"""
    print(ascii_art)
    print("Welcome to NOMEN - Text & Image ↔ Base64 Converter")
    
    while True:
        print("\nChoose an option:")
        print("1. Convert Text to Base64")
        print("2. Convert Base64 to Text")
        print("3. Convert Image to Base64")
        print("4. Convert Base64 to Image")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ").strip()

        if choice == '1':
            text = input("Enter the text to convert: ")
            print("Base64 Encoded:", text_to_base64(text))
        
        elif choice == '2':
            base64_str = input("Enter the Base64 string to decode: ")
            try:
                print("Decoded Text:", base64_to_text(base64_str))
            except Exception:
                print("Invalid Base64 input. Please try again.")

        elif choice == '3':
            image_path = input("Enter the image file path (e.g., image.jpg): ").strip()
            base64_string = image_to_base64(image_path)
            if base64_string:
                with open("image_base64.txt", "w") as file:
                    file.write(base64_string)
                print("Image successfully converted to Base64!")
                print("Saved as 'image_base64.txt'.")

        elif choice == '4':
            base64_file = input("Enter the Base64 file path (e.g., image_base64.txt): ").strip()
            try:
                with open(base64_file, "r") as file:
                    base64_str = file.read()
                output_path = input("Enter the output file name (e.g., output.jpg): ").strip()
                base64_to_image(base64_str, output_path)
            except FileNotFoundError:
                print("Error: Base64 file not found.")

        elif choice == '5':
            print("Exiting NOMEN. Goodbye!")
            break

        else:
            print("Invalid choice, please enter 1, 2, 3, 4, or 5.")

if __name__ == "__main__":
    main()
