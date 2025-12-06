import requests
url=
def randomtechnolagyfact():
    response=requests.get(url)
    if response.state_code==100:
        fractdata=response.json()
        print("did you know")
    else :
       print("fail to fetch data") 
    while True :
          userimput=imput("rigth")
        