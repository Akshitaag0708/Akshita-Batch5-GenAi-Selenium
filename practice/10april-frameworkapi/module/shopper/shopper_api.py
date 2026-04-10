import requests
import os
from utils.logger import get_logger

logger = get_logger(__name__)

class ShopperAPI:

    def __init__(self, token):
        self.base_url = os.getenv("BASE_URL")
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

    def get_shopper(self, shopper_id):
        url = f"{self.base_url}/shoppers/{shopper_id}"

        logger.info(f"GET Request → {url}")
        response = requests.get(url, headers=self.headers, verify=False)

        logger.info(f"Response Status → {response.status_code}")
        logger.debug(f"Response Body → {response.text}")

        return response

    def update_shopper(self, shopper_id, payload):
        url = f"{self.base_url}/shoppers/{shopper_id}"

        logger.info(f"PATCH Request → {url}")
        logger.info(f"Payload → {payload}")

        response = requests.patch(url, json=payload, headers=self.headers, verify=False)

        logger.info(f"Response Status → {response.status_code}")
        logger.debug(f"Response Body → {response.text}")

        return response