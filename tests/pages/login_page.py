from appium.webdriver.common.appiumby import AppiumBy

from tests.pages.base_page import BasePage


class LoginPage(BasePage):
    LOGIN_FIELD = (
        AppiumBy.ID,
        "ru.edu.qamid:id/login_edit_text"
    )

    PASSWORD_FIELD = (
        AppiumBy.ID,
        "ru.edu.qamid:id/password_edit_text"
    )

    SIGN_IN_BUTTON = (
        AppiumBy.ID,
        "ru.edu.qamid:id/enter_button"
    )

    EMPTY_FIELDS_TOAST = (
        AppiumBy.XPATH,
        "//android.widget.Toast[@text='Login and password cannot be empty']"
    )

    WRONG_CREDENTIALS_TOAST = (
        AppiumBy.XPATH,
        "//android.widget.Toast[@text='Wrong login or password']"
    )

    TOAST = (
        AppiumBy.XPATH,
        "//android.widget.Toast"
    )

    def is_login_page_opened(self):
        return self.find_visible(
            self.LOGIN_FIELD
        ).is_displayed()

    def enter_login(self, login):
        self.enter_text(
            self.LOGIN_FIELD,
            login
        )

    def enter_password(self, password):
        self.enter_text(
            self.PASSWORD_FIELD,
            password
        )

    def click_sign_in(self):
        self.click(
            self.SIGN_IN_BUTTON
        )

    def login(self, login, password):
        self.enter_login(login)
        self.enter_password(password)
        self.click_sign_in()

    def get_empty_fields_error(self):
        return self.find_present(
            self.EMPTY_FIELDS_TOAST
        ).get_attribute("text")

    def get_wrong_credentials_error(self):
        return self.find_present(
            self.WRONG_CREDENTIALS_TOAST
        ).get_attribute("text")

    def get_toast_text(self, timeout=30):
        return self.find_present(
            self.TOAST,
            timeout=timeout
        ).get_attribute("text")