from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.all_locators import LoginPageTransitionLocators, PersonalAccountLocators


def test_transition_in_personal_account(authorization):
    authorization.find_element(*LoginPageTransitionLocators.transition_from_personal_account).click()
    WebDriverWait(authorization, 3).until(expected_conditions.visibility_of_element_located(PersonalAccountLocators.save_button))

    assert '/profile' in authorization.current_url
