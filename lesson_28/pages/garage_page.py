from .locators import QuatoGarageLocator
from ..pages.base_page import BasePage

class GaragePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver=driver)
        self.url = None
        self.locators = QuatoGarageLocator()


    def _profile_button(self):
        return self._button(self.locators.profile_button)


    def profile_click(self):
        return self._profile_button().click()







