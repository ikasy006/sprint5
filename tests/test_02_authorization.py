import url.url

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from conftest import create_driver
from url.url import Config
from locators.all_locators import LoginPageTransitionLocators, HomePageLocators, RegistrationPageLocators

# Наставник отметил, что в данных тестах мы проверяем лишь возможность перехода на страницу "/login", без учета самой авторизации.
# Однако с учетом замечания, полученного в ходе ревью, в первом тесте проверяется факт авторизации, что не проверяется в последующих,
# ибо при нажатии по различным кнопкам для входа, результат один - переход на одну и ту же страницу

class TestAuthorization:
    #проверка авторизации пользователя через главную страницу
    def test_authorization_from_main_page_success(self, create_driver, generated_login, generated_valid_password):
        create_driver.get(Config.BASE_URL)
        create_driver.find_element(*LoginPageTransitionLocators.transition_from_main_page).click()
        WebDriverWait(create_driver, 3).until(expected_conditions.visibility_of_all_elements_located(HomePageLocators.login_account_button))

        create_driver.find_element(*RegistrationPageLocators.email_input).send_keys(generated_login)
        create_driver.find_element(*RegistrationPageLocators.password_input).send_keys(generated_valid_password)

        create_driver.find_element(*HomePageLocators.login_account_button).click()
        WebDriverWait(create_driver, 3).until(expected_conditions.visibility_of_element_located(HomePageLocators.place_order))

        assert create_driver.current_url.rstrip('/') == url.url.Config.BASE_URL

    def test_authorization_from_personal_account_success(self, create_driver):
        create_driver.find_element(*LoginPageTransitionLocators.transition_from_personal_account).click()
        WebDriverWait(create_driver, 3).until(expected_conditions.visibility_of_element_located(HomePageLocators.login_account_button))

        assert '/login' in create_driver.current_url

    def test_authorization_from_registration_form_success(self, create_driver):
        create_driver.get(url.url.Config.REGISTER_URL)

        create_driver.find_element(*LoginPageTransitionLocators.transition_from_registration_page).click()
        WebDriverWait(create_driver, 3).until(expected_conditions.visibility_of_element_located(HomePageLocators.login_account_button))

        assert '/login' in create_driver.current_url

    def test_authorization_from_password_recovery_success(self, create_driver):
        create_driver.get(url.url.Config.PASSWORD_RECOVERY)

        create_driver.find_element(*LoginPageTransitionLocators.transition_from_registration_page).click()
        WebDriverWait(create_driver, 3).until(expected_conditions.visibility_of_element_located(HomePageLocators.login_account_button))

        assert '/login' in create_driver.current_url
