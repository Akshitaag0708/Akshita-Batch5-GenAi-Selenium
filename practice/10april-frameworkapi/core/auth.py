from module.login.login import LoginAPI
from utils.read import read_json

login_api = LoginAPI()

def get_auth_data():
    data = read_json("test_data/login.json")
    payload = data["valid_user"]

    response = login_api.login(payload)


    assert response.status_code == 200

    res_json = response.json()

    token = res_json["data"]["jwtToken"]
    shopper_id = res_json["data"]["userId"]

    return {
        "token": token,
        "shopper_id": shopper_id
    }