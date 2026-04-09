from core.base_api import BaseAPI
from utils.config import BASE_URL


class CardAPI:

    def __init__(self):
        self.api = BaseAPI(BASE_URL)


    def get_cards(self):
        return self.api.get("/cards")


    def create_card(self, payload, headers):
        return self.api.post("/cards", headers=headers, json=payload)


    def update_card(self, payload):
        return self.api.patch("/cards", json=payload)


    def card_transaction(self, payload):
        return self.api.post("/cards/transaction", json=payload)


    def verify_card(self, payload):
        return self.api.post("/cards/verify", json=payload)