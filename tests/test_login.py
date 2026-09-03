import allure

from tests.pages.login_page import LoginPage
from tests.pages.main_page import MainPage


@allure.epic("Мобильный хоспис")
@allure.feature("Авторизация")
@allure.title("TC-001 Успешная авторизация")
@allure.description(
    "Проверка успешной авторизации пользователя "
    "с валидными логином и паролем."
)
def test_successful_login(driver):
    login_page = LoginPage(driver)
    main_page = MainPage(driver)

    with allure.step("Ввести валидные логин и пароль"):
        login_page.login("login2", "password2")

    with allure.step("Проверить открытие главной страницы"):
        assert main_page.is_main_page_opened()


@allure.epic("Мобильный хоспис")
@allure.feature("Авторизация")
@allure.title("TC-002 Авторизация с неверным логином")
@allure.description(
    "Проверка сообщения об ошибке при попытке авторизации "
    "с неверным логином и валидным паролем."
)
def test_login_with_wrong_login(driver):
    login_page = LoginPage(driver)

    with allure.step("Ввести неверный логин и валидный пароль"):
        login_page.login("wrong_login", "password2")

    with allure.step("Проверить сообщение об ошибке"):
        actual_message = login_page.get_toast_text(timeout=30)

        assert actual_message == "Wrong login or password", (
            f"Ожидалось сообщение 'Wrong login or password', "
            f"но получено: '{actual_message}'"
        )


@allure.epic("Мобильный хоспис")
@allure.feature("Авторизация")
@allure.title("TC-003 Авторизация с неверным паролем")
@allure.description(
    "Проверка сообщения об ошибке при попытке авторизации "
    "с валидным логином и неверным паролем."
)
def test_login_with_wrong_password(driver):
    login_page = LoginPage(driver)

    with allure.step("Ввести валидный логин и неверный пароль"):
        login_page.login("login2", "wrong_password")

    with allure.step("Проверить сообщение об ошибке"):
        actual_message = login_page.get_toast_text(timeout=30)

        assert actual_message == "Wrong login or password", (
            f"Ожидалось сообщение 'Wrong login or password', "
            f"но получено: '{actual_message}'"
        )


@allure.epic("Мобильный хоспис")
@allure.feature("Авторизация")
@allure.title("TC-004 Авторизация с пустыми полями")
@allure.description(
    "Проверка сообщения об ошибке при попытке авторизации "
    "с пустыми полями логина и пароля."
)
def test_login_with_empty_fields(driver):
    login_page = LoginPage(driver)

    with allure.step("Нажать кнопку входа, не заполняя логин и пароль"):
        login_page.click_sign_in()

    with allure.step("Проверить сообщение об ошибке"):
        assert (
            login_page.get_empty_fields_error()
            == "Login and password cannot be empty"
        )
