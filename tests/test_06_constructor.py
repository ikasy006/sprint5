import time

import url.url

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.all_locators import HomePageLocators

def test_constructor_transition_to_rolls_success(authorization):
    authorization.find_element(*HomePageLocators.souse).click()
    authorization.find_element(*HomePageLocators.rolls).click()
    button = authorization.find_element(*HomePageLocators.rolls)

    assert "tab_tab_type_current__2BEPc" in button.get_attribute("class")

def test_constructor_transition_to_souse_success(authorization):
    authorization.find_element(*HomePageLocators.souse).click()
    button = authorization.find_element(*HomePageLocators.souse)

    assert "tab_tab_type_current__2BEPc" in button.get_attribute("class")

def  test_constructor_transition_to_toppings_success(authorization):
    authorization.find_element(*HomePageLocators.toppings).click()
    button = authorization.find_element(*HomePageLocators.toppings)

    assert "tab_tab_type_current__2BEPc" in button.get_attribute("class")
