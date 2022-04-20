import requests
import json

URL = "http://localhost:8000"


def get_token():
    # Get auth token
    url = f"{URL}/api/stages/auth/"
    response = requests.post(url, data={'username': 'admin', 'password': '123'})
    return response.json()


def get_data():
    url = f"{URL}/api/stages/"
    header = {'Authorization': f'Token {get_token()}'}
    response = requests.get(url, headers=header)
    print(response.json())


def create_new(data):
    url = f"{URL}/api/stages/"
    header = {'Authorization': f'Token {get_token()}'}
    response = requests.post(url, data=data, headers=header)
    print(response.text)


if __name__ == "__main__":
    get_data()  # read data

    # Uncommed snippet below to upload new data
    # with open('date_data.json', 'r') as json_file:
    #     for line in json_file.readlines():
    #         data = json.loads(line)
    #         create_new(data)
    
