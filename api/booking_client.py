import requests


class BookingClient:
    BASE_URL = "https://restful-booker.herokuapp.com"

    def create_token(self, username, password):
        return requests.post(
            f"{self.BASE_URL}/auth",
            json={"username": username, "password": password},
        )

    def create_booking(self, payload):
        return requests.post(f"{self.BASE_URL}/booking", json=payload)

    def get_booking(self, booking_id):
        return requests.get(f"{self.BASE_URL}/booking/{booking_id}")

    def update_booking(self, booking_id, payload, token):
        return requests.put(
            f"{self.BASE_URL}/booking/{booking_id}",
            json=payload,
            headers={"Cookie": f"token={token}"},
        )

    def partial_update_booking(self, booking_id, payload, token):
        return requests.patch(
            f"{self.BASE_URL}/booking/{booking_id}",
            json=payload,
            headers={"Cookie": f"token={token}"},
        )

    def delete_booking(self, booking_id, token):
        return requests.delete(
            f"{self.BASE_URL}/booking/{booking_id}",
            headers={"Cookie": f"token={token}"},
        )
