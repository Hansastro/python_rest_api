import base64
import os

def encode_image_base64(image_file):
    mime_dict = {
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.png': 'image/png'
    }
    with open(image_file, "rb") as img_file:
        filename = os.path.split(image_file)
        _, file_extension = os.path.splitext(filename[1])
        print(file_extension)
        return {'image_type': mime_dict.get(file_extension), 'image_data': base64.b64encode(img_file.read()).decode('utf-8')}

