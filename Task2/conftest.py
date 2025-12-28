import requests
import pytest
import random

BASE_URL = "https://qa-internship.avito.com/api/1/item"
TEST_SELLER_ID = 17092025

@pytest.fixture(scope="session")
def ad_id():
    "Создает одно объявление и возвращает только его id"
    name = f"Смартфон iPhone 14 - {random.randint(1, 10000)}"
    price = random.randint(1000, 200000)
    
    ad_data = {
        "sellerID": TEST_SELLER_ID,
        "name": name,
        "price": price,
        "statistics": {
            "likes": random.randint(0, 1000),
            "viewCount": random.randint(0, 10000),
            "contacts": random.randint(0, 500)
        }
    } 

    response = requests.post(BASE_URL, json=ad_data)
    assert response.status_code == 200, f"Не удалось создать объявление: {response.text}"
    
    # Извлекаем ID из строки "Сохраняем объявление"
    created_id = response.json()["status"].split(" - ")[1]
    print(f"\n[Fixture] Создано тестовое объявление: {created_id}")
    return created_id

@pytest.fixture(scope="session")
def ad_data(ad_id):
    "Возвращает полные данные созданного объявления по его ID"
    response = requests.get(f"{BASE_URL}/{ad_id}")
    assert response.status_code == 200
    
    # берем из API первый элемент
    data = response.json()
    return data[0] if isinstance(data, list) else data