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

    def is_control_panel_opened(self):
        return self.find_visible(
            self.NEWS_LIST
        ).is_displayed()

    def open_create_news_form(self):
        self.click(self.ADD_NEWS_BUTTON)

    def is_news_present(self, title):
        news_title = (
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable('
            'new UiSelector().resourceId('
            '"ru.edu.qamid:id/news_list_recycler_view"))'
            '.scrollIntoView('
            'new UiSelector().resourceId('
            '"ru.edu.qamid:id/news_item_title_text_view")'
            f'.text("{title}"))'
        )

        return self.find_visible(
            news_title
        ).is_displayed()