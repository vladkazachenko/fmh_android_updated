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
