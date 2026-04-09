from api.wishlist.get_wishlist import WishlistAPI

def test_add_to_wishlist(auth_data, headers):
    wishlist_api = WishlistAPI()

    shopper_id = auth_data["shopper_id"]

    response = wishlist_api.add_to_wishlist(
        shopper_id=shopper_id,
        headers=headers,
        product_id=51,
        quantity=1
    )

    res_json = response.json()
    print(res_json)


    if response.status_code == 409:
        assert res_json["message"] == "CONFLICT"
        assert "already present" in res_json["data"]
    else:
        assert response.status_code in [200, 201]
        assert res_json["statusCode"] == 200

def test_get_wishlist(auth_data, headers):
    wishlist_api = WishlistAPI()

    shopper_id = auth_data["shopper_id"]

    response = wishlist_api.get_wishlist(
        shopper_id=shopper_id,
        headers=headers
    )

    res_json = response.json()
    print(res_json)


    assert response.status_code == 200
    assert res_json["statusCode"] == 200
    assert res_json["message"] == "Success"


    assert isinstance(res_json["data"], list)

    # Optional: if items exist
    if len(res_json["data"]) > 0:
        assert "productId" in res_json["data"][0]
        assert "productName" in res_json["data"][0]