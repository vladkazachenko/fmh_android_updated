from appium.webdriver.common.appiumby import AppiumBy

from tests.pages.base_page import BasePage


class MainPage(BasePage):
    NEWS_LIST_CONTAINER = (
        AppiumBy.ID,
        "ru.edu.qamid:id/main_news_list_container"
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

    LOG_OUT_BUTTON = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="Log out"]'
    )

    def is_main_page_opened(self):
        return self.find_visible(
            self.NEWS_LIST_CONTAINER
        ).is_displayed()

    def open_news(self):
        self.click(self.ALL_NEWS_BUTTON)

    def open_our_mission(self):
        self.click(self.OUR_MISSION_BUTTON)

    def restart_app(self):
        self.driver.terminate_app(
            "ru.edu.qamid"
        )

        self.driver.activate_app(
            "ru.edu.qamid"
        )

    def log_out(self):
        self.click(self.AUTHORIZATION_BUTTON)
        self.click(self.LOG_OUT_BUTTON)