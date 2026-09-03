from datetime import datetime

import allure

from tests.pages.login_page import LoginPage
from tests.pages.main_page import MainPage
from tests.pages.news_page import NewsPage
from tests.pages.control_panel_page import ControlPanelPage
from tests.pages.create_edit_news_page import CreateEditNewsPage


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


@allure.epic("Мобильный хоспис")
@allure.feature("Новости")
@allure.title("TC-043 Открытие формы редактирования новости")
@allure.description(
    "Проверка открытия формы редактирования "
    "для выбранной новости."
)
def test_open_news_for_edit(driver):
    login_page = LoginPage(driver)
    main_page = MainPage(driver)
    news_page = NewsPage(driver)
    control_panel_page = ControlPanelPage(driver)
    create_edit_news_page = CreateEditNewsPage(driver)

    unique_title = (
        "Редактирование "
        + datetime.now().strftime("%d%m%Y_%H%M%S")
    )

    description = (
        "Новость для проверки открытия формы редактирования"
    )

    with allure.step("Авторизоваться в приложении"):
        login_page.login("login2", "password2")

    with allure.step("Перейти в раздел News"):
        main_page.open_news()

    with allure.step("Открыть Control Panel"):
        news_page.open_control_panel()

    with allure.step("Создать новость для последующего редактирования"):
        control_panel_page.open_create_news_form()
        create_edit_news_page.select_category("Объявление")
        create_edit_news_page.enter_title(unique_title)
        create_edit_news_page.select_current_date()
        create_edit_news_page.select_current_time()
        create_edit_news_page.enter_description(description)
        create_edit_news_page.save_news()

    with allure.step("Открыть созданную новость для редактирования"):
        control_panel_page.open_news_for_edit(unique_title)

    with allure.step(
        "Проверить, что открыта форма редактирования выбранной новости"
    ):
        assert create_edit_news_page.is_news_opened_for_edit(
            unique_title
        )


@allure.epic("Мобильный хоспис")
@allure.feature("Новости")
@allure.title("TC-049 Сохранение изменений")
@allure.description(
    "Проверка сохранения измененного заголовка новости "
    "после редактирования."
)
def test_save_edited_news(driver):
    login_page = LoginPage(driver)
    main_page = MainPage(driver)
    news_page = NewsPage(driver)
    control_panel_page = ControlPanelPage(driver)
    create_edit_news_page = CreateEditNewsPage(driver)

    timestamp = datetime.now().strftime("%d%m%Y_%H%M%S")

    original_title = (
        "До редактирования "
        + timestamp
    )

    edited_title = (
        "После редактирования "
        + timestamp
    )

    description = (
        "Новость для проверки сохранения изменений"
    )

    with allure.step("Авторизоваться в приложении"):
        login_page.login("login2", "password2")

    with allure.step("Перейти в раздел News"):
        main_page.open_news()

    with allure.step("Открыть Control Panel"):
        news_page.open_control_panel()

    with allure.step("Создать новость для редактирования"):
        control_panel_page.open_create_news_form()
        create_edit_news_page.select_category("Объявление")
        create_edit_news_page.enter_title(original_title)
        create_edit_news_page.select_current_date()
        create_edit_news_page.select_current_time()
        create_edit_news_page.enter_description(description)
        create_edit_news_page.save_news()

    with allure.step("Открыть созданную новость для редактирования"):
        control_panel_page.open_news_for_edit(original_title)

    with allure.step("Изменить заголовок новости"):
        create_edit_news_page.enter_title(edited_title)

    with allure.step("Сохранить изменения"):
        create_edit_news_page.save_news()

    with allure.step("Проверить отображение измененного заголовка"):
        assert control_panel_page.is_news_present(edited_title)


@allure.epic("Мобильный хоспис")
@allure.feature("Новости")
@allure.title("TC-055 Сохранение изменений при редактировании новости")
@allure.description(
    "Проверка сохранения измененных данных новости "
    "после повторного открытия формы редактирования."
)
def test_saved_changes_after_reopening(driver):
    login_page = LoginPage(driver)
    main_page = MainPage(driver)
    news_page = NewsPage(driver)
    control_panel_page = ControlPanelPage(driver)
    create_edit_news_page = CreateEditNewsPage(driver)

    timestamp = datetime.now().strftime("%d%m%Y_%H%M%S")

    original_title = (
        "До сохранения "
        + timestamp
    )

    edited_title = (
        "После сохранения "
        + timestamp
    )

    original_description = (
        "Исходное описание новости"
    )

    edited_description = (
        "Измененное описание новости"
    )

    with allure.step("Авторизоваться в приложении"):
        login_page.login("login2", "password2")

    with allure.step("Перейти в раздел News"):
        main_page.open_news()

    with allure.step("Открыть Control Panel"):
        news_page.open_control_panel()

    with allure.step("Создать новость для редактирования"):
        control_panel_page.open_create_news_form()
        create_edit_news_page.select_category("Объявление")
        create_edit_news_page.enter_title(original_title)
        create_edit_news_page.select_current_date()
        create_edit_news_page.select_current_time()
        create_edit_news_page.enter_description(
            original_description
        )
        create_edit_news_page.save_news()

    with allure.step("Открыть созданную новость для редактирования"):
        control_panel_page.open_news_for_edit(original_title)

    with allure.step("Изменить заголовок новости"):
        create_edit_news_page.enter_title(edited_title)

    with allure.step("Изменить описание новости"):
        create_edit_news_page.enter_description(
            edited_description
        )

    with allure.step("Сохранить изменения"):
        create_edit_news_page.save_news()

    with allure.step(
        "Повторно открыть измененную новость для редактирования"
    ):
        control_panel_page.open_news_for_edit(edited_title)

    with allure.step(
        "Проверить сохранение заголовка и описания после повторного открытия"
    ):
        assert create_edit_news_page.are_news_changes_saved(
            edited_title,
            edited_description
        )