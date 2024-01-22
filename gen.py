import random
import string
from pathlib import Path
from captcha.image import ImageCaptcha
import os
# with open("quan_diem_xau_doc_text.txt", "r", encoding="utf-8") as file:
#     file_content = file.readlines()

# vietnamese_words = [text.replace("\n", "") for text in file_content]
# vietnamese_words = [ text  for text in vietnamese_words if text != ""]
# # print(vietnamese_words)

# file = open("label.txt", "w", encoding="utf-8") 

# num_of_images = 1
# while num_of_images <= 200:
#         # # Chọn ngẫu nhiên một từ từ danh sách
#     captcha_text = random.choice(vietnamese_words)
#     draw_text = captcha_text.split(" ")
#     for text in draw_text:
#             # Specify dimensions
#         image = ImageCaptcha(width=200, height=50)

#         # Generate the text-based captcha
#         data = image.generate(text)
#         img_path = os.path.join("vietnamese_data/",  str(num_of_images) + ".png")
#         # Save the captcha image file
#         image.write(text, img_path)
#         file.write(img_path +"\t" + text + "\n")
#         num_of_images += 1
    
# file = open("label.txt", "r", encoding="utf-8")
# file_content = file.readlines()
# label = [file.replace("\n","").split("\t")[-1] for file in file_content]
# print(label)
data_dir = Path("sensitive")
# images = sorted(list(map(str, list(data_dir.glob("*.png")))))

tmp = open("label_sen.txt", "r", encoding="utf-8")
file_content = tmp.readlines()
print(file_content)
labels = [item.replace("\n","").split("\t")[1].lower()  for item in file_content]
images = [item.replace("\n","").split("\t")[0].split("/")[1].lower()  for item in file_content]
print(len(labels))
print(len(images))
print(len(os.listdir("sensitive")))