from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

def test_registration_success(driver_open_registration, generated_login, generated_valid_password):
    driver_open_registration.find_element(By.XPATH, "//label[text()='Имя']/following-sibling::input").send_keys("Ирина")
    driver_open_registration.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input").send_keys(generated_login)
    driver_open_registration.find_element(By.XPATH, "//label[text()='Пароль']/following-sibling::input").send_keys(generated_valid_password)

    driver_open_registration.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()
    WebDriverWait(driver_open_registration, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, "//button[text()='Войти']")))

    assert '/login' in driver_open_registration.current_url
    driver_open_registration.quit()

def test_registration_invalid_password_false(driver_open_registration, generated_login, generated_invalid_password):
    driver_open_registration.find_element(By.XPATH, "//label[text()='Имя']/following-sibling::input").send_keys("Ирина")
    driver_open_registration.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input").send_keys(
        generated_login)
    driver_open_registration.find_element(By.XPATH, "//label[text()='Пароль']/following-sibling::input").send_keys(
        generated_invalid_password)

    driver_open_registration.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()

    assert driver_open_registration.find_element(By.CLASS_NAME, "input__error").text == 'Некорректный пароль'

    driver_open_registration.quit()
