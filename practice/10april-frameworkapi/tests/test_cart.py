from module.cart.cart_api import CartAPI
from utils.read import read_json
from utils.logger import get_logger
from core.auth import get_auth_data

logger = get_logger(__name__)


def test_get_cart():
    auth = get_auth_data()
    token = auth["token"]
    shopper_id = auth["shopper_id"]

    cart_api = CartAPI(token)

    response = cart_api.get_cart(shopper_id)

    logger.info(f"Response → {response.text}")

    assert response.status_code == 200


def test_add_to_cart():
    auth = get_auth_data()
    token = auth["token"]
    shopper_id = auth["shopper_id"]

    cart_api = CartAPI(token)

    data = read_json("test_data/cart.json")
    payload = data["add_item"]

    response = cart_api.add_to_cart(shopper_id, payload)

    logger.info(f"Response → {response.text}")

    assert response.status_code in [200, 201, 409]   # 409 if already exists


def test_update_cart():
    auth = get_auth_data()
    token = auth["token"]
    shopper_id = auth["shopper_id"]

    cart_api = CartAPI(token)


    get_res = cart_api.get_cart(shopper_id)
    data = get_res.json()

    if data["data"]:
        item_id = data["data"][0]["productId"]
    else:
        item_id = 1   # fallback

    payload = {
        "productId": item_id,
        "quantity": 2
    }

    response = cart_api.update_cart(shopper_id, item_id, payload)

    logger.info(f"Response → {response.text}")

    assert response.status_code in [200, 404]


def test_delete_from_cart():
    auth = get_auth_data()
    token = auth["token"]
    shopper_id = auth["shopper_id"]

    cart_api = CartAPI(token)

    get_res = cart_api.get_cart(shopper_id)
    data = get_res.json()

    if data["data"]:
        product_id = data["data"][0]["productId"]
    else:
        product_id = 1   # fallback

    response = cart_api.delete_from_cart(shopper_id, product_id)

    logger.info(f"Response → {response.text}")

    assert response.status_code in [200, 204, 404]