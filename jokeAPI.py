import requests
url="https://official-joke-api.appspot.com/random_joke"
response=requests.get(url)
if response.status_code==200:
    print(f"full json response:{response.json()}")
    jokedata=response.json()
    return {fjokedata['setup']}-{jokedata['punchline']}
else:
    return"pay to retribeut"