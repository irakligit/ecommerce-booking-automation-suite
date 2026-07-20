from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    DEFAULT_TIMEOUT = 20

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, self.DEFAULT_TIMEOUT)

    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_all(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.click_element(element)

    def click_element(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    def type_text(self, locator, text):
        field = self.find(locator)
        field.clear()
        field.send_keys(text)

    def get_text(self, locator):
        return self.find(locator).text

    def is_visible(self, locator):
        try:
            self.find(locator)
            return True
        except TimeoutException:
            return False
