from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutInfoPage(BasePage):
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")

    def fill_shipping_details(self, first_name, last_name, postal_code):
        self.type_text(self.FIRST_NAME_INPUT, first_name)
        self.type_text(self.LAST_NAME_INPUT, last_name)
        self.type_text(self.POSTAL_CODE_INPUT, postal_code)
        return self

    def continue_to_overview(self):
        self.click(self.CONTINUE_BUTTON)


class CheckoutOverviewPage(BasePage):
    FINISH_BUTTON = (By.ID, "finish")

    def finish(self):
        self.click(self.FINISH_BUTTON)


class CheckoutCompletePage(BasePage):
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def get_confirmation_message(self):
        return self.get_text(self.COMPLETE_HEADER)

    def is_order_complete(self):
        return self.is_visible(self.COMPLETE_HEADER)
