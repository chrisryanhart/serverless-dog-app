import json
import requests
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os
import boto3
from botocore.exceptions import ClientError


def get_secret():

    secret_name = "firestore/dog-database"
    region_name = "eu-north-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    # Decrypts secret using the associated KMS key.
    secret = get_secret_value_response['SecretString']

    return secret

database_key = get_secret()

# if that doesn't work, manually serialize the data
# ensure it's in json format
database_key = os.environ[database_key]

# Initialize Firebase app
cred = credentials.Certificate(database_key)
firebase_admin.initialize_app(cred)

# Access the Firestore database
db = firestore.client()


# now call the db inside the func

def lambda_handler(event, context):
    
    baseDogUrl = 'https://api.thedogapi.com/v1/breeds/1'
    headers = {"Content-Type": "application/json"}

    response = requests.get(baseDogUrl, headers=headers)
    
    data = response.json()

    # store in firestore

    db.collections('dogs').document(1).set({"name": data["name"]})

    allDogs = db.collections('dogs').get()

    result = allDogs[0].to_dict()

    print(result)

    
    return result