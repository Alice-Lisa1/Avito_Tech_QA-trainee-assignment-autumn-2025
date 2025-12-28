 # 6 Проверка поведения при полном сценарии запросов(авто)
import requests

BASE_URL = "https://qa-internship.avito.com/api/1/item"
TEST_SELLER_ID = 17092025

def test_full_flow(ad_id):
    """Полный сценарий: GET по ID -> GET по продавцу -> Валидация данных"""
    
    # Проверка получения по конкретному ID
    resp_id = requests.get(f"{BASE_URL}/{ad_id}")
    print(f"\nШаг 1: GET по ID {ad_id}. Статус: {resp_id.status_code}")
    assert resp_id.status_code == 200
    
    # Обработка ответа 
    data = resp_id.json()
    item = data[0] if isinstance(data, list) else data
    assert item["sellerId"] == TEST_SELLER_ID, "ID продавца в объявлении не совпадает"

    # Проверка наличия объявления в списке продавца
    resp_seller = requests.get(f"https://qa-internship.avito.com/api/1/{TEST_SELLER_ID}/item")
    print(f"Шаг 2: GET по продавцу {TEST_SELLER_ID}. Статус: {resp_seller.status_code}")
    assert resp_seller.status_code == 200
    
    ads = resp_seller.json()
    assert any(ad["id"] == ad_id for ad in ads), f"Объявление {ad_id} не найдено в списке продавца"

    # Валидация полей статистики
    stats = item.get("statistics", {})
    print(f"Шаг 3: Проверка полей статистики. Найдено: {list(stats.keys())}")
    
    assert stats.get("likes", -1) >= 0
    assert stats.get("viewCount", -1) >= 0
    assert stats.get("contacts", -1) >= 0

    print(f"✓ Полный сценарий выполнен успешно для ad_id={ad_id}")