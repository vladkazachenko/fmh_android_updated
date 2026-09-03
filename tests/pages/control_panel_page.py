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

    def _scroll_to_news_title(self, title):
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

        return self.find_visible(news_title)

    def is_news_present(self, title):
        return self._scroll_to_news_title(
            title
        ).is_displayed()

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

        self.click(edit_button)