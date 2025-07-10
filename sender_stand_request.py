# Анна Антипова, 32-я когорта — Финальный проект. Инженер по тестированию плюс

import requests
from data import order_data
from config import BASE_URL
from config import CREATE_URL
from config import ORDER_TRACK_URL


def post_new_order():
    response = requests.post(CREATE_URL, json=order_data)
    response.raise_for_status()
    return response.json()["track"]

def get_order_by_track(track_number):
    response = requests.get(ORDER_TRACK_URL, params={"t": track_number})
    return response