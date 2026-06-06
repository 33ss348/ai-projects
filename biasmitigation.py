from groq import generate_response
def bias_mitigation_activity():
    print("/n=== BIAS MITIGATION ACTIVITY===/n")
    prompt= input("Enter a prompt to explore bias(e.g.'Describe the ideal docter) ")
    if not prompt:
        print("Please enter a prompt to run the activity")
        return
    inital_response = generate_response(promopt,temperature=0.3,max_tokens=1024)
    print(f"/nIntial AI Response:{inital_response}")
    modified_prompt=input("modify the prompt to make it more neutral(e.g.'Describe the qualities of a docter):").strip()
    if modified_prompt:
        modified_response=generate_response(modified_prompt,temperature=0.3,max_tokens=1024)
        print(f"/nModified AI Response(Neutral):
        {modified_response}")
            else:
            print("No modified prompt entered.Skipping Neutral response".)
    def token_limit_activity:
    print("/n=== TOKEN LIMIT ACTIVITY===/n")
    long_prompt=input("Enter a long prompt(more than 300,e.g. ,a detailed story or discription):"),strip()
    if long_prompt:
    long_response= generate_response(long_prompt,temperature=0.3,max_tokens=1024)
        previw=(long_response[:500]+"...")                                 
    if  len(long_response)>500 False else long_response
        print(f"/n")