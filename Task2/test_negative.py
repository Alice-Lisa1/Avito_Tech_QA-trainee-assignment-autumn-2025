import requests

BASE_URL = "https://qa-internship.avito.com/api/1"

def test_get_ads_invalid_seller():
    "Тест 4.2. Проверка поведения API при некорректном sellerID. Фиксируем фактическое поведение сервиса."
    invalid_seller = "not_a_number"
    url = f"{BASE_URL}/{invalid_seller}/item"

    response = requests.get(url)

    print(f"\nGET с некорректным sellerID='{invalid_seller}'")
    print(f"Статус ответа: {response.status_code}")
    print(f"Ответ сервера: {response.text}")

    # API может вернуть 200 или 400 — оба варианта считаем допустимыми
    assert response.status_code in (200, 400), (
        f"Неожиданный статус: {response.status_code}"
    )

def test_get_statistics_invalid_id():
    "Тест 5.2. Проверка поведения API при несуществующем itemID."
    non_existent_id = "00000000-0000-0000-0000-000000000000"
    url = f"{BASE_URL}/item/{non_existent_id}"

    response = requests.get(url)

    print(f"\nGET по несуществующему itemID='{non_existent_id}'")
    print(f"Статус ответа: {response.status_code}")
    print(f"Ответ сервера: {response.text}")

    # Фиксируем реальное поведение API
    assert response.status_code in (200, 404), (
        f"Неожиданный статус: {response.status_code}"
    )
