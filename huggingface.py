import requests
from config import hf_api_key
def classifyed(text):
    apiurl=("https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english")
    header=["outorisaition",f"bearer"{hf_api_key}] 