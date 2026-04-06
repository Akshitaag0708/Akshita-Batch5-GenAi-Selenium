import requests

# payload = {
#   "city": "Jaipur",
#   "country": "India",
#   "email": "akshitaag0708@gmail.com",
#   "firstName": "Akshita",
#   "gender": "FEMALE",
#   "lastName": "Agarwal",
#   "password": "1234567",
#   "phone": 7852849078,
#   "state": "Rajasthan",
#   "zoneId": "ALPHA"
# }
#
#
# res=requests.post("https://www.shoppersstack.com/shopping/shoppers",json=payload , verify=False)
# here verify=False → ignores SSL certificate issue

# assert 409 == res.status_code , f"not equal {res.status_code}"
# print(res.json())

user_id=None
token=None
payload2={
  "email": "akshitaag0708@gmail.com",
  "password": "1234567",
  "role": "SHOPPER"
}

res2=requests.post("https://www.shoppersstack.com/shopping/users/login" , json=payload2 , verify=False)
assert 200 == res2.status_code , f"not equal {res2.status_code}"
print(res2.json())
data = res2.json()

user_id=data["data"]["userId"]
token=data["data"]["jwtToken"]
print(user_id)
print(token)


headers = {
        "Authorization": f"Bearer {token}"
}
# first adds token in request header then Bearer = authentication scheme

res3 = requests.get(f"https://www.shoppersstack.com/shopping/shoppers/{user_id}",headers=headers,verify=False)
assert 200 == res3.status_code , f"not equal {res3.status_code}"
print(res3.json())


