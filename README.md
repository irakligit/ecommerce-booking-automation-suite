# saucedemo-checkout-automation

Two pytest-bdd suites: a Selenium checkout flow for [saucedemo.com](https://www.saucedemo.com/) (Page Object Model), and an API suite against [Restful-Booker](https://restful-booker.herokuapp.com) (thin requests client).

## What it does

**UI:** Logs in as `standard_user`, sorts the products by price low to high, adds
the cheapest one to the cart, goes through checkout with some dummy shipping
info, and checks that the order actually completes.

Scenario lives in `features/checkout.feature`.

**API:** Authenticates against `/auth` to get a token, creates a booking and
checks the response shape and values, then updates and deletes that same
booking, confirming each change with a follow-up `GET`.

Scenarios live in `features/booking_crud.feature`.

## Layout

```
features/
  checkout.feature
  booking_crud.feature
pages/
  base_page.py
  login_page.py
  inventory_page.py
  cart_page.py
  checkout_page.py
api/
  booking_client.py
step_defs/
  test_checkout.py
  test_booking_api.py
conftest.py
pytest.ini
```

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Needs Chrome installed for the UI suite. webdriver-manager grabs the matching chromedriver on its own. The API suite just needs network access to restful-booker.herokuapp.com.

## Running it

Everything:

```bash
pytest -v
```

Just the UI suite:

```bash
pytest step_defs -v
```

Headless:

```bash
HEADLESS=1 pytest step_defs -v
```

Just the API suite:

```bash
pytest step_defs/test_booking_api.py -v
```
