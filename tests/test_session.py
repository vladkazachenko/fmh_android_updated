import allure

from tests.pages.login_page import LoginPage
from tests.pages.main_page import MainPage


@allure.epic("Мобильный хоспис")
@allure.feature("Сессия пользователя")
@allure.title("TC-007 Сохранение сессии после перезапуска приложения")
@allure.description(
    "Проверка сохранения авторизованной сессии пользователя "
    "после закрытия и повторного запуска приложения."
)
def test_session_is_saved_after_app_restart(driver):
    login_page = LoginPage(driver)
    main_page = MainPage(driver)

    with allure.step("Авторизоваться в приложении"):
        login_page.login(
            "login2",
            "password2"
        )

    with allure.step("Проверить открытие главного экрана"):
        assert main_page.is_main_page_opened()

    with allure.step("Закрыть и повторно запустить приложение"):
        main_page.restart_app()

    with allure.step(
        "Проверить сохранение сессии и открытие главного экрана"
    ):
        assert main_page.is_main_page_opened()


@allure.epic("Мобильный хоспис")
@allure.feature("Сессия пользователя")
@allure.title("TC-008 Выход из аккаунта")
@allure.description(
    "Проверка выхода авторизованного пользователя "
    "из приложения."
)
def test_log_out(driver):
    login_page = LoginPage(driver)
    main_page = MainPage(driver)

    with allure.step("Авторизоваться в приложении"):
        login_page.login(
            "login2",
            "password2"
        )

    with allure.step("Проверить открытие главного экрана"):
        assert main_page.is_main_page_opened()

    with allure.step("Выйти из аккаунта"):
        main_page.log_out()

    with allure.step(
        "Проверить открытие экрана авторизации после выхода"
    ):
        assert login_page.is_login_page_opened()