from pytest_bdd import scenarios, given, when, then, parsers

scenarios("../features/booking_crud.feature")

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


@given("I am authenticated with the booking API")
def authenticated(auth_token):
    assert auth_token


@given("I have created a booking", target_fixture="created_booking")
def have_created_booking(booking_client, auth_token):
    response = booking_client.create_booking(BOOKING_PAYLOAD)
    assert response.status_code == 200
    body = response.json()
    booking_id = body["bookingid"]
    yield booking_id, body["booking"]
    booking_client.delete_booking(booking_id, auth_token)


@when("I create a booking", target_fixture="created_booking")
def create_booking(booking_client, auth_token):
    response = booking_client.create_booking(BOOKING_PAYLOAD)
    assert response.status_code == 200
    body = response.json()
    booking_id = body["bookingid"]
    yield booking_id, body["booking"]
    booking_client.delete_booking(booking_id, auth_token)


@then("the booking response should match a valid schema")
def check_schema(created_booking):
    _, booking = created_booking
    assert_booking_schema(booking)


@then("the booking should match what I sent")
def check_values(created_booking):
    _, booking = created_booking
    assert booking["firstname"] == BOOKING_PAYLOAD["firstname"]
    assert booking["lastname"] == BOOKING_PAYLOAD["lastname"]
    assert booking["totalprice"] == BOOKING_PAYLOAD["totalprice"]
    assert booking["depositpaid"] == BOOKING_PAYLOAD["depositpaid"]
    assert booking["bookingdates"] == BOOKING_PAYLOAD["bookingdates"]
    assert booking["additionalneeds"] == BOOKING_PAYLOAD["additionalneeds"]


@when(parsers.parse("I update the booking's total price to {new_price:d}"), target_fixture="updated_booking_id")
def update_booking(booking_client, auth_token, created_booking, new_price):
    booking_id, _ = created_booking
    updated_payload = {**BOOKING_PAYLOAD, "totalprice": new_price}
    response = booking_client.update_booking(booking_id, updated_payload, auth_token)
    assert response.status_code == 200
    return booking_id


@then(parsers.parse("the booking's total price should be {expected_price:d}"))
def check_updated_price(booking_client, updated_booking_id, expected_price):
    fetched = booking_client.get_booking(updated_booking_id)
    assert fetched.json()["totalprice"] == expected_price


@when("I delete the booking", target_fixture="deleted_booking_id")
def delete_booking(booking_client, auth_token, created_booking):
    booking_id, _ = created_booking
    response = booking_client.delete_booking(booking_id, auth_token)
    assert response.status_code in (200, 201)
    return booking_id


@then("the booking should no longer exist")
def check_deleted(booking_client, deleted_booking_id):
    fetched = booking_client.get_booking(deleted_booking_id)
    assert fetched.status_code == 404
