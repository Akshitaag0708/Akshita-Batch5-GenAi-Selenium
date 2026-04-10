from utils.logger import get_logger
from module.shopper.shopper_api import ShopperAPI
from utils.read import read_json

logger = get_logger(__name__)

def test_update_shopper(auth_data):

    token = auth_data["token"]
    shopper_id = auth_data["shopper_id"]

    logger.info("Starting test_update_shopper")

    shopper_api = ShopperAPI(token)

    data = read_json("test_data/shopper.json")
    payload = data["update_user"]

    response = shopper_api.update_shopper(shopper_id, payload)

    logger.info(f"Status Code → {response.status_code}")
    logger.info(f"Response → {response.text}")

    assert response.status_code == 200