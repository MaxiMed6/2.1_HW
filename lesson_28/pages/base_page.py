from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BasePage:
    def __init__(self, driver):
        self._driver = driver
        self.url = None

    def open_page(self, url=None):
        url = url or self.url
        self._driver.get(url)


    def _button(self, locator):
        return WebDriverWait(self._driver, timeout=5).until(
            EC.element_to_be_clickable(locator))

    def _field_is_located(self, locator):
        return WebDriverWait(self._driver, timeout=5).until(
            EC.presence_of_element_located(locator))



