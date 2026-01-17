import image
import from daytime to daytime
from PIL import image
from config import hf_api_key
client=Inference_Clients(apikey=HF_API_KEY)
print(f"primery model")
print("type exit to quit")
while True:
   prompt=input("enter prompt")
   if prompt.lower()=="quit":
      break
   if not prompt:
      continue
print("generating images")
image=None
for model in MODELS:
   try:
      image=client.text to image