import url.url

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.all_locators import HomePageLocators

def test_transition_to_main_page_by_logo(personal_account):
    personal_account.find_element(*HomePageLocators.logo).click()
    WebDriverWait(personal_account, 3).until(expected_conditions.visibility_of_element_located(HomePageLocators.header))

    assert personal_account.current_url.rstrip('/') == url.url.Config.BASE_URL

def test_transition_to_main_page_by_constructor(personal_account):
    personal_account.find_element(*HomePageLocators.constructor).click()
    WebDriverWait(personal_account, 3).until(expected_conditions.visibility_of_element_located(HomePageLocators.header))

    assert personal_account.current_url.rstrip('/') == url.url.Config.BASE_URL
