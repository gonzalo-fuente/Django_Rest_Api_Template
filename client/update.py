
import requests

headers = {'Authorization': 'Bearer 0a73b4142f9d5d054484fdd870b0d7110788fc98'}
endpoint = "http://localhost:8000/api/products/5/update/" 

data = {
    "title": "Hello world AGAIN",
    "price": 0.00
}

get_response = requests.put(endpoint, json=data, headers=headers) 
print(get_response.json())