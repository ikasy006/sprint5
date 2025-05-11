import pytest
import string
import random

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

@pytest.fixture(scope="session")
def generated_valid_password():
    length = 6
    chars = string.ascii_letters + string.digits
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

@pytest.fixture(scope="session")
def generated_invalid_password():
    length = 5
    chars = string.ascii_letters + string.digits
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

@pytest.fixture(scope="session")
def generated_login():
    number = random.randint(100, 999)
    login = f"irina_kasyanova_22_{number}@ya.ru"
    return login

@pytest.fixture
def driver_open_registration():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/register")
    return driver

@pytest.fixture
def driver_open_main_page():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    return driver

@pytest.fixture
def driver_authorization(generated_login, generated_valid_password):
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/login")

    driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input").send_keys(
        generated_login)
    driver.find_element(By.XPATH, "//label[text()='Пароль']/following-sibling::input").send_keys(
        generated_valid_password)
    driver.find_element(By.XPATH, "//button[text()='Войти']").click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.ID, 'root')))
    return driver

@pytest.fixture
def driver_open_personal_account(driver_authorization):
    driver_authorization.find_element(By.XPATH, "//p[text()='Личный Кабинет']").click()
    WebDriverWait(driver_authorization, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[text()='Сохранить']")))
    return driver_authorization

