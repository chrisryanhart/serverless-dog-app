import json
import requests


def lambda_handler(event, context):
    
    baseDogUrl = 'https://api.thedogapi.com/v1/breeds/1'
    headers = {"Content-Type": "application/json"}

    response = requests.get(baseDogUrl, headers=headers)
    
    data = response.json()

    print(data['name'])

    
    return data