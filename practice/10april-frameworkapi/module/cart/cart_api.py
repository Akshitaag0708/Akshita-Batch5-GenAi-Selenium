import requests
from utils.logger import get_logger

logger = get_logger(__name__)

class CartAPI:

    def __init__(self, token):
        self.base_url = "https://www.shoppersstack.com/shopping"
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

    def get_cart(self, shopper_id):
        url = f"{self.base_url}/shoppers/{shopper_id}/carts"

        logger.info(f"GET Cart → {url}")

        response = requests.get(url, headers=self.headers, verify=False)

        logger.info(f"Status Code → {response.status_code}")
        return response

    def add_to_cart(self, shopper_id, payload):
        url = f"{self.base_url}/shoppers/{shopper_id}/carts"

        logger.info(f"POST Cart → {url}")
        logger.info(f"Payload → {payload}")

        response = requests.post(url, json=payload, headers=self.headers, verify=False)

        logger.info(f"Status Code → {response.status_code}")
        return response

    def update_cart(self, shopper_id, item_id, payload):
        url = f"{self.base_url}/shoppers/{shopper_id}/carts/{item_id}"

        logger.info(f"PUT Cart → {url}")
        logger.info(f"Payload → {payload}")

        response = requests.put(url, json=payload, headers=self.headers, verify=False)

        logger.info(f"Status Code → {response.status_code}")
        return response

    def delete_from_cart(self, shopper_id, product_id):
        url = f"{self.base_url}/shoppers/{shopper_id}/carts/{product_id}"

        logger.info(f"DELETE Cart → {url}")

        response = requests.delete(url, headers=self.headers, verify=False)

        logger.info(f"Status Code → {response.status_code}")
        return response