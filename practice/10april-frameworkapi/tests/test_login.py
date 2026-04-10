from module.login.login import LoginAPI
from utils.read import read_json
login_api = LoginAPI()

def test_login():
    data = read_json("test_data/login.json")

    payload = data["valid_user"]

    response = login_api.login(payload)

    assert response.status_code == 200
    res_json = response.json()
    shopper_id = res_json["data"]["userId"]
    print("SHOPPER ID:", shopper_id)


def test_wrong_login():
    data = read_json("test_data/login.json")

    payload = data["invalid_user"]

    response = login_api.login(payload)

    assert response.status_code in [400, 401]



