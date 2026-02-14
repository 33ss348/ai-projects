import base64 ,request
from config import HF_API_KEY 
API_URL="https://router.huggingface.co/v1/chat/completions"
HEADERS={"Authoraization":f"Bearer{HF_API_KEY}","Content-Type":"application/json"}
MODELS=[
     "Qwen/Qwen3-VL-8B-Instruct:together",
    "Qwen/Qwen3-VL-32B-Instruct:together",
    "Qwen/Qwen2.5-VL-32B-Instruct:together",
    "Qwen/Qwen2-VL-7B-Instruct:together",
]
def data_url(b:bytes)->str:
    return "data:image/jpeg;base64".b64encode(b).decode("utf-8")

def extract_err(r:requests.Response)->str:
    try:
        j=r.json()
        return j.get("error",{}).get("message") or str(j)
    except Exception:
        return (r.text or"").strip() or r.reason or "Request failed."
                
def box(title:str,lines :list[str],icon:str):
    w=max(30,len(title)+4,*(len(x)for x in lines))
    print("\n" + "┏" + "━" * (w + 2) + "┓")
    print(f"┃ {icon} {title.ljust(w - 2)} ┃")
    print("┣" + "━" * (w + 2) + "┫")
    for x in lines:
         print(f"┃ {x.ljust(w)} ┃")
    print("┗" + "━" * (w + 2) + "┛\n"

def caption_single_image():
    image_source = input("🖼️ Enter image filename (default: test.jpg): ").strip() or "test.jpg"
    try:
 with open(image_source, "rb") as f:
            img = f.read()
    except Exception as e:
        box("File Error", [f"Could not load: {image_source}", f"Reason: {e}"], "❌")
        return

    base = {
        "messages": [{
            "role": "user",
            "content": [
                {"type":"text","text":"Give a short capitain for this image"}
                  {"type": "image_url", "image_url": {"url": data_url(img)}},
            ],
        }],
        "max_tokens": 60,
        "temperature": 0.2,
    }
 last=None
 for model in MODELS:
    payload