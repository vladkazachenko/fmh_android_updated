from selenium.common.exceptions import TimeoutException

from appium.webdriver.common.appiumby import AppiumBy

from tests.pages.base_page import BasePage


class FilterNewsPage(BasePage):
    CATEGORY_FIELD = (
        AppiumBy.ID,
        "ru.edu.qamid:id/filter_news_category_auto_complete"
    )

    START_DATE_FIELD = (
        AppiumBy.ID,
        "ru.edu.qamid:id/filter_news_date_start_edit_text"
    )

    END_DATE_FIELD = (
        AppiumBy.ID,
        "ru.edu.qamid:id/filter_news_date_end_edit_text"
    )

    ACTIVE_CHECKBOX = (
        AppiumBy.ID,
        "ru.edu.qamid:id/filter_news_active_check_box"
    )

    INACTIVE_CHECKBOX = (
        AppiumBy.ID,
        "ru.edu.qamid:id/filter_news_inactive_check_box"
    )

    APPLY_BUTTON = (
        AppiumBy.ID,
        "ru.edu.qamid:id/filter_news_apply_button"
    )

    CANCEL_BUTTON = (
        AppiumBy.ID,
        "ru.edu.qamid:id/filter_news_cancel_button"
    )

    DATE_DIALOG_OK_BUTTON = (
        AppiumBy.ID,
        "android:id/button1"
    )

    def is_filter_opened(self):
        return self.find_visible(
            self.CATEGORY_FIELD
        ).is_displayed()

    def select_category(self, category):
        category_option = (
            AppiumBy.XPATH,
            f'//android.widget.TextView[@text="{category}"]'
        )

        for attempt in range(3):
            self.click(
                self.CATEGORY_FIELD
            )

            try:
                option = self.find_present(
                    category_option,
                    timeout=7
                )

                option.click()

                selected_category = self.find_visible(
                    self.CATEGORY_FIELD
                ).get_attribute("text")

                if selected_category != category:
                    raise AssertionError(
                        f'Ожидалась категория "{category}", '
                        f'но выбрана "{selected_category}"'
                    )

                return

            except TimeoutException:
                if attempt < 2:
                    self.driver.back()

        raise TimeoutException(
            f'Не удалось выбрать категорию "{category}"'
        )

    def select_current_start_date(self):
        self.click(
            self.START_DATE_FIELD
        )

        self.click(
            self.DATE_DIALOG_OK_BUTTON
        )

        return self.find_visible(
            self.START_DATE_FIELD
        ).get_attribute("text").strip()

    def select_current_end_date(self):
        self.click(
            self.END_DATE_FIELD
        )

        self.click(
            self.DATE_DIALOG_OK_BUTTON
        )

        return self.find_visible(
            self.END_DATE_FIELD
        ).get_attribute("text").strip()

    def apply_filter(self):
        self.click(
            self.APPLY_BUTTON
        )

    def cancel_filter(self):
        self.click(
            self.CANCEL_BUTTON
        )