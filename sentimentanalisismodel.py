import requests
api_url="https://huggingface.co/settings/tokens"
headers={"Authoraization":"bearer place your api key here"}
text="I like food"
response=requests.post(api_url,headers=headers,json={"input ":text})
if response.status_code==200:
    result=response.json()
    print("sentiment:{with confidense code result[0['label']]}")
else:
    print("error found")