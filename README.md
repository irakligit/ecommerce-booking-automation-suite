# Swag Labs Checkout Automation

A small, clean UI end-to-end test automation framework for the
[Swag Labs](https://www.saucedemo.com/) sandbox, built with **Selenium
WebDriver**, **pytest-bdd** (Gherkin/BDD) and the **Page Object Model**
(POM) pattern.

## Flow under test

`features/checkout.feature` describes the following user journey:

1. Log in with `standard_user` / `secret_sauce`.
2. Sort products by price, low to high.
3. Add the cheapest item to the cart.
4. Proceed to checkout, fill in mock shipping details, and finish the order.
5. Assert that the `Thank you for your order!` completion message is shown.

## Project layout

```
.
├── features/
│   └── checkout.feature      # Gherkin scenario
├── pages/                    # Page Object Model
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── step_defs/
│   └── test_checkout.py      # pytest-bdd step definitions
├── conftest.py                # WebDriver fixture
├── pytest.ini
└── requirements.txt
```

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Chrome must be installed; `webdriver-manager` downloads the matching
ChromeDriver automatically.

## Run

```bash
pytest -v
```

Run headless (e.g. in CI):

```bash
HEADLESS=1 pytest -v
```
