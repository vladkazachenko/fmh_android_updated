from selenium.common.exceptions import StaleElementReferenceException

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

    MAIN_MENU_BUTTON = (
        AppiumBy.ID,
        "ru.edu.qamid:id/main_menu_image_button"
    )

    NEWS_MENU_ITEM = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="News"]'
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

    def open_news_from_menu(self):
        self.click(
            self.MAIN_MENU_BUTTON
        )

        self.click(
            self.NEWS_MENU_ITEM
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

    def _get_news_action_locator(
        self,
        title,
        action_resource_id
    ):
        title_literal = self._xpath_literal(
            title
        )

        return (
            AppiumBy.XPATH,
            '//*[@resource-id='
            '"ru.edu.qamid:id/news_item_material_card_view"]'
            '[.//*[@resource-id='
            '"ru.edu.qamid:id/news_item_title_text_view" '
            f'and @text={title_literal}]]'
            '//*[@resource-id='
            f'"{action_resource_id}"]'
        )

    def _scroll_to_news_title(self, title):
        return self.find_visible(
            self._get_news_title_locator(
                title
            )
        )

    def _scroll_to_news_action(
        self,
        title,
        action_locator
    ):
        self._scroll_to_news_title(
            title
        )

        news_list = self.find_visible(
            self.NEWS_LIST
        )

        for _ in range(4):
            action_elements = (
                self.driver.find_elements(
                    *action_locator
                )
            )

            for action_element in action_elements:
                try:
                    if (
                        action_element.is_displayed()
                        and action_element.is_enabled()
                    ):
                        return action_element

                except StaleElementReferenceException:
                    continue

            self.driver.execute_script(
                "mobile: scrollGesture",
                {
                    "elementId": news_list.id,
                    "direction": "down",
                    "percent": 0.2
                }
            )

        return self.find_clickable(
            action_locator
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
            self._get_news_action_locator(
                title,
                "ru.edu.qamid:id/news_item_edit_image_view"
            )
        )

        edit_element = (
            self._scroll_to_news_action(
                title,
                edit_button
            )
        )

        edit_element.click()

    def open_delete_confirmation(self, title):
        delete_button = (
            self._get_news_action_locator(
                title,
                "ru.edu.qamid:id/news_item_delete_image_view"
            )
        )

        delete_element = (
            self._scroll_to_news_action(
                title,
                delete_button
            )
        )

        delete_element.click()

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