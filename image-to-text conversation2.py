import requests
import base64
from config import HF_API_KEY

PROPER_URL = "https://router.huggingface.co/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {HF_API_KEY}",
    "Content-Type": "application/json"
}

VISION_MODELS = [
    "Qwen/Qwen3-VL-8B-Instruct:together",
    "Qwen/Qwen2.5-VL-7B-Instruct:together",
]

TEXT_MODELS = [
    "Qwen/Qwen2.5-7B-Instruct:together",
    "mistralai/Mistral-7B-Instruct-v0.3:together",
]


# Convert image to base64 data URL
def image_to_data_url(path: str):
    with open(path, "rb") as f:
        image_bytes = f.read()
        encoded = base64.b64encode(image_bytes).decode("utf-8")
        return f"data:image/jpeg;base64,{encoded}"


# Query Hugging Face API
def query_hf_api(model: str, messages: list):
    payload = {
        "model": model,
        "messages": messages,
        "max_tokens": 500
    }

    response = requests.post(PROPER_URL, headers=HEADERS, json=payload)

    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code)
        print(response.text)
        return None


# Example usage
if __name__ == "__main__":
    messages = [
        {"role": "user", "content": "Explain how AI works in simple terms."}
    ]

    result = query_hf_api(TEXT_MODELS[0], messages)
    print(result)