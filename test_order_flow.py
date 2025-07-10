
import requests
from config import BASE_URL

create_url = f"{BASE_URL}/api/v1/orders"
order_track_url = f"{BASE_URL}/api/v1/orders/track"


def create_order():
    order_data = {
        "firstName": "Иван",
        "lastName": "Иванов",
        "address": "ул. Ленина, д. 1",
        "metroStation": "Сокол",
        "phone": "+79991234567",
        "rentTime": 3,
        "deliveryDate": "2025-07-11",
        "comment": "Оставить у двери",
        "color": ["BLACK"]
    }

    response = requests.post(create_url, json=order_data)
    response.raise_for_status()
    return response.json()["track"]


def get_order_by_track(track_number):
    response = requests.get(order_track_url, params={"t": track_number})
    return response


def test_order_creation_and_tracking():
    track_number = create_order()
    response = get_order_by_track(track_number)

    assert response.status_code == 200, f"Expected status 200, got {response.status_code}"
    assert "order" in response.json(), "В ответе отсутствует информация о заказе"
