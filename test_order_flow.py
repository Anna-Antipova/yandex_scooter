import pytest
from sender_stand_request import post_new_order, get_order_by_track

def test_order_creation_and_tracking():
    track_number = post_new_order()
    response = get_order_by_track(track_number)

    assert response.status_code == 200
    assert "order" in response.json()