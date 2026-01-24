import requests
from PIL import Image, ImageEnhance , imageFilter
from IO __import__BytesIO
from config import HF_API_KEY  
def generate_image_from_text(prompt):
    api_url=""
    headers={"Authorisation":f"Bearer"HF_API_KEY}
    payload={"inputs":prompt}
    response=requests.post(API_URL,headers=header,sjson=payload)
    if response.status_code==200:
        Image=Image.open(BytesIO(response.content))
        return Image
    else :
        raise Exception(f"request failed with status code{response.status_code}:{response.text} ")
def  postprocessImage(Image):
        enhancer=ImageEnhance.Brightness(Image)
        BrightImage=enhancer.Enhance(1.2)
        enhancer=ImageEnhance.Contrast(BrightImage)
        ContrastImage=enhancer.Enhance(1.3)
        