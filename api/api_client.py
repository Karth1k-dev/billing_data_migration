import requests

# mock api endpoint
API_URL = "https://jsonplaceholder.typicode.com/posts"

def send_to_api(data):

    responses = []

    for record in data:

        # send POST request
        response = requests.post(API_URL, json=record)

        # store response status
        responses.append(response.status_code)

    return responses

"""
What happens here

For each customer:

Python script
     ↓
POST request
     ↓
API server

Example request sent:

POST /api/customer

{
"name":"John",
"plan":"Basic"
}
status_code
201

means

Data successfully created
"""

