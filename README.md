фикстуры: 
generated_valid_password - генерация валидного пароля
generated_invalid_password - генерация невалидного пароля
generated_login - генерация логина
driver_open_registration - открытие страницы регистрации 
driver_open_main_page - открытие главной страницы
driver_authorization - авторизация с использованием данных из генераторов пароля и логина
driver_open_personal_account - открытие страницы личного кабинета

тесты: 
test_01_registration - тесты на регистрацию (test_registration_success - с использованием валидного пароля, 
                                             test_registration_invalid_password_false - с использованием невалидного пароля)
                                             
test_02_authorization - тесты на переход к странице авторизации (test_authorization_from_main_page_success - вход по кнопке «Войти в аккаунт» на главной,
                                                                 test_authorization_from_personal_account_success - вход через кнопку «Личный кабинет»,
                                                                 test_authorization_from_registration_form_success - вход через кнопку в форме регистрации,
                                                                 test_authorization_from_password_recovery_success - вход через кнопку в форме восстановления пароля)
                                                                 
test_03_transition_in_personal_account - переход в личный кабинет

test_04_exit_from_account - выход из аккаунта

test_05_transition_to_main_page - переход из личного кабинета в конструктор (test_transition_to_main_page_by_logo - через логотип,
                                                                             test_transition_to_main_page_by_constructor - через кнопку "Конструктор")
                                                                             
test_06_constructor - переходы в разделе "Конструктор" (test_constructor_transition_to_rolls_success - переход к разделу "Булки",
                                                        test_constructor_transition_to_souse_success - переход к разделу "Соусы"
                                                        test_constructor_transition_to_toppings_success - переход к разделу "Начинки")
