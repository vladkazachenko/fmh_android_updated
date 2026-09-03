from appium.webdriver.common.appiumby import AppiumBy

from tests.pages.base_page import BasePage


class CreateEditNewsPage(BasePage):
    CATEGORY_FIELD = (
        AppiumBy.ID,
        "ru.edu.qamid:id/news_category_auto_complete"
    )

    TITLE_FIELD = (
        AppiumBy.ID,
        "ru.edu.qamid:id/news_title_edit_text"
    )

    DATE_FIELD = (
        AppiumBy.ID,
        "ru.edu.qamid:id/news_publish_date_edit_text"
    )

    TIME_FIELD = (
        AppiumBy.ID,
        "ru.edu.qamid:id/news_publish_time_edit_text"
    )

    DESCRIPTION_FIELD = (
        AppiumBy.ID,
        "ru.edu.qamid:id/news_description_edit_text"
    )

    ACTIVE_SWITCH = (
        AppiumBy.ID,
        "ru.edu.qamid:id/news_active_switch"
    )

    SAVE_BUTTON = (
        AppiumBy.ID,
        "ru.edu.qamid:id/news_save_button"
    )

    DIALOG_OK_BUTTON = (
        AppiumBy.ID,
        "android:id/button1"
    )

    def is_create_news_form_opened(self):
        return self.find_visible(
            self.CATEGORY_FIELD
        ).is_displayed()

    def select_category(self, category):
        self.click(self.CATEGORY_FIELD)

        category_option = (
            AppiumBy.XPATH,
            f'//android.widget.TextView[@text="{category}"]'
        )

        self.click(category_option)

    def enter_title(self, title):
        self.enter_text(
            self.TITLE_FIELD,
            title
        )

    def select_current_date(self):
        self.click(self.DATE_FIELD)
        self.click(self.DIALOG_OK_BUTTON)

    def select_current_time(self):
        self.click(self.TIME_FIELD)
        self.click(self.DIALOG_OK_BUTTON)

    def enter_description(self, description):
        self.enter_text(
            self.DESCRIPTION_FIELD,
            description
        )

    def save_news(self):
        if self.driver.is_keyboard_shown():
            self.driver.hide_keyboard()

        save_button = (
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true))'
            '.scrollIntoView(new UiSelector().resourceId('
            '"ru.edu.qamid:id/news_save_button"))'
        )

        self.click(save_button)