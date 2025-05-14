from selenium.webdriver.common.by import By

class HomePageLocators:
    login_account_button = (By.XPATH, "//button[text()='Войти']")
    account_link = (By.XPATH, "//a[@href = '/account']")
    constructor = (By.XPATH, "//p[text()='Конструктор']")
    place_order = (By.XPATH, "//button[text()='Оформить заказ']")
    logo = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']/a")
    header = (By.XPATH, "//h1[text()='Соберите бургер']")
    souse = (By.XPATH, "//span[text()='Соусы']/parent::div")
    rolls = (By.XPATH, "//span[text()='Булки']/parent::div")
    toppings = (By.XPATH, "//span[text()='Начинки']/parent::div")


class RegistrationPageLocators:
    password_input = (By.XPATH, "//label[text() = 'Пароль']/following-sibling::input")
    email_input = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    name_input = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    registration_button = (By.XPATH, "//button[text()='Зарегистрироваться']")
    invalid_password_message = (By.CLASS_NAME, "input__error")

class LoginPageTransitionLocators:
    transition_from_main_page = (By.XPATH, "//button[text()='Войти в аккаунт']")
    transition_from_personal_account = (By.XPATH, "//p[text()='Личный Кабинет']")
    transition_from_registration_page = (By.XPATH, "//a[text()='Войти']")
    transition_from_password_recovery_success = (By.XPATH, "//a[text()='Войти']")

class PersonalAccountLocators:
    save_button = (By.XPATH, "//button[text()='Сохранить']")
    exit_button = (By.XPATH, "//button[text()='Выход']")
