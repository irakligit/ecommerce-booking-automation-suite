from pytest_bdd import scenarios, given, when, then, parsers

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import (
    CheckoutInfoPage,
    CheckoutOverviewPage,
    CheckoutCompletePage,
)

scenarios("../features/checkout.feature")


@given(parsers.parse('I am logged in as "{username}" with password "{password}"'))
def login(driver, username, password):
    login_page = LoginPage(driver).open()
    login_page.login(username, password)
    assert InventoryPage(driver).is_loaded()


@when("I sort the products by price low to high")
def sort_products_by_price(driver):
    InventoryPage(driver).sort_by_price_low_to_high()


@when("I add the cheapest item to the cart", target_fixture="cheapest_item_name")
def add_cheapest_item_to_cart(driver):
    inventory_page = InventoryPage(driver)
    cheapest_item_name = inventory_page.get_cheapest_item_name()
    inventory_page.add_cheapest_item_to_cart()
    return cheapest_item_name


@when("I proceed to checkout")
def proceed_to_checkout(driver):
    InventoryPage(driver).go_to_cart()
    cart_page = CartPage(driver)
    assert cart_page.is_loaded()
    cart_page.checkout()


@when(parsers.parse('I enter my shipping details as "{first_name}" "{last_name}" "{postal_code}"'))
def enter_shipping_details(driver, first_name, last_name, postal_code):
    CheckoutInfoPage(driver).fill_shipping_details(
        first_name, last_name, postal_code
    ).continue_to_overview()


@when("I finish the order")
def finish_order(driver):
    CheckoutOverviewPage(driver).finish()


@then(parsers.parse('the page title should show "{expected_title}"'))
def assert_page_title(driver, expected_title):
    assert CheckoutCompletePage(driver).get_page_title() == expected_title


@then(parsers.parse('the order confirmation should say "{expected_message}"'))
def assert_order_confirmation(driver, expected_message):
    complete_page = CheckoutCompletePage(driver)
    assert complete_page.is_order_complete()
    assert expected_message in complete_page.get_confirmation_message()
