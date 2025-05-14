from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from url.url import Config
from locators.all_locators import RegistrationPageLocators, HomePageLocators

def test_registration_success(create_driver, generated_login, generated_valid_password):
    create_driver.get(Config.REGISTER_URL)

    create_driver.find_element(*RegistrationPageLocators.name_input).send_keys('Ирина')
    create_driver.find_element(*RegistrationPageLocators.email_input).send_keys(generated_login)
    create_driver.find_element(*RegistrationPageLocators.password_input).send_keys(generated_valid_password)

    create_driver.find_element(*RegistrationPageLocators.registration_button).click()
    WebDriverWait(create_driver, 3).until(expected_conditions.visibility_of_element_located(HomePageLocators.login_account_button))

    assert "/login" in create_driver.current_url

def test_registration_invalid_password_false(create_driver, generated_login, generated_invalid_password):
    create_driver.get(Config.REGISTER_URL)

    create_driver.find_element(*RegistrationPageLocators.name_input).send_keys('Ирина')
    create_driver.find_element(*RegistrationPageLocators.email_input).send_keys(generated_login)
    create_driver.find_element(*RegistrationPageLocators.password_input).send_keys(generated_invalid_password)

    create_driver.find_element(*RegistrationPageLocators.registration_button).click()
    WebDriverWait(create_driver, 3).until(expected_conditions.visibility_of_element_located(RegistrationPageLocators.invalid_password_message))

    assert create_driver.find_element(*RegistrationPageLocators.invalid_password_message).text == 'Некорректный пароль'
