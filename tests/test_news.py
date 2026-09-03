import allure

from tests.pages.login_page import LoginPage
from tests.pages.main_page import MainPage
from tests.pages.news_page import NewsPage
from tests.pages.control_panel_page import ControlPanelPage
from tests.pages.create_edit_news_page import CreateEditNewsPage
from datetime import datetime


@allure.epic("Мобильный хоспис")
@allure.feature("Новости")
@allure.title("TC-033 Открытие формы создания новости")
@allure.description(
    "Проверка открытия формы создания новой новости "
    "из панели управления Control Panel."
)
def test_open_create_news_form(driver):
    login_page = LoginPage(driver)
    main_page = MainPage(driver)
    news_page = NewsPage(driver)
    control_panel_page = ControlPanelPage(driver)
    create_edit_news_page = CreateEditNewsPage(driver)

    with allure.step("Авторизоваться в приложении"):
        login_page.login("login2", "password2")

    with allure.step("Перейти с главного экрана в раздел News"):
        main_page.open_news()

    with allure.step("Открыть Control Panel"):
        news_page.open_control_panel()

    with allure.step("Открыть форму создания новости"):
        control_panel_page.open_create_news_form()

    with allure.step("Проверить открытие формы создания новости"):
        assert create_edit_news_page.is_create_news_form_opened()


@allure.epic("Мобильный хоспис")
@allure.feature("Новости")
@allure.title("TC-041 Сохранение новой новости")
@allure.description(
    "Проверка создания и сохранения новой новости "
    "с корректно заполненными обязательными полями."
)
def test_create_news(driver):
    login_page = LoginPage(driver)
    main_page = MainPage(driver)
    news_page = NewsPage(driver)
    control_panel_page = ControlPanelPage(driver)
    create_edit_news_page = CreateEditNewsPage(driver)

    unique_title = (
        "Автотест "
        + datetime.now().strftime("%d%m%Y_%H%M%S")
    )

    description = "Новость создана автоматизированным тестом"

    with allure.step("Авторизоваться в приложении"):
        login_page.login("login2", "password2")

    with allure.step("Перейти в раздел News"):
        main_page.open_news()

    with allure.step("Открыть Control Panel"):
        news_page.open_control_panel()

    with allure.step("Открыть форму создания новости"):
        control_panel_page.open_create_news_form()

    with allure.step("Выбрать категорию новости"):
        create_edit_news_page.select_category("Объявление")

    with allure.step("Заполнить заголовок новости"):
        create_edit_news_page.enter_title(unique_title)

    with allure.step("Выбрать текущую дату публикации"):
        create_edit_news_page.select_current_date()

    with allure.step("Выбрать текущее время публикации"):
        create_edit_news_page.select_current_time()

    with allure.step("Заполнить описание новости"):
        create_edit_news_page.enter_description(description)

    with allure.step("Сохранить новость"):
        create_edit_news_page.save_news()

    with allure.step("Проверить отображение созданной новости"):
        assert control_panel_page.is_news_present(unique_title)