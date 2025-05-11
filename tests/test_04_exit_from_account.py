from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

def test_exit_from_account(driver_open_personal_account):
    driver_open_personal_account.find_element(By.XPATH, "//button[text()='Выход']").click()
    WebDriverWait(driver_open_personal_account, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, "//button[text()='Войти']")))

    assert '/login' in driver_open_personal_account.current_url

    driver_open_personal_account.quit()
