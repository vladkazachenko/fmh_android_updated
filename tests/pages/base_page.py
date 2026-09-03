from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find_visible(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def find_present(self, locator, timeout=None):
        wait = (
            self.wait
            if timeout is None
            else WebDriverWait(self.driver, timeout)
        )

        return wait.until(
            EC.presence_of_element_located(locator)
        )

    def find_clickable(self, locator):
        return self.wait.until(
            EC.element_to_be_clickable(locator)
        )

    def click(self, locator):
        self.find_clickable(locator).click()

    def enter_text(self, locator, text):
        element = self.find_visible(locator)
        element.clear()
        element.send_keys(text)