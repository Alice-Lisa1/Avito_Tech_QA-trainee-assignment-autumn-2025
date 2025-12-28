# 4 Получение всех объявлений по sellerID
import requests

TEST_SELLER_ID = 17092025 
def test_get_ads_by_seller():
    url = f"https://qa-internship.avito.com/api/1/{TEST_SELLER_ID}/item"
    response = requests.get(url)
    print(f"\nGET объявлений продавца {TEST_SELLER_ID}. Статус ответа: {response.status_code}")

    assert response.status_code == 200
    
    ads = response.json()
    ids_list = [item["id"] for item in ads]

    print(f"\n--- Найдено объявлений: {len(ads)} ---")
    
    for ad in ads:
        print(f"ID: {ad['id']} | Name: {ad.get('name')} | Price: {ad.get('price')}")

    # Печатаем список ID для удаления объявлений
    print(f"\nВсе ID списком для копирования:")
    for i in ids_list:
        print(f'"{i}",')