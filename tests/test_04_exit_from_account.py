import url.url

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.all_locators import HomePageLocators, PersonalAccountLocators


def test_exit_from_account(authorization):
    authorization.find_element(*HomePageLocators.account_link).click()
    WebDriverWait(authorization, 3).until(expected_conditions.visibility_of_element_located(PersonalAccountLocators.exit_button))

    authorization.find_element(*PersonalAccountLocators.exit_button).click()
    WebDriverWait(authorization, 3).until(expected_conditions.visibility_of_element_located(HomePageLocators.login_account_button))

    assert '/login' in authorization.current_url
