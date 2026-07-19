from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    URL = "https://www.saucedemo.com/cart.html"

    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CART_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def is_loaded(self):
        return self.is_visible(self.CHECKOUT_BUTTON)

    def get_item_names(self):
        return [item.text for item in self.find_all(self.CART_ITEM_NAME)]

    def checkout(self):
        self.click(self.CHECKOUT_BUTTON)
