from hf import generate_response
import io, streamlit as st
SYSTEM_PROMPT=""" you are a Math tutor.For every math  problem:
1) show step by step solution 2) explain reasoning  3) give an alternative solution if possible
4) verify the answer 5) use proper notation 6) divide complex problems into  parts
Format: problem-> steps-> **Final Answer**-> concepts used.Be percise and educational."""

def math_generate(problem:str,level:str,temperature:0.1,max_tokens=1024)
    prompt=f"{SYSTEM_PROMPT}\n\MathProblem({level}):
    {problem}"
    return generate_response(prompt,temperature=temperature,max_tokens=max_tokens)
def export_txt(history):
    txt= "\n\n".join([f"Q{i}: {h['q']}\nA{i}: {h['a']}" for i,h 
in enumerate(history,1)])
    return io.BytesIO(txt.encode('utf-8'))
def setup_ui():
    st.set_page_config(page_title="Math tutor" layout="centered")
    st.title("Math tutor")
    st.write("Solves any math problem step by step with explanations .")
with st.expander("Examples"):
    st.markdown