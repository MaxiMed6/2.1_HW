from .locators import QautoProfileLocator
from ..pages.base_page import BasePage


class ProfilePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver=driver)
        self.url = None
        self.locators = QautoProfileLocator()


    def user_name_find(self):
        return self._field_is_located(self.locators.user_name).text





