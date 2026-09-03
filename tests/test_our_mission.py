import allure

from tests.pages.login_page import LoginPage
from tests.pages.main_page import MainPage
from tests.pages.our_mission_page import OurMissionPage


@allure.epic("Мобильный хоспис")
@allure.feature("Love is all")
@allure.title("TC-016 Открытие раздела Love is all")
@allure.description(
    "Проверка перехода с главного экрана "
    "в раздел Love is all."
)
def test_open_our_mission(driver):
    login_page = LoginPage(driver)
    main_page = MainPage(driver)
    our_mission_page = OurMissionPage(driver)

    with allure.step("Авторизоваться в приложении"):
        login_page.login("login2", "password2")

    with allure.step("Открыть раздел Love is all"):
        main_page.open_our_mission()

    with allure.step("Проверить открытие раздела Love is all"):
        assert our_mission_page.is_our_mission_opened()


@allure.epic("Мобильный хоспис")
@allure.feature("Love is all")
@allure.title("TC-018 Прокрутка списка цитат")
@allure.description(
    "Проверка возможности прокрутки списка цитат "
    "в разделе Love is all."
)
def test_scroll_our_mission_quotes(driver):
    login_page = LoginPage(driver)
    main_page = MainPage(driver)
    our_mission_page = OurMissionPage(driver)

    with allure.step("Авторизоваться в приложении"):
        login_page.login("login2", "password2")

    with allure.step("Открыть раздел Love is all"):
        main_page.open_our_mission()

    with allure.step("Запомнить цитаты, видимые до прокрутки"):
        titles_before = (
            our_mission_page.get_visible_quote_titles()
        )

    with allure.step("Прокрутить список цитат вниз"):
        our_mission_page.scroll_quotes_down()

    with allure.step(
        "Проверить изменение отображаемых цитат после прокрутки"
    ):
        assert our_mission_page.is_quotes_list_scrolled(
            titles_before
        )


@allure.epic("Мобильный хоспис")
@allure.feature("Love is all")
@allure.title("TC-019 Разворачивание цитаты")
@allure.description(
    "Проверка отображения дополнительного текста "
    "после разворачивания цитаты в разделе Love is all."
)
def test_expand_our_mission_quote(driver):
    login_page = LoginPage(driver)
    main_page = MainPage(driver)
    our_mission_page = OurMissionPage(driver)

    with allure.step("Авторизоваться в приложении"):
        login_page.login("login2", "password2")

    with allure.step("Открыть раздел Love is all"):
        main_page.open_our_mission()

    with allure.step("Развернуть первую цитату"):
        our_mission_page.expand_first_quote()

    with allure.step(
        "Проверить отображение описания развернутой цитаты"
    ):
        assert our_mission_page.is_quote_description_visible()