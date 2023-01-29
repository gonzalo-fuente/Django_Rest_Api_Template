import requests

headers = {'Authorization': 'Bearer 0a73b4142f9d5d054484fdd870b0d7110788fc98'}
endpoint = "http://localhost:8000/api/products/" 

data = {
    "title": "This is the title",
    "price": 2.99
}
get_response = requests.post(endpoint, json=data, headers=headers) 
print(get_response.json())