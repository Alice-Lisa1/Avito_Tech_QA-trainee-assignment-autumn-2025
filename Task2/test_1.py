#1 Проверка диапазона значений sellerId
import requests
import random
import pytest

URL = "https://qa-internship.avito.com/api/1/item"

cases = [
    (111111, 200),
    (499999, 200),
    (999999, 200),
    (111110, 400),
    (1000000, 400)
]

@pytest.mark.parametrize("seller_id, expected_status", cases)
def test_seller_id_range(seller_id, expected_status):
    ad_data = {
        "sellerID": seller_id,
        "name": "Тестовое имя",
        "price": random.randint(1000, 200000),
        "statistics": {
            "likes": random.randint(0, 1000),
            "viewCount": random.randint(0, 10000),
            "contacts": random.randint(0, 500)
        }
    }

    response = requests.post(URL, json=ad_data)

    # Проверка HTTP-статуса
    assert response.status_code == expected_status
    response_json = response.json()

    # Проверки о создании объявления
    if expected_status == 200:
        status_text = response_json.get("status", "")
        assert " - " in status_text, "❌ В ответе нет ID созданного объявления"

    # Проверки для ошибки валидации
    if expected_status == 400:
        assert "status" in response_json, "❌ Нет поля status в ответе 400"
        assert "result" in response_json, "❌ Нет поля result в ответе 400"