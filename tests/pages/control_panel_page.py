from appium.webdriver.common.appiumby import AppiumBy

from tests.pages.base_page import BasePage


class ControlPanelPage(BasePage):
    NEWS_LIST = (
        AppiumBy.ID,
        "ru.edu.qamid:id/news_list_recycler_view"
    )

    ADD_NEWS_BUTTON = (
        AppiumBy.ID,
        "ru.edu.qamid:id/add_news_image_view"
    )

    DELETE_DIALOG_MESSAGE = (
        AppiumBy.ID,
        "android:id/message"
    )

    DELETE_DIALOG_OK_BUTTON = (
        AppiumBy.ID,
        "android:id/button1"
    )

    def is_control_panel_opened(self):
        return self.find_visible(
            self.NEWS_LIST
        ).is_displayed()

    def open_create_news_form(self):
        self.click(
            self.ADD_NEWS_BUTTON
        )

    def return_to_news(self):
        self.driver.back()

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

    def _get_news_title_locator(self, title):
        return (
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable('
            'new UiSelector().resourceId('
            '"ru.edu.qamid:id/news_list_recycler_view"))'
            '.scrollIntoView('
            'new UiSelector().resourceId('
            '"ru.edu.qamid:id/news_item_title_text_view")'
            f'.text("{title}"))'
        )

    def _get_news_title_xpath_locator(self, title):
        title_literal = self._xpath_literal(
            title
        )

        return (
            AppiumBy.XPATH,
            '//*[@resource-id='
            '"ru.edu.qamid:id/news_item_title_text_view" '
            f'and @text={title_literal}]'
        )

    def _scroll_to_news_title(self, title):
        return self.find_visible(
            self._get_news_title_locator(
                title
            )
        )

    def is_news_present(self, title):
        return self._scroll_to_news_title(
            title
        ).is_displayed()

    def is_news_absent(self, title):
        title_locator = (
            self._get_news_title_xpath_locator(
                title
            )
        )

        def news_disappeared(driver):
            return len(
                driver.find_elements(
                    *title_locator
                )
            ) == 0

        return self.wait.until(
            news_disappeared
        )

    def open_news_for_edit(self, title):
        edit_button = (
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable('
            'new UiSelector().resourceId('
            '"ru.edu.qamid:id/news_list_recycler_view"))'
            '.scrollIntoView('
            'new UiSelector().resourceId('
            '"ru.edu.qamid:id/news_item_title_text_view")'
            f'.text("{title}")'
            '.fromParent('
            'new UiSelector().resourceId('
            '"ru.edu.qamid:id/news_item_edit_image_view")))'
        )

        self.click(
            edit_button
        )

    def open_delete_confirmation(self, title):
        self._scroll_to_news_title(
            title
        )

        title_literal = self._xpath_literal(
            title
        )

        delete_button = (
            AppiumBy.XPATH,
            '//*[@resource-id='
            '"ru.edu.qamid:id/news_item_material_card_view"]'
            '[.//*[@resource-id='
            '"ru.edu.qamid:id/news_item_title_text_view" '
            f'and @text={title_literal}]]'
            '//*[@resource-id='
            '"ru.edu.qamid:id/news_item_delete_image_view"]'
        )

        self.click(
            delete_button
        )

    def get_delete_confirmation_message(self):
        return self.find_visible(
            self.DELETE_DIALOG_MESSAGE
        ).get_attribute(
            "text"
        )

    def confirm_delete(self):
        self.click(
            self.DELETE_DIALOG_OK_BUTTON
        )