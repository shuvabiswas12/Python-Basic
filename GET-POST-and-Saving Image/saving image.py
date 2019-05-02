import requests
from PIL import Image
from io import BytesIO

r = requests.get("http://s1.1zoom.me/b5660/164/Thailand_Parks_Tropics_511622_1600x900.jpg")

print("status code: ", r.status_code)

image = Image.open(BytesIO(r.content))

path = "./image."+image.format

print(image.size, image.format, image.mode)

try:
    image.save(path, image.format)
except:
    print("can't save image")

