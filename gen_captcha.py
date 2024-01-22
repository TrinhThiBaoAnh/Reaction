# Importing the required libraries
from captcha.image import ImageCaptcha
import random
import string
import os
# Specify dimensions for the captcha image
image = ImageCaptcha(width=200, height=50)
file = open("label.txt", "w", encoding="utf-8") 
# Generate a random string for the captcha
captcha_length = 6  # You can adjust the length of the random string
num_of_gen = 1
while num_of_gen <= 2000:
    captcha_text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=captcha_length))

    # Print the generated captcha text
    # print("Generated captcha text:", captcha_text)

    # Generate the text-based captcha image
    data = image.generate(captcha_text)

    # Save the captcha image file with the filename as the generated text
    img_path = os.path.join("captcha_dataset/",  str(num_of_gen) + ".png")
    # Save the captcha image file
    image.write(captcha_text, img_path)
    file.write(img_path +"\t" + captcha_text + "\n")
    num_of_gen += 1