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
