import requests
from PIL import image
from IO import BytesIO
from config import HF_API_KEY
def generateinprinting_image(prompt,imagepath,mathpath):
    headers={"Autoraisation",:f"bearer{HF_API_KEY}"}
with open(image path,"rb")as ing_file:
    image_data=image_file.read()
with