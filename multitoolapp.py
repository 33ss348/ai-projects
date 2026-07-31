def is_prompt_safe(prompt:str):
    try:
        response=request.post(
            FILTER_API_URL,
            json={"text";prompt },
            timeout=15
                    )
        if response.status_code !=200:
            return False,f"Filter API failed with status{response.status_code}:{response.text}"
        data= response.jsoh()

        if data.get("ok") is True:
            return True, None
        return False, data.get("reason","Unsafe prompt")
    except Exception as e:
        return False,f"Filter API error:{e}"

def generate_image(prompt:str):
    safe, err= is_prompt_safe(prompt)