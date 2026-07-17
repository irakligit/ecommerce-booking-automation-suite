from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    URL = "https://www.saucedemo.com/cart.html"

    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def is_loaded(self):
        return self.is_visible(self.CHECKOUT_BUTTON)

    def checkout(self):
        self.click(self.CHECKOUT_BUTTON)
