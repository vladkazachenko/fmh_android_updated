from selenium.common.exceptions import StaleElementReferenceException

from appium.webdriver.common.appiumby import AppiumBy

from tests.pages.base_page import BasePage


class NewsPage(BasePage):
    NEWS_LIST_CONTAINER = (
        AppiumBy.ID,
        "ru.edu.qamid:id/news_list_container"
    )

    NEWS_TITLE = (
        AppiumBy.ID,
        "ru.edu.qamid:id/news_item_title_text_view"
    )

    NEWS_DATE = (
        AppiumBy.ID,
        "ru.edu.qamid:id/news_item_date_text_view"
    )

    SORT_BUTTON = (
        AppiumBy.ID,
        "ru.edu.qamid:id/news_sort_button"
    )

    FILTER_BUTTON = (
        AppiumBy.ID,
        "ru.edu.qamid:id/news_filter_button"
    )

    CONTROL_PANEL_BUTTON = (
        AppiumBy.ID,
        "ru.edu.qamid:id/news_edit_button"
    )

    def is_news_page_opened(self):
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

            for title in news_titles:
                try:
                    if title.is_displayed():
                        return True

                except StaleElementReferenceException:
                    continue

            return False

        return self.wait.until(
            visible_news_exists
        )

    def get_visible_news_titles(self):
        news_titles = self.driver.find_elements(
            *self.NEWS_TITLE
        )

        visible_titles = []

        for title in news_titles:
            try:
                if title.is_displayed():
                    visible_titles.append(
                        title.get_attribute("text")
                    )

            except StaleElementReferenceException:
                continue

        return visible_titles

    def get_visible_news_dates(self):
        news_dates = self.driver.find_elements(
            *self.NEWS_DATE
        )

        visible_dates = []

        for date in news_dates:
            try:
                if date.is_displayed():
                    visible_dates.append(
                        date.get_attribute("text").strip()
                    )

            except StaleElementReferenceException:
                continue

        return visible_dates

    def sort_news(self):
        self.click(
            self.SORT_BUTTON
        )

    def is_news_order_changed(self, titles_before):
        def order_changed(driver):
            news_titles = driver.find_elements(
                *self.NEWS_TITLE
            )

            titles_after = []

            for title in news_titles:
                try:
                    if title.is_displayed():
                        titles_after.append(
                            title.get_attribute("text")
                        )

                except StaleElementReferenceException:
                    continue

            return (
                len(titles_after) > 0
                and titles_after != titles_before
            )

        return self.wait.until(
            order_changed
        )

    def open_filter(self):
        self.click(
            self.FILTER_BUTTON
        )

    def open_control_panel(self):
        self.click(
            self.CONTROL_PANEL_BUTTON
        )