from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..locators.tracking_page_locator import TrackingPageLocators
from lesson_27.nova_posta_tracking.pages.base_page import BasePage



# css_input number="input#np-number-input-desktop-btn-search-en"  Пытался грамотно и через css, но селениум видел елемент но не считал его кликабельным для ввода трекинг номера

class TrackingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver)
        self.url = "https://tracking.novaposhta.ua/#/uk"

    def input_tracking_number(self):
        return WebDriverWait(self.driver, timeout=5).until(
            EC.presence_of_element_located(TrackingPageLocators.TRACKING_FIELD))

    def find_button(self):
        return WebDriverWait(self.driver, timeout=5).until(
            EC.presence_of_element_located(TrackingPageLocators.FIND_BUTTON))


    def get_error_message_text(self):
        try:
            error_element = WebDriverWait(self.driver, timeout=5).until(
                EC.presence_of_element_located(TrackingPageLocators.ERROR_MESSAGE)
            )
            return error_element.text
        except TimeoutException:
            print(f"Повідомлення про помилку не знайдено")
            return None












