from PIL import Image
from gtts import gTTS
from pytesseract import image_to_string
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def image_to_sound(path_to_image):
  
    try:
        loaded_image = Image.open(path_to_image)
        decoded_text = image_to_string(loaded_image)

        # extracted text
        cleaned_text = " ".join(decoded_text.split("\n")).strip()

        if not cleaned_text:
            print("No text detected in the image.")
            return False

        print(f"Extracted Text: {cleaned_text}")

        sound = gTTS(cleaned_text, lang="en")
        sound.save("sound.mp3")
        return True

    except Exception as bug:
        print("Error while executing the code:", bug)
        return False


if __name__ == "__main__":
    image_path = "R.jpeg"

    try:
        with open(image_path, 'rb') as f:
            pass
    except FileNotFoundError:
        print(f"The image '{image_path}' was not found.")
    else:
        success = image_to_sound(image_path)
        if success:
            print("Conversion successful!")
        else:
            print("Conversion failed!")