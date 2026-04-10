import requests
from utils.logger import get_logger

logger = get_logger(__name__)

class WishlistAPI:

    def __init__(self, token):
        self.base_url = "https://www.shoppersstack.com/shopping"
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }


    def get_wishlist(self, shopper_id):
        url = f"{self.base_url}/shoppers/{shopper_id}/wishlist"

        logger.info(f"GET Wishlist → {url}")

        response = requests.get(url, headers=self.headers, verify=False)

        logger.info(f"Status Code → {response.status_code}")
        return response


    def add_to_wishlist(self, shopper_id, payload):
        url = f"{self.base_url}/shoppers/{shopper_id}/wishlist"

        logger.info(f"POST Wishlist → {url}")
        logger.info(f"Payload → {payload}")

        response = requests.post(url, json=payload, headers=self.headers, verify=False)

        logger.info(f"Status Code → {response.status_code}")
        return response


    def delete_from_wishlist(self, shopper_id, product_id):
        url = f"{self.base_url}/shoppers/{shopper_id}/wishlist/{product_id}"

        logger.info(f"DELETE Wishlist → {url}")

        response = requests.delete(url, headers=self.headers, verify=False)

        logger.info(f"Status Code → {response.status_code}")
        return response