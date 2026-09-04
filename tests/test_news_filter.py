from datetime import datetime

import allure

from tests.pages.login_page import LoginPage
from tests.pages.main_page import MainPage
from tests.pages.news_page import NewsPage
from tests.pages.filter_news_page import FilterNewsPage
from tests.pages.control_panel_page import ControlPanelPage
from tests.pages.create_edit_news_page import CreateEditNewsPage


def create_news_for_filter(
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
@allure.feature("Фильтрация новостей")
@allure.title("TC-027 Фильтрация новостей")
@allure.description(
    "Проверка отображения новостей, соответствующих "
    "выбранному периоду публикации."
)
def test_filter_news_by_date(driver):
    login_page = LoginPage(driver)
    main_page = MainPage(driver)
    news_page = NewsPage(driver)
    filter_news_page = FilterNewsPage(driver)
    control_panel_page = ControlPanelPage(driver)
    create_edit_news_page = CreateEditNewsPage(driver)

    timestamp = datetime.now().strftime(
        "%d%m%Y_%H%M%S_%f"
    )

    title = (
        "Фильтр по дате "
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

        assert (
            control_panel_page.is_control_panel_opened()
        )

    with allure.step(
        "Создать новость с текущей датой публикации"
    ):
        create_news_for_filter(
            control_panel_page,
            create_edit_news_page,
            title,
            "Новость для проверки фильтрации по дате"
        )

    with allure.step(
        "Перейти из Control Panel в обычный раздел News"
    ):
        control_panel_page.open_news_from_menu()

    with allure.step(
        "Проверить, что открыт именно обычный раздел News"
    ):
        assert news_page.is_news_page_opened()

    with allure.step(
        "Открыть фильтр обычного раздела News"
    ):
        news_page.open_filter()

    with allure.step(
        "Установить текущую дату как начало периода"
    ):
        start_date = (
            filter_news_page.select_current_start_date()
        )

    with allure.step(
        "Установить текущую дату как конец периода"
    ):
        end_date = (
            filter_news_page.select_current_end_date()
        )

    with allure.step(
        "Проверить совпадение начала и конца периода"
    ):
        assert start_date == end_date

    with allure.step("Применить фильтр"):
        filter_news_page.apply_filter()

    with allure.step(
        "Проверить возврат именно в обычный раздел News"
    ):
        assert news_page.is_news_page_opened()

    with allure.step(
        "Получить даты отображаемых новостей"
    ):
        dates_after_filter = (
            news_page.get_visible_news_dates()
        )

    with allure.step(
        "Проверить результат фильтрации по периоду"
    ):
        assert len(dates_after_filter) > 0, (
            "После фильтрации список новостей пуст"
        )

        assert all(
            date == start_date
            for date in dates_after_filter
        ), (
            f"Ожидались новости с датой {start_date}, "
            f"получены даты: {dates_after_filter}"
        )


@allure.epic("Мобильный хоспис")
@allure.feature("Фильтрация новостей")
@allure.title("TC-028 Отмена фильтрации новостей")
@allure.description(
    "Проверка закрытия формы фильтрации "
    "после изменения параметров и нажатия CANCEL."
)
def test_cancel_news_filter(driver):
    login_page = LoginPage(driver)
    main_page = MainPage(driver)
    news_page = NewsPage(driver)
    filter_news_page = FilterNewsPage(driver)

    with allure.step("Авторизоваться в приложении"):
        login_page.login(
            "login2",
            "password2"
        )

    with allure.step(
        "Перейти в обычный раздел News"
    ):
        main_page.open_news()

        assert news_page.is_news_page_opened()

    with allure.step(
        "Открыть форму фильтрации"
    ):
        news_page.open_filter()

        assert filter_news_page.is_filter_opened()

    with allure.step(
        "Изменить параметр фильтрации"
    ):
        filter_news_page.select_category(
            "Объявление"
        )

    with allure.step(
        "Нажать CANCEL"
    ):
        filter_news_page.cancel_filter()

    with allure.step(
        "Проверить, что форма фильтрации закрылась "
        "и открыт раздел News"
    ):
        assert news_page.is_news_page_opened()