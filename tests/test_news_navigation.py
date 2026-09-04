from datetime import datetime

import allure

from tests.pages.login_page import LoginPage
from tests.pages.main_page import MainPage
from tests.pages.news_page import NewsPage
from tests.pages.control_panel_page import ControlPanelPage
from tests.pages.create_edit_news_page import CreateEditNewsPage


def create_test_news(
    control_panel_page,
    create_edit_news_page,
    title,
    description
):
    control_panel_page.open_create_news_form()

    create_edit_news_page.select_category(
        "Объявление"
    )

    create_edit_news_page.enter_title(
        title
    )

    create_edit_news_page.select_current_date()

    create_edit_news_page.select_current_time()

    create_edit_news_page.enter_description(
        description
    )

    create_edit_news_page.save_news()


@allure.epic("Мобильный хоспис")
@allure.feature("Новости")
@allure.title("TC-021 Отображение списка новостей в разделе News")
@allure.description(
    "Проверка отображения списка новостей "
    "после перехода в раздел News."
)
def test_news_list_is_displayed(driver):
    login_page = LoginPage(driver)
    main_page = MainPage(driver)
    news_page = NewsPage(driver)

    with allure.step("Авторизоваться в приложении"):
        login_page.login(
            "login2",
            "password2"
        )

    with allure.step("Перейти в раздел News"):
        main_page.open_news()

    with allure.step("Проверить открытие раздела News"):
        assert news_page.is_news_page_opened()

    with allure.step(
        "Проверить отображение списка новостей"
    ):
        assert news_page.is_news_list_displayed()


@allure.epic("Мобильный хоспис")
@allure.feature("Новости")
@allure.title("TC-022 Сортировка новостей в разделе News")
@allure.description(
    "Проверка изменения порядка отображения новостей "
    "после нажатия кнопки сортировки."
)
def test_sort_news(driver):
    login_page = LoginPage(driver)
    main_page = MainPage(driver)
    news_page = NewsPage(driver)
    control_panel_page = ControlPanelPage(driver)
    create_edit_news_page = CreateEditNewsPage(driver)

    timestamp = datetime.now().strftime(
        "%d%m%Y_%H%M%S"
    )

    first_title = (
        "Сортировка 1 "
        + timestamp
    )

    second_title = (
        "Сортировка 2 "
        + timestamp
    )

    with allure.step("Авторизоваться в приложении"):
        login_page.login(
            "login2",
            "password2"
        )

    with allure.step("Перейти в раздел News"):
        main_page.open_news()

    with allure.step("Открыть Control Panel"):
        news_page.open_control_panel()

    with allure.step(
        "Создать первую новость для проверки сортировки"
    ):
        create_test_news(
            control_panel_page,
            create_edit_news_page,
            first_title,
            "Первая новость для проверки сортировки"
        )

    with allure.step(
        "Создать вторую новость для проверки сортировки"
    ):
        create_test_news(
            control_panel_page,
            create_edit_news_page,
            second_title,
            "Вторая новость для проверки сортировки"
        )

    with allure.step("Вернуться в раздел News"):
        control_panel_page.return_to_news()

    with allure.step(
        "Проверить наличие нескольких новостей"
    ):
        titles_before = (
            news_page.get_visible_news_titles()
        )

        assert len(titles_before) > 1, (
            "После создания тестовых данных "
            "в списке должно быть минимум две новости"
        )

    with allure.step("Изменить направление сортировки"):
        news_page.sort_news()

    with allure.step(
        "Проверить изменение порядка новостей после сортировки"
    ):
        assert news_page.is_news_order_changed(
            titles_before
        )


@allure.epic("Мобильный хоспис")
@allure.feature("Новости")
@allure.title("TC-029 Открытие Control Panel")
@allure.description(
    "Проверка открытия панели управления новостями "
    "из раздела News."
)
def test_open_control_panel(driver):
    login_page = LoginPage(driver)
    main_page = MainPage(driver)
    news_page = NewsPage(driver)
    control_panel_page = ControlPanelPage(driver)

    with allure.step("Авторизоваться в приложении"):
        login_page.login(
            "login2",
            "password2"
        )

    with allure.step("Перейти в раздел News"):
        main_page.open_news()

    with allure.step("Открыть Control Panel"):
        news_page.open_control_panel()

    with allure.step(
        "Проверить открытие Control Panel"
    ):
        assert control_panel_page.is_control_panel_opened()