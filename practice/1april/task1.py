import requests
payload = {
    "id": 111110,
    "category": {
        "id": 110,
        "name": "string"
    },
    "name": "doggie",
    "photoUrls": ["string"],
    "tags": [
        {
            "id": 0,
            "name": "string"
        }
    ],
    "status": "available"
}
pet_id = None

def post_data():
    global pet_id
    res = requests.post("https://petstore.swagger.io/v2/pet", json=payload)
    print(res.status_code)
    pet_id = res.json()['id']

def get_data():
    res = requests.get(f"https://petstore.swagger.io/v2/pet/{pet_id}")
    print(res.json())
    print(res.status_code)

def delete_data():
    res = requests.delete(f"https://petstore.swagger.io/v2/pet/{pet_id}")
    print(res.status_code)

post_data()
get_data()
delete_data()
