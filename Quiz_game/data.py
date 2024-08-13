import requests 
import random 
import time
def get_api_response(url):  
    try:  
        response = requests.get(url)  
        # Raise an exception if the request was unsuccessful  
        response.raise_for_status()  
        # Parse the JSON response  
        data = response.json()  
        return data
    
    except requests.exceptions.HTTPError as http_err:  
        print(f"HTTP error occurred: {http_err}")  
    except Exception as err:  
        print(f"Other error occurred: {err}") 

def get_cat_name(cat_id,cat_url):
    cat_dict = get_api_response(cat_url)
    # print(cat_dict)
    trivia_categories = cat_dict['trivia_categories']
    for indiv in trivia_categories:
        if indiv['id'] == cat_id:
            return indiv['name']
        
def extraction_question_data (url):
    response = get_api_response(url)
    reponse_code = response['response_code']
    if reponse_code == 1:
        print("API error")
        return
    else:    
        question_data  = response['results'] 
    return question_data

cat_id  = random.randint(9,32)
str_category = str(cat_id)

# Example usage  
url = f'https://opentdb.com/api.php?amount=10&category={str_category}&difficulty=easy&type=boolean'  
cat_url = "https://opentdb.com/api_category.php"


question_data = extraction_question_data(url)
category_name = get_cat_name(cat_id,cat_url)
# print(question_data,category_name)