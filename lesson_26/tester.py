from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.print_page_options import PrintOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

try:
    driver.get("http://localhost:8000/dz.html")
    print("Сторінка завантажена")

    print("Frame1")
    driver.switch_to.frame("frame1")
    time.sleep(5)

    input1 = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='input1']")))
    input1.clear()
    input1.send_keys("Frame1_Secret")
    time.sleep(5)
    button = driver.find_element(By.XPATH, "//button[contains(@onclick, 'input1')]")
    button.click()

    alert = wait.until(EC.alert_is_present())
    assert "Верифікація пройшла успішно!" in alert.text
    print("Frame1: Успішно")
    time.sleep(5)
    alert.accept()
    input1.clear()

    driver.switch_to.default_content()

    print('Frame2')
    driver.switch_to.frame("frame2")
    time.sleep(5)

    input2 = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='input2']")))
    input2.clear()
    input2.send_keys("Frame2_Secret")

    time.sleep(5)
    button = driver.find_element(By.XPATH, "//button[contains(@onclick, 'input2')]")
    button.click()

    alert = wait.until(EC.alert_is_present())
    assert "Верифікація пройшла успішно!" in alert.text
    print("Frame2: Успішно")
    time.sleep(5)
    alert.accept()
    input2.clear()

    driver.switch_to.default_content()

    print("\nВсі фрейми оброблено!")

except TimeoutException as e:
    print(f"Помилка очікування: {e}")
except AssertionError as e:
    print(f"Помилка перевірки: {e}")
except Exception as e:
    print(f"Загальна помилка: {e}")

finally:
    time.sleep(2)
    driver.quit()