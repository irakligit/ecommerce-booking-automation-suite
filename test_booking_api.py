import pytest

BOOKING_PAYLOAD = {
    "firstname": "James",
    "lastname": "Brown",
    "totalprice": 250,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2026-08-01",
        "checkout": "2026-08-05",
    },
    "additionalneeds": "Breakfast",
}


def assert_booking_schema(booking):
    assert isinstance(booking["firstname"], str)
    assert isinstance(booking["lastname"], str)
    assert isinstance(booking["totalprice"], int)
    assert isinstance(booking["depositpaid"], bool)
    assert isinstance(booking["bookingdates"]["checkin"], str)
    assert isinstance(booking["bookingdates"]["checkout"], str)
    assert isinstance(booking["additionalneeds"], str)


@pytest.fixture
def created_booking(booking_client):
    response = booking_client.create_booking(BOOKING_PAYLOAD)
    assert response.status_code == 200
    body = response.json()
    return body["bookingid"], body["booking"]


def test_create_booking_returns_valid_schema(created_booking):
    _, booking = created_booking
    assert_booking_schema(booking)
    assert booking["firstname"] == BOOKING_PAYLOAD["firstname"]
    assert booking["lastname"] == BOOKING_PAYLOAD["lastname"]
    assert booking["totalprice"] == BOOKING_PAYLOAD["totalprice"]
    assert booking["depositpaid"] == BOOKING_PAYLOAD["depositpaid"]
    assert booking["bookingdates"] == BOOKING_PAYLOAD["bookingdates"]
    assert booking["additionalneeds"] == BOOKING_PAYLOAD["additionalneeds"]
