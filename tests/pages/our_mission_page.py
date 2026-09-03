from appium.webdriver.common.appiumby import AppiumBy

from tests.pages.base_page import BasePage


class OurMissionPage(BasePage):
    TITLE = (
        AppiumBy.ID,
        "ru.edu.qamid:id/our_mission_title_text_view"
    )

    QUOTES_LIST = (
        AppiumBy.ID,
        "ru.edu.qamid:id/our_mission_item_list_recycler_view"
    )

    QUOTE_TITLE = (
        AppiumBy.ID,
        "ru.edu.qamid:id/our_mission_item_title_text_view"
    )

    QUOTE_DESCRIPTION = (
        AppiumBy.ID,
        "ru.edu.qamid:id/our_mission_item_description_text_view"
    )

    EXPAND_BUTTON = (
        AppiumBy.ID,
        "ru.edu.qamid:id/our_mission_item_open_card_image_button"
    )

    def is_our_mission_opened(self):
        return self.find_visible(
            self.TITLE
        ).is_displayed()

    def is_quotes_list_visible(self):
        return self.find_visible(
            self.QUOTES_LIST
        ).is_displayed()

    def get_visible_quote_titles(self):
        quote_elements = self.driver.find_elements(
            *self.QUOTE_TITLE
        )

        return [
            element.get_attribute("text")
            for element in quote_elements
            if element.is_displayed()
        ]

    def scroll_quotes_down(self):
        quotes_list = self.find_visible(
            self.QUOTES_LIST
        )

        self.driver.execute_script(
            "mobile: scrollGesture",
            {
                "elementId": quotes_list.id,
                "direction": "down",
                "percent": 0.75
            }
        )

    def is_quotes_list_scrolled(self, titles_before):
        titles_after = self.get_visible_quote_titles()

        return titles_after != titles_before

    def expand_first_quote(self):
        self.click(self.EXPAND_BUTTON)

    def is_quote_description_visible(self):
        def visible_description(driver):
            descriptions = driver.find_elements(
                *self.QUOTE_DESCRIPTION
            )

            return any(
                description.is_displayed()
                for description in descriptions
            )

        return self.wait.until(
            visible_description
        )