import random 
import request
import html
education_category_ID=9
api_url="https://opentdb.com/api.php?amount=10&category={EDUCATION_CATEGORY_ID}&type=multiple"
def get_education_qusion():
    response=request.get(api_url)
    if response.status_code==200:
        data=response.json()
    if data['esponse_code']== 0 and data['results']:
        return data['results']
    return None 
def run_quiz():
    questions=get_education_qusion()
    if not questions:
        print("failed to fetch")
        return
    score=0
    print("welcome to the quiz")
    for I, q enumerate(qusions,1):
    qusion=
