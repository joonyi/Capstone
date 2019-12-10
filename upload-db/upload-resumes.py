import requests
import json

URL = "http://localhost:8000"

'''
def edit_data(job_id):
    url = f"{URL}/api/resumes/{job_id}/"
    header = {'Authorization': f'Token {get_token()}'}
    data = {
        "job_id": "Koh",
    }
    response = requests.put(url, data=data, headers=header)
    print(response.text, response.status_code)


def delete_data(job_id):
    url = f"{URL}/api/resumes/{job_id}/"
    header = {'Authorization': f'Token {get_token()}'}
    response = requests.delete(url, headers=header)
    print(response.status_code)
'''


def get_token():
    # Get auth token
    url = f"{URL}/api/resumes/auth/"
    response = requests.post(url, data={'username': 'admin', 'password': '123'})
    return response.json()


def get_data():
    url = f"{URL}/api/resumes/"
    header = {'Authorization': f'Token {get_token()}'}
    response = requests.get(url, headers=header)
    print(response.json())


def create_new(data):
    url = f"{URL}/api/resumes/"
    header = {'Authorization': f'Token {get_token()}'}
    response = requests.post(url, data=data, headers=header)
    print(response.text)


if __name__ == "__main__":
    get_data()

    # Uncommed snippet below to upload new data
    # with open('data.json', 'r') as json_file:
    #     for line in json_file.readlines():
    #         data = json.loads(line)
    #         create_new(data)
    
