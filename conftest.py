import pytest
import string
import random

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.all_locators import RegistrationPageLocators, PersonalAccountLocators
from url.url import Config
from locators.all_locators import HomePageLocators
from selenium import webdriver

@pytest.fixture
def create_driver():
    driver = webdriver.Chrome()
    driver.get(Config.BASE_URL)

    yield driver

    driver.quit()

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
def authorization(create_driver, generated_login, generated_valid_password):
    create_driver.get(Config.LOGIN_URL)

    create_driver.find_element(*RegistrationPageLocators.email_input).send_keys(generated_login)
    create_driver.find_element(*RegistrationPageLocators.password_input).send_keys(generated_valid_password)

    create_driver.find_element(*HomePageLocators.login_account_button).click()
    WebDriverWait(create_driver, 3).until(expected_conditions.visibility_of_element_located(HomePageLocators.place_order))

    return create_driver

@pytest.fixture
def personal_account(authorization):
    authorization.find_element(*HomePageLocators.account_link).click()
    WebDriverWait(authorization, 3).until(expected_conditions.visibility_of_element_located(PersonalAccountLocators.exit_button))

    return authorization
