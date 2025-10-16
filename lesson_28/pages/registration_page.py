from .locators import QautoRegisterLocator
from ..pages.base_page import BasePage
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from settings import settings


class RegistrationPage(BasePage):


    def __init__(self, driver):
        super().__init__(driver=driver)
        self.url = settings.BASE_URL
        self.locators = QautoRegisterLocator()

    def _name_input(self):
        return self._field_is_located(self.locators.name_input)

    def _last_name_input(self):
        return self._field_is_located(self.locators.last_name)


    def _email_input(self):
        return self._field_is_located(self.locators.email)

    def _password_input(self):
        return self._field_is_located(self.locators.password)

    def _re_password_input(self):
        return self._field_is_located(self.locators.re_password)


    def _register_button(self):
        return self._button(self.locators.register_button)

    def _sign_up_button(self):
        return self._button(self.locators.sign_up_button)



    def set_user_data(self, name, last_name, email, password):
        self._name_input().send_keys(name)
        self._last_name_input().send_keys(last_name)
        self._email_input().send_keys(email)
        self._password_input().send_keys(password)
        self._re_password_input().send_keys(password)
        return self


    def sign_up_click(self):
        return self._sign_up_button().click()


    def register_click(self):
        return self._register_button().click()