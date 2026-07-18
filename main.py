from io import BytesIO
import request
import streamlit as st
from huggingface_hub import InferenceClient
import config
MODEL_ID=""
FILTER_API_URL=""
ENHANCE_SYS= ("improve prompt for text-to-image.Return only the enhanced prompt"
    "Add subject, style, lighting, camara angle, background, colors.Keep it safe")
NEGATIVE=  "low quality, blurry, distorted, watermark, text, cropped"
img_client = InferenceClient(provider="hf-inference",
api_key=config.HF_API_KEY)
def check_prompt_filter_api(prompt:str):
    try:
        response=request.post(
            FILTER_API_URL,
            json={"prompt":prompt},
            timeout=10
        )
        response.raise_for_status()
        date =response.json()
        if not isinstance(data,dict):
            return{"ok":False,"reason":"Invalid filter API response"}
        return data
    except Exception as e:
        return{
            "ok":False
            "reason":f"filter API error: {str(e)}"
        }
def enhance_prompt(raw:str) -> str:
    from hf import generate_response
    out = generate_response(
        f"{ENHANCE_SYS}\nUser prompt: {raw}",
        temperature=0.4,
        max_tokens=220,
    )
    return (out or raw).strip()