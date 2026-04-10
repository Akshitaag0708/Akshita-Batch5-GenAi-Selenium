import pytest
from module.login.login import LoginAPI
from utils.read import read_json

@pytest.fixture(scope="session")
def auth_data():
    login_api = LoginAPI()
    data = read_json("test_data/login.json")

    response = login_api.login(data["valid_user"])
    res_json = response.json()

    return {
        "token": res_json["data"]["jwtToken"],
        "shopper_id": res_json["data"]["userId"]
    }