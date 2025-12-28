# 3 Получение объявления по ID
import requests

def test_get_ad_by_id(ad_id):
    url = f"https://qa-internship.avito.com/api/1/item/{ad_id}"  
    response = requests.get(url)
    print(f"\nGET по ID {ad_id}. Статус ответа: {response.status_code}")
    assert response.status_code == 200
    item = response.json()[0] if isinstance(response.json(), list) else response.json()
    assert item["sellerId"] == 17092025
    print(f"✓ Объявление по ID проверено: {item}")
