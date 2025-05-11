from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

def test_transition_to_main_page_by_logo(driver_open_personal_account):
    driver_open_personal_account.find_element(By.XPATH, "html/body/div/div/header/nav/div/a").click()
    WebDriverWait(driver_open_personal_account, 3).until(
        expected_conditions.visibility_of_element_located((By.ID, "root")))

    assert "https://stellarburgers.nomoreparties.site/" == driver_open_personal_account.current_url
    driver_open_personal_account.quit()

def test_transition_to_main_page_by_constructor(driver_open_personal_account):
    driver_open_personal_account.find_element(By.XPATH, "html/body/div/div/header/nav/div/a").click()
    WebDriverWait(driver_open_personal_account, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, "//p[text()='Конструктор']")))

    assert "https://stellarburgers.nomoreparties.site/" == driver_open_personal_account.current_url
    driver_open_personal_account.quit()
