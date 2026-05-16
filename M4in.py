from groq import generate_response
def reinforcement_learning_activity
print("/n=== REINFORCEMENT LEARNIG ACTIVITY ===/n")
prompt = input("Enter a prompt for AI model(e.g 'Describe the Lion'):").strip()
if not prompt:
    print("Please enter a prompt to run the activity.")
    return
initial_response=generate_response(prompt,temperature=0.3,max_tokens=1024)
print("/n=== Initial AI response{Initial AI response}")
try:
    rating = int(input("Rate the response form 1(bad) to 5(good):").strip())
    if rating < 1 or rating >5:
       print("invalid rating using 3.")
       rating = 3
except ValueError :
    print("Invalid rating using 3.")
    rating=3
    feedback=input("Provide feed back for improvement:").strip()
    improved_response = f"{initial_response}"("Improved with your feedback:{feedback}")
    print(f"/nImproved AI Response: {Improved_Response}")
    print("/nReflection":)
    print("1.How did the model's response improve with feedback?")
    print("2.How does reinforcement help AI to improve its performence over time?")
def role_based_prompt_activity():
    print("/===ROLE BASED PROMPTS ACTIVITY===/n")
    category=input("Enter a category(e.g,science,history,math):").strip()
    item= input(f"Enter a specific{category}")