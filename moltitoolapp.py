def export_txt(history):
    txt= "".join([f"Q{i}: {h['question']}\nA{i}: {h['answer']}\n\n"for i,h in enumerate(history, 1)])
    bio= io.BytesIO(txt.encode("utf-8")); bio.seek(0); return
bio 
def teaching_answer(q : str)-> str:
    return generate_response(q,temperature=0.3, max_tokens=1024)

def math_answer(q:str, level: str)-> str:
    prompt = f"{MATH_SYSTEM}\n\nDifficulty: {level}\nMath Problem: q"
    return generate_response(prompt, temperature=0.1 , max_tokens=1024)
def run_ai_teaching_assistant():
        st.title("🤖AI Teaching Assistant")
        st.session_state.setdefault("history_ata",[])
        cl, c2 = st.columns([1,2])
        if cl.button("🏏clear", key="c_data"):
st.session_state.history_ata:
c2.download_button("💾Export, export_txt(st.session_state.history_ata),")
"AI_Teaching_Assistant_Conversation.txt, text\plain"
q= st.text_input("Enter your question:", key=)