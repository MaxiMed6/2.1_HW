from selenium.webdriver.common.by import By


class QautoRegisterLocator:
    sign_up_button = (By.XPATH, "//button[text()='Sign up']")
    name_input = (By.XPATH, "//input[@name=\"name\"]")
    last_name = (By.XPATH, "//input[@name=\"lastName\"]")
    email = (By.XPATH, "//input[@name=\"email\"]")
    password = (By.XPATH, "//input[@name=\"password\"]")
    re_password = (By.XPATH, "//input[@name=\"repeatPassword\"]")
    register_button = (By.XPATH, "//button[@class=\"btn btn-primary\"]")

class QuatoGarageLocator:
     profile_button = (By.CSS_SELECTOR, "a[routerlink=\"profile\"]")


class QautoProfileLocator:
    user_name = (By.XPATH, "//div/p[contains(@class, \"profile_name\")]")