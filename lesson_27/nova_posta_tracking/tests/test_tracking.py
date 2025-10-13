import pytest
from  selenium.webdriver import Chrome
from lesson_27.nova_posta_tracking.pages.tracking_page import TrackingPage
import time

number = 59584633564546


def test_tracking(driver):

    tracking = TrackingPage(driver)
    tracking.open_url()

    input_tracking = tracking.input_tracking_number()
    time.sleep(5)
    input_tracking.send_keys(number)
    time.sleep(5)

    tracking_button = tracking.find_button()
    time.sleep(5)
    tracking_button.click()
    time.sleep(5)

    error_text = tracking.get_error_message_text()
    time.sleep(5)
    assert error_text is not None, "Повідомлення про помилку не з'явилося після введення неправильного номера."
    expected_error_part = "Ми не знайшли посилку за таким номером"
    assert expected_error_part in error_text, f"Очікуваний фрагмент '{expected_error_part}' не знайдено в повідомленні про помилку: '{error_text}'"

    print("Тест пройдено: повідомлення про помилку з'явилося і містить очікуваний текст.")

