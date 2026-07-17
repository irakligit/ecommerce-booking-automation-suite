# saucedemo-checkout-automation

Selenium + pytest-bdd checkout test for [saucedemo.com](https://www.saucedemo.com/), using the Page Object Model.

## What it does

Logs in as `standard_user`, sorts the products by price low to high, adds
the cheapest one to the cart, goes through checkout with some dummy shipping
info, and checks that the order actually completes.

Scenario lives in `features/checkout.feature`.

## Layout

```
features/checkout.feature
pages/
  base_page.py
  login_page.py
  inventory_page.py
  cart_page.py
  checkout_page.py
step_defs/test_checkout.py
conftest.py
pytest.ini
```

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Needs Chrome installed. webdriver-manager grabs the matching chromedriver on its own.

## Running it

```bash
pytest -v
```

Headless:

```bash
HEADLESS=1 pytest -v
```
