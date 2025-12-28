# import requests

# BASE_URL = "https://qa-internship.avito.com/api/2/item"

# # # Список ID объявлений, которые нужно удалить
# ad_ids = [
# "00144e16-6a69-4280-b6b7-9028f0906a78",
# "f3f2b0ee-1735-463c-a83c-d82f9371fec1"
# ]

# for ad_id in ad_ids:
#     url = f"{BASE_URL}/{ad_id}"
#     response = requests.delete(url, headers={"Accept": "application/json"})
    
#     if response.status_code == 200:
#         print(f"✅ Объявление {ad_id} успешно удалено")
#     elif response.status_code == 404:
#         print(f"⚠ Объявление {ad_id} не найдено")
#     else:
#         print(f"❌ Ошибка при удалении {ad_id}: {response.status_code} - {response.text}")