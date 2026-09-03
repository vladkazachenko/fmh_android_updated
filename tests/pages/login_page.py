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

    def enter_login(self, login):
        self.enter_text(self.LOGIN_FIELD, login)

    def enter_password(self, password):
        self.enter_text(self.PASSWORD_FIELD, password)

    def click_sign_in(self):
        self.click(self.SIGN_IN_BUTTON)

    def login(self, login, password):
        self.enter_login(login)
        self.enter_password(password)
        self.click_sign_in()