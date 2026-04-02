# import requests
# from requests import delete

#  get
# response=requests.get("https://petstore.swagger.io/v2/store/inventory")

# response=requests.get("https://petstore.swagger.io/v2/pet/findByStatus?status=sold")

# print(response.text)
# print(response.status_code)
# print(response.json())


# fetch the value of Busy
# r= response.json()
# print(r["Busy"])

# expected=201
# assert expected==response.status_code , f"not equal to {response.status_code}"


# post
# payload={
#   "id": 110,
#   "category": {
#     "id": 10,
#     "name": "string"
#   },
#   "name": "doggie",
#   "photoUrls": [
#     "string"
#   ],
#   "tags": [
#     {
#       "id": 0,
#       "name": "string"
#     }
#   ],
#   "status": "available"
# }
# response1=requests.post("https://petstore.swagger.io/v2/pet",json=payload)
# assert 200 == response1.status_code , f"not equal {response1.status_code}"
# print(response1.json())

# delete()

# response=requests.delete("https://petstore.swagger.io/v2/pet/10")
# assert 200 == response.status_code , f"not equal to {response.status_code}"
# print(response.text)


# all three in function

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
