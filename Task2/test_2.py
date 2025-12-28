#2  Создание объявления
def test_ad_creation(ad_data):
    # Статус берется из фикстуры
    print(f"\nID: {ad_data.get('id')}, Имя: {ad_data['name']}")
    print(f"✅ Объявление создано успешно (Статус 200)")