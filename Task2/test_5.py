#  5 Получение статистики по itemID 
def test_get_statistics_by_item(ad_data):
    "Проверка статистики объявления. Данные приходят из фикстуры ad_data (GET уже был успешен)."
    print(f"\n--- Проверка статистики для ID: {ad_data.get('id')} ---")
    print("Статус получения данных: 200 OK")
    stats = ad_data.get("statistics", {})

    print("Статистика объявления:")
    print(f"Likes: {stats.get('likes')}")
    print(f"ViewCount: {stats.get('viewCount')}")
    print(f"Contacts: {stats.get('contacts')}")

    # Проверка наличия полей
    assert "likes" in stats, "Поле 'likes' отсутствует"
    assert "viewCount" in stats, "Поле 'viewCount' отсутствует"
    assert "contacts" in stats, "Поле 'contacts' отсутствует"

    # Проверка типов данных
    assert isinstance(stats["likes"], int), "'likes' должен быть числом"
    assert isinstance(stats["viewCount"], int), "'viewCount' должен быть числом"
    assert isinstance(stats["contacts"], int), "'contacts' должен быть числом"

    # Проверка логики 
    assert stats["likes"] >= 0, "'likes' не может быть отрицательным"
    assert stats["viewCount"] >= 0, "'viewCount' не может быть отрицательным"
    assert stats["contacts"] >= 0, "'contacts' не может быть отрицательным"

    print("✅ Статистика успешно проверена")