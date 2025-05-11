from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

def test_transition_in_personal_account(driver_authorization):
    driver_authorization.find_element(By.XPATH, "//p[text()='Личный Кабинет']").click()
    WebDriverWait(driver_authorization, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, "//button[text()='Сохранить']")))

    assert "/profile" in driver_authorization.current_url
    driver_authorization.quit()
