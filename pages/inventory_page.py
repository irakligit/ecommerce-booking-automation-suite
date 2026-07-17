from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage


class InventoryPage(BasePage):
    URL = "https://www.saucedemo.com/inventory.html"

    PAGE_TITLE = (By.CLASS_NAME, "title")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    ITEM_ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.btn_inventory")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    SORT_LOW_TO_HIGH = "lohi"

    def is_loaded(self):
        return self.is_visible(self.PAGE_TITLE)

    def sort_by_price_low_to_high(self):
        Select(self.find(self.SORT_DROPDOWN)).select_by_value(self.SORT_LOW_TO_HIGH)
        return self

    def get_cheapest_item_name(self):
        """Assumes the list is already sorted low to high; the first card is the cheapest."""
        first_item = self.find_all(self.INVENTORY_ITEMS)[0]
        return first_item.find_element(*self.ITEM_NAME).text

    def add_cheapest_item_to_cart(self):
        first_item = self.find_all(self.INVENTORY_ITEMS)[0]
        first_item.find_element(*self.ITEM_ADD_TO_CART_BUTTON).click()
        return self

    def go_to_cart(self):
        self.click(self.CART_LINK)
