import time

from selenium.webdriver.common.by import By

def test_constructor_transition_to_rolls_success(driver_open_main_page):
    driver_open_main_page.find_element(By.XPATH, "html/body/div/div/main/section/div/div/span[text()='Соусы']").click()
    driver_open_main_page.find_element(By.XPATH, "html/body/div/div/main/section/div/div/span[text()='Булки']").click()
    time.sleep(1)

    scroll_container = driver_open_main_page.find_element(By.CLASS_NAME, "BurgerIngredients_ingredients__menuContainer__Xu3Mo")
    rolls_title = driver_open_main_page.find_element(By.XPATH, "//h2[text()='Булки']")

    pos = driver_open_main_page.execute_script("return arguments[1].getBoundingClientRect().top - arguments[0].getBoundingClientRect().top;",scroll_container, rolls_title)
    assert int(pos) == 0
    driver_open_main_page.quit()

def test_constructor_transition_to_souse_success(driver_open_main_page):
    driver_open_main_page.find_element(By.XPATH, "html/body/div/div/main/section/div/div/span[text()='Соусы']").click()
    time.sleep(1)

    scroll_container = driver_open_main_page.find_element(By.CLASS_NAME, "BurgerIngredients_ingredients__menuContainer__Xu3Mo")
    souse_title = driver_open_main_page.find_element(By.XPATH, "//h2[text()='Соусы']")

    pos = driver_open_main_page.execute_script("return arguments[1].getBoundingClientRect().top - arguments[0].getBoundingClientRect().top;",scroll_container, souse_title)
    assert int(pos) == 0
    driver_open_main_page.quit()

def test_constructor_transition_to_toppings_success(driver_open_main_page):
    driver_open_main_page.find_element(By.XPATH, "html/body/div/div/main/section/div/div/span[text()='Начинки']").click()
    time.sleep(1)

    scroll_container = driver_open_main_page.find_element(By.CLASS_NAME, "BurgerIngredients_ingredients__menuContainer__Xu3Mo")
    toppings_title = driver_open_main_page.find_element(By.XPATH, "//h2[text()='Начинки']")

    pos = driver_open_main_page.execute_script("return arguments[1].getBoundingClientRect().top - arguments[0].getBoundingClientRect().top;",scroll_container, toppings_title)
    assert int(pos) == 0
    driver_open_main_page.quit()