# import requests
# import pytest
# from test_2 import ad_id as ad_fixture  # фикстура создаёт одно объявление

# BASE_URL = "https://qa-internship.avito.com/api/1"
# TEST_SELLER_ID = 111111

# def test_get_ads_by_seller(ad_fixture):
#     """
#     Получить все объявления продавца списком
#     ad_fixture создаёт одно тестовое объявление
#     """
#     url = f"{BASE_URL}/{TEST_SELLER_ID}/item"
#     headers = {"Accept": "application/json"}

#     response = requests.get(url, headers=headers)

#     # Проверка статуса запроса
#     assert response.status_code == 200, f"Ошибка запроса: {response.status_code} {response.text}"

#     ads = response.json()  # это уже список всех объявлений продавца

#     # Проверка что хотя бы одно объявление вернулось
#     assert len(ads) > 0, "Нет объявлений у этого продавца"

#     # Проверка sellerId у всех объявлений
#     for ad in ads:
#         assert ad.get("sellerId") == TEST_SELLER_ID, f"Неверный sellerId: {ad.get('sellerId')}"

#     # Выводим список объявлений
#     print("Все объявления продавца:")
#     for ad in ads:
#         print(f"ID: {ad['id']}, Name: {ad['name']}, Price: {ad['price']}")