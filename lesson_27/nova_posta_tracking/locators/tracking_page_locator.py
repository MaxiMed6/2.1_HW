from selenium.webdriver.common.by import By


class TrackingPageLocators:
    TRACKING_FIELD = (By.XPATH, "/html/body/div/div/main/div/div/main/section/div/div/div[1]/div/div[1]/form/div/div/div/input")
    FIND_BUTTON = (By.CSS_SELECTOR, "input[type='submit']")

    ERROR_MESSAGE = (By.XPATH, "//section//div[contains(@id, 'error')]//span")
