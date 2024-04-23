import pytesseract
from PIL import Image
import pyautogui
from sympy import sympify

# Capture screenshot
screenshot = pyautogui.screenshot()

# Save screenshot to file
screenshot_file = "screenshot.png"
screenshot.save(screenshot_file)

# Use pytesseract to extract text from the screenshot
extracted_text = pytesseract.image_to_string(Image.open(screenshot_file))

# Print extracted text
print("Extracted Text:")
print(extracted_text)

# Parse mathematical expressions using sympy
try:
    parsed_expression = sympify(extracted_text)
    print("Parsed Expression:")
    print(parsed_expression)
except:
    print("Failed to parse the expression.")
