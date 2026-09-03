from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC

from tests.pages.base_page import BasePage


class MainPage(BasePage):
    NEWS_LIST_CONTAINER = (
        AppiumBy.ID,
        "ru.edu.qamid:id/main_news_list_container"
    )

    NEWS_CARD = (
        AppiumBy.ID,
        "ru.edu.qamid:id/news_item_material_card_view"
    )

    NEWS_TITLE = (
        AppiumBy.ID,
        "ru.edu.qamid:id/news_item_title_text_view"
    )

    NEWS_DESCRIPTION = (
        AppiumBy.ID,
        "ru.edu.qamid:id/news_item_description_text_view"
    )

    ALL_NEWS_BUTTON = (
        AppiumBy.ID,
        "ru.edu.qamid:id/all_news_text_view"
    )

    OUR_MISSION_BUTTON = (
        AppiumBy.ID,
        "ru.edu.qamid:id/our_mission_image_button"
    )

    AUTHORIZATION_BUTTON = (
        AppiumBy.ID,
        "ru.edu.qamid:id/authorization_image_button"
    )

    MAIN_MENU_BUTTON = (
        AppiumBy.ID,
        "ru.edu.qamid:id/main_menu_image_button"
    )

    MAIN_MENU_ITEM = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="Main"]'
    )

    NEWS_MENU_ITEM = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="News"]'
    )

    LOG_OUT_BUTTON = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="Log out"]'
    )

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        self.expanded_news_title = None

    def is_main_page_opened(self):
        return self.find_visible(
            self.NEWS_LIST_CONTAINER
        ).is_displayed()

    def is_news_list_displayed(self):
        self.find_visible(
            self.NEWS_LIST_CONTAINER
        )

        def visible_news_exists(driver):
            news_titles = driver.find_elements(
                *self.NEWS_TITLE
            )

            return any(
                title.is_displayed()
                for title in news_titles
            )

        return self.wait.until(
            visible_news_exists
        )

    def _xpath_literal(self, text):
        if '"' not in text:
            return f'"{text}"'

        if "'" not in text:
            return f"'{text}'"

        parts = text.split('"')

        return "concat(" + ', \'"\', '.join(
            f'"{part}"'
            for part in parts
        ) + ")"

    def _get_news_title_by_text(self, title):
        title_literal = self._xpath_literal(
            title
        )

        news_title = (
            AppiumBy.XPATH,
            '//*[@resource-id='
            '"ru.edu.qamid:id/news_item_title_text_view" '
            f'and @text={title_literal}]'
        )

        return self.find_visible(
            news_title
        )

    def _get_description_locator(self):
        if self.expanded_news_title is None:
            raise AssertionError(
                "Новость не была развернута"
            )

        title_literal = self._xpath_literal(
            self.expanded_news_title
        )

        return (
            AppiumBy.XPATH,
            '//*[@resource-id='
            '"ru.edu.qamid:id/news_item_material_card_view"]'
            '[.//*[@resource-id='
            '"ru.edu.qamid:id/news_item_title_text_view" '
            f'and @text={title_literal}]]'
            '//*[@resource-id='
            '"ru.edu.qamid:id/news_item_description_text_view"]'
        )

    def expand_first_news(self):
        news_titles = self.driver.find_elements(
            *self.NEWS_TITLE
        )

        for title_element in news_titles:
            if title_element.is_displayed():
                self.expanded_news_title = (
                    title_element.get_attribute("text")
                )

                title_element.click()
                return

        raise AssertionError(
            "Не найдена видимая новость"
        )

    def collapse_first_news(self):
        if self.expanded_news_title is None:
            raise AssertionError(
                "Перед сворачиванием новость не была развернута"
            )

        title_element = self._get_news_title_by_text(
            self.expanded_news_title
        )

        title_element.click()

    def is_news_description_visible(self):
        description = self._get_description_locator()

        return self.find_visible(
            description
        ).is_displayed()

    def is_news_description_hidden(self):
        description = self._get_description_locator()

        return self.wait.until(
            EC.invisibility_of_element_located(
                description
            )
        )

    def open_main_menu(self):
        self.click(
            self.MAIN_MENU_BUTTON
        )

    def is_main_menu_opened(self):
        main_item = self.find_visible(
            self.MAIN_MENU_ITEM
        )

        news_item = self.find_visible(
            self.NEWS_MENU_ITEM
        )

        return (
            main_item.is_displayed()
            and news_item.is_displayed()
        )

    def open_news_from_menu(self):
        self.click(
            self.NEWS_MENU_ITEM
        )

    def open_news(self):
        self.click(
            self.ALL_NEWS_BUTTON
        )

    def open_our_mission(self):
        self.click(
            self.OUR_MISSION_BUTTON
        )

    def restart_app(self):
        self.driver.terminate_app(
            "ru.edu.qamid"
        )

        self.driver.activate_app(
            "ru.edu.qamid"
        )

    def log_out(self):
        self.click(
            self.AUTHORIZATION_BUTTON
        )

        self.click(
            self.LOG_OUT_BUTTON
        )