from utils.read_data import read_json
from api.bank_card.card_api import CardAPI

data = read_json("test_data/card_data.json")

def test_create_card(headers):
    card = CardAPI()

    payload = data["valid_card"]
    response = card.create_card(payload, headers=headers)

    assert response.status_code in [200,201]