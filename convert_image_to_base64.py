import json
from Rest_app.utils.base64_image import encode_image_base64

image_file = '/home/jean-phi/data/Projects/GardenWeb/gardenweb/static/images/logo.png'
output_file = './image_data.json'

img_data = encode_image_base64(image_file)

with open(output_file, "w") as json_file:
    print('write json file')
    json.dump(img_data, json_file)