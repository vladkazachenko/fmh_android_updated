from datetime import datetime

import allure

from tests.pages.login_page import LoginPage
from tests.pages.main_page import MainPage
from tests.pages.news_page import NewsPage
from tests.pages.control_panel_page import ControlPanelPage
from tests.pages.create_edit_news_page import CreateEditNewsPage


@allure.epic("Мобильный хоспис")
@allure.feature("Создание новости")
@allure.title("TC-035 Создание новости без категории")
@allure.description(
    "Проверка невозможности создания новости "
    "без заполнения обязательного поля Category."
)
def test_create_news_without_category(driver):
    login_page = LoginPage(driver)
    main_page = MainPage(driver)
    news_page = NewsPage(driver)
    control_panel_page = ControlPanelPage(driver)
    create_edit_news_page = CreateEditNewsPage(driver)

    timestamp = datetime.now().strftime(
        "%d%m%Y_%H%M%S_%f"
    )

    title = (
        "Без категории "
        + timestamp
    )

    with allure.step(
        "Авторизоваться в приложении"
    ):
        login_page.login(
            "login2",
            "password2"
        )

    with allure.step(
        "Перейти в раздел News"
    ):
        main_page.open_news()

    with allure.step(
        "Открыть Control Panel"
    ):
        news_page.open_control_panel()

        assert (
            control_panel_page.is_control_panel_opened()
        )

    with allure.step(
        "Открыть форму создания новости"
    ):
        control_panel_page.open_create_news_form()

        assert (
            create_edit_news_page
            .is_create_news_form_opened()
        )

    with allure.step(
        "Оставить Category пустой "
        "и заполнить остальные обязательные поля"
    ):
        create_edit_news_page.enter_title(
            title
        )

        create_edit_news_page.select_current_date()

        create_edit_news_page.select_current_time()

        create_edit_news_page.enter_description(
            "Проверка обязательности поля Category"
        )

    with allure.step(
        "Нажать SAVE"
    ):
        create_edit_news_page.save_news()

    with allure.step(
        "Проверить предупреждение у поля Category"
    ):
        assert (
            create_edit_news_page
            .is_category_warning_visible()
        )

    with allure.step(
        "Проверить, что новость не была создана"
    ):
        assert (
            create_edit_news_page
            .is_create_news_form_opened()
        )