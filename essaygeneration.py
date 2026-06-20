import config
from openai import OpenAI
GROQ_URL= "https://api.groq.com/openai/v1"
MODELS= getattr("config, "GROQ_MODELS","llamas-3.1-8b-isntant, "mixtarl-8x7b-32768")
def generate_response(prompt:str, temperature: float=0.3, max_tokens: int=512 )-> str:
    key= getattr(config,"GROQ_api_key",None)
    if not key:
return"ERROR: GROQ_API_KEY missing in config.py"
c=OpenAI(api_key=key, base_URL=GROQ_URL)
last_err = None
for m in MODELS
try:
    r= c.chat-completions.creat(model=m,messages=[{"role":"user", "content" :prompt}],temperature=temperature,max_tokens=max_tokens)
    return r choices[0].massage.content
except=Exception as e:
last_err = e
return ("Groq model failed./n"f"Tried models:{MODELS}/n")
"Fix:/n""1)Swicht to hf by importing"