from datetime import datetime

import allure

from tests.pages.login_page import LoginPage
from tests.pages.main_page import MainPage
from tests.pages.news_page import NewsPage
from tests.pages.control_panel_page import ControlPanelPage
from tests.pages.create_edit_news_page import CreateEditNewsPage


@allure.epic("Мобильный хоспис")
@allure.feature("Управление новостями")
@allure.title("TC-052 Подтверждение удаления новости")
@allure.description(
    "Проверка удаления выбранной новости "
    "после подтверждения удаления кнопкой OK."
)
def test_confirm_news_deletion(driver):
    login_page = LoginPage(driver)
    main_page = MainPage(driver)
    news_page = NewsPage(driver)
    control_panel_page = ControlPanelPage(driver)
    create_edit_news_page = CreateEditNewsPage(driver)

    timestamp = datetime.now().strftime(
        "%d%m%Y_%H%M%S_%f"
    )

    title = (
        "Удаление "
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
        "Создать новость для последующего удаления"
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
            "Новость для проверки удаления"
        )

        create_edit_news_page.save_news()

    with allure.step(
        "Открыть окно подтверждения удаления созданной новости"
    ):
        control_panel_page.open_delete_confirmation(
            title
        )

    with allure.step(
        "Проверить сообщение подтверждения удаления"
    ):
        assert (
            control_panel_page.get_delete_confirmation_message()
            == (
                "Are you sure you want to permanently delete "
                "the document? These changes cannot be reversed "
                "in the future."
            )
        )

    with allure.step(
        "Подтвердить удаление кнопкой OK"
    ):
        control_panel_page.confirm_delete()

    with allure.step(
        "Проверить удаление новости из списка"
    ):
        assert control_panel_page.is_news_absent(
            title
        )