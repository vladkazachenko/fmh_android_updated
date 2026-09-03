from appium.webdriver.common.appiumby import AppiumBy

from tests.pages.base_page import BasePage


class MainPage(BasePage):
    NEWS_LIST_CONTAINER = (
        AppiumBy.ID,
        "ru.edu.qamid:id/main_news_list_container"
    )

    def is_main_page_opened(self):
        return self.find_visible(
            self.NEWS_LIST_CONTAINER
        ).is_displayed()