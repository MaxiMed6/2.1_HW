import pytest
from selenium import webdriver
from selenium.webdriver import Chrome
from lesson_28.pages.garage_page import GaragePage
from lesson_28.pages.profile_page import ProfilePage
from lesson_28.pages.registration_page import RegistrationPage


@pytest.fixture
def driver():
    driver = Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def registration_page(driver):
    registration_page=RegistrationPage(driver)
    registration_page.open_page()
    return registration_page


@pytest.fixture
def garage_page(driver):
    garage_page = GaragePage(driver)
    return garage_page


@pytest.fixture
def profile_page(driver):
    profile_page = ProfilePage(driver)
    return profile_page
