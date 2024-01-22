from PIL import Image, ImageDraw, ImageFont
import random
import string
import os

def random_crop(image, crop_size=(200, 50)):
    img_width, img_height = image.size
    crop_width, crop_height = crop_size

    # Generate random coordinates for the top-left corner
    left = random.randint(0, img_width - crop_width)
    top = random.randint(0, img_height - crop_height)

    # Calculate the coordinates for the bottom-right corner
    right = left + crop_width
    bottom = top + crop_height

    # Crop the image
    cropped_image = image.crop((left, top, right, bottom))

    return cropped_image

# Example usage:
image_path = "images/pexels-anni-roenkae-2832432.jpg"
original_image = Image.open(image_path)

#
# Kích thước ảnh
img_width = 200
img_height = 50

# Thư mục lưu ảnh
output_folder = "sensitive2"

# Tạo thư mục nếu chưa tồn tại
os.makedirs(output_folder, exist_ok=True)

# Font tiếng Việt
font_path = "arial/arial.ttf"  # Thay đổi đường dẫn đến font tiếng Việt


# Đọc danh sách từ file
with open("quan_diem_xau_doc_text.txt", "r", encoding="utf-8") as file:
    vietnamese_words = [line.strip() for line in file if line.strip()]

# Số lượng ảnh muốn tạo
num_images = 120000
i =  120001
file = open("label_sen2.txt", "a", encoding="utf-8") 
while i <= num_images:
    # Tạo ảnh trắng với màu nền ngẫu nhiên
    

    # Chọn một từ ngẫu nhiên
    random_text = random.choice(vietnamese_words)
    texts = random_text.split(" ")
    for text in texts:
        i = i +1 
        bg_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        # image = Image.new("RGB", (img_width, img_height), color=bg_color)
        image = random_crop(original_image)
        draw = ImageDraw.Draw(image)
        # Lấy kích thước của chữ để điều chỉnh vị trí trung tâm
        font_size = random.randint(30, 50)
        font = ImageFont.truetype(font_path, font_size)
        text_width, text_height = draw.textsize(text, font)

        # Tính toán vị trí trung tâm để chữ vừa với ảnh
        text_x = (img_width - text_width) // 2
        text_y = (img_height - text_height) // 2

        # Màu chữ ngẫu nhiên
        text_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        # Viết chữ lên ảnh
        draw.text((text_x, text_y), text, font=font, fill=text_color)

        # Lưu ảnh vào thư mục
        image_path = os.path.join(output_folder, f"sen_{i}.png")
        image.save(image_path)
        file.write(image_path +"\t" + text + "\n")           

# Hiển thị xong, đóng ảnh
image.show()
print(i)
