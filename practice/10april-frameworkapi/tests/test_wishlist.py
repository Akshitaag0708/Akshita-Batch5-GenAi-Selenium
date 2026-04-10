from module.wishlist.wishlist_api import WishlistAPI
from utils.read import read_json
from utils.logger import get_logger
from core.auth import get_auth_data

logger = get_logger(__name__)


def test_get_wishlist():
    auth = get_auth_data()

    token = auth["token"]
    shopper_id = auth["shopper_id"]

    wishlist_api = WishlistAPI(token)

    response = wishlist_api.get_wishlist(shopper_id)

    logger.info(f"Response → {response.text}")

    assert response.status_code == 200


def test_add_to_wishlist():
    auth = get_auth_data()

    token = auth["token"]
    shopper_id = auth["shopper_id"]

    wishlist_api = WishlistAPI(token)

    data = read_json("test_data/wishlist.json")
    payload = data["add_item"]

    response = wishlist_api.add_to_wishlist(shopper_id, payload)

    logger.info(f"Response → {response.text}")

    assert response.status_code in [200, 201 , 409]


def test_delete_from_wishlist():
    auth = get_auth_data()
    token = auth["token"]
    shopper_id = auth["shopper_id"]


    wishlist_api = WishlistAPI(token)

    product_id = 1

    response = wishlist_api.delete_from_wishlist(shopper_id, product_id)

    logger.info(f"Response → {response.text}")

    assert response.status_code in [200, 204 , 404]