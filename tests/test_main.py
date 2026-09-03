import allure

from tests.pages.login_page import LoginPage
from tests.pages.main_page import MainPage
from tests.pages.news_page import NewsPage


@allure.epic("Мобильный хоспис")
@allure.feature("Главный экран")
@allure.title("TC-009 Отображение новостей на главном экране")
@allure.description(
    "Проверка отображения списка новостей "
    "на главном экране после авторизации."
)
def test_news_are_displayed_on_main_page(driver):
    login_page = LoginPage(driver)
    main_page = MainPage(driver)

    with allure.step("Авторизоваться в приложении"):
        login_page.login(
            "login2",
            "password2"
        )

    with allure.step("Проверить открытие главного экрана"):
        assert main_page.is_main_page_opened()

    with allure.step(
        "Проверить отображение списка новостей на главном экране"
    ):
        assert main_page.is_news_list_displayed()


@allure.epic("Мобильный хоспис")
@allure.feature("Главный экран")
@allure.title("TC-011 Разворачивание новости")
@allure.description(
    "Проверка отображения описания новости "
    "после разворачивания карточки на главном экране."
)
def test_expand_news_on_main_page(driver):
    login_page = LoginPage(driver)
    main_page = MainPage(driver)

    with allure.step("Авторизоваться в приложении"):
        login_page.login(
            "login2",
            "password2"
        )

    with allure.step("Проверить открытие главного экрана"):
        assert main_page.is_main_page_opened()

    with allure.step("Развернуть первую новость"):
        main_page.expand_first_news()

    with allure.step(
        "Проверить отображение описания развернутой новости"
    ):
        assert main_page.is_news_description_visible()


@allure.epic("Мобильный хоспис")
@allure.feature("Главный экран")
@allure.title("TC-012 Сворачивание новости")
@allure.description(
    "Проверка скрытия описания новости "
    "после повторного нажатия на развернутую карточку."
)
def test_collapse_news_on_main_page(driver):
    login_page = LoginPage(driver)
    main_page = MainPage(driver)

    with allure.step("Авторизоваться в приложении"):
        login_page.login(
            "login2",
            "password2"
        )

    with allure.step("Проверить открытие главного экрана"):
        assert main_page.is_main_page_opened()

    with allure.step("Развернуть первую новость"):
        main_page.expand_first_news()

    with allure.step(
        "Проверить, что описание новости отображается"
    ):
        assert main_page.is_news_description_visible()

    with allure.step("Свернуть развернутую новость"):
        main_page.collapse_first_news()

    with allure.step(
        "Проверить, что описание новости перестало отображаться"
    ):
        assert main_page.is_news_description_hidden()


@allure.epic("Мобильный хоспис")
@allure.feature("Навигация")
@allure.title("TC-013 Открытие бокового меню")
@allure.description(
    "Проверка открытия главного меню приложения "
    "с пунктами Main и News."
)
def test_open_main_menu(driver):
    login_page = LoginPage(driver)
    main_page = MainPage(driver)

    with allure.step("Авторизоваться в приложении"):
        login_page.login(
            "login2",
            "password2"
        )

    with allure.step("Открыть главное меню приложения"):
        main_page.open_main_menu()

    with allure.step(
        "Проверить отображение пунктов Main и News"
    ):
        assert main_page.is_main_menu_opened()


@allure.epic("Мобильный хоспис")
@allure.feature("Навигация")
@allure.title("TC-015 Переход в раздел News")
@allure.description(
    "Проверка перехода в раздел News "
    "через главное меню приложения."
)
def test_open_news_from_main_menu(driver):
    login_page = LoginPage(driver)
    main_page = MainPage(driver)
    news_page = NewsPage(driver)

    with allure.step("Авторизоваться в приложении"):
        login_page.login(
            "login2",
            "password2"
        )

    with allure.step("Открыть главное меню приложения"):
        main_page.open_main_menu()

    with allure.step("Выбрать пункт News"):
        main_page.open_news_from_menu()

    with allure.step("Проверить открытие раздела News"):
        assert news_page.is_news_page_opened()