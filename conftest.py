import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from api.booking_client import BookingClient

API_USERNAME = "admin"
API_PASSWORD = "password123"


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--window-size=1400,1000")
    if os.getenv("HEADLESS"):
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    chrome_driver = webdriver.Chrome(service=service, options=options)
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture(scope="session")
def booking_client():
    return BookingClient()


@pytest.fixture(scope="session")
def auth_token(booking_client):
    response = booking_client.create_token(API_USERNAME, API_PASSWORD)
    assert response.status_code == 200
    return response.json()["token"]
