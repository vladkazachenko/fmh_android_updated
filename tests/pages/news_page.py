from appium.webdriver.common.appiumby import AppiumBy

from tests.pages.base_page import BasePage


class NewsPage(BasePage):
    NEWS_LIST_CONTAINER = (
        AppiumBy.ID,
        "ru.edu.qamid:id/news_list_container"
    )

    CONTROL_PANEL_BUTTON = (
        AppiumBy.ID,
        "ru.edu.qamid:id/news_edit_button"
    )

    def is_news_page_opened(self):
        return self.find_visible(
            self.NEWS_LIST_CONTAINER
        ).is_displayed()

    def open_control_panel(self):
        self.click(self.CONTROL_PANEL_BUTTON)