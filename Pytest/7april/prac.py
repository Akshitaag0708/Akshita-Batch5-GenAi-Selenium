import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

session = requests.Session()

payload = {
  "city": "Jaipur",
  "country": "India",
  "email": "akshitaag0708@gmail.com",
  "firstName": "Akshita",
  "gender": "FEMALE",
  "lastName": "Agarwal",
  "password": "1234567",
  "phone": 7852849078,
  "state": "Rajasthan",
  "zoneId": "ALPHA"
}


res = session.post(
    "https://www.shoppersstack.com/shopping/shoppers",
    json=payload,
    verify=False
)
assert 409 == res.status_code
print(res.json())


payload2 = {
  "email": "akshitaag0708@gmail.com",
  "password": "1234567",
  "role": "SHOPPER"
}

res2 = session.post(
    "https://www.shoppersstack.com/shopping/users/login",
    json=payload2,
    verify=False
)
assert 200 == res2.status_code
print(res2.json())

data = res2.json()
user_id = data["data"]["userId"]
token = data["data"]["jwtToken"]

print(user_id)
print(token)


session.headers.update({
    "Authorization": f"Bearer {token}"
})

res3 = session.get(
    f"https://www.shoppersstack.com/shopping/shoppers/{user_id}",
    verify=False
)
assert 200 == res3.status_code
print(res3.json())