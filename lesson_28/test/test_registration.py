import time
import pytest
from faker import Faker

fake = Faker("en_US")

def test_registration(driver,registration_page,garage_page, profile_page):
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    password = "Qwerty123"
    registration_page.sign_up_click()
    registration_page.set_user_data(first_name, last_name, email, password)
    registration_page.register_click()
    garage_page.profile_click()
    user_name = profile_page.user_name_find()
    assert user_name.split()[0] == first_name, f"Очікувалося ім’я '{first_name}', отримано '{user_name.split()[0]}'"
    print(f"Тест пройдено: ім’я '{user_name}'")







