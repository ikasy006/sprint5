from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

def test_authorization_from_main_page_success(driver_open_main_page):
    driver_open_main_page.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()
    WebDriverWait(driver_open_main_page, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[text()='Войти']")))
    assert '/login' in driver_open_main_page.current_url
    driver_open_main_page.quit()

def test_authorization_from_personal_account_success(driver_open_main_page):
    driver_open_main_page.find_element(By.XPATH, "//p[text()='Личный Кабинет']").click()
    WebDriverWait(driver_open_main_page, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[text()='Войти']")))
    assert '/login' in driver_open_main_page.current_url
    driver_open_main_page.quit()

def test_authorization_from_registration_form_success(driver_open_registration):
    driver_open_registration.find_element(By.XPATH, "//a[text()='Войти']").click()
    WebDriverWait(driver_open_registration, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[text()='Войти']")))
    assert '/login' in driver_open_registration.current_url
    driver_open_registration.quit()

def test_authorization_from_password_recovery_success():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/forgot-password")

    driver.find_element(By.XPATH, "//a[text()='Войти']").click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, "//button[text()='Войти']")))
    assert '/login' in driver.current_url
    driver.quit()
