import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options


@pytest.fixture
def driver():
    options = UiAutomator2Options()

    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.udid = "emulator-5554"
    options.app_package = "ru.edu.qamid"
    options.app_activity = "ru.edu.qamid.ui.AppActivity"
    options.no_reset = False

    driver = webdriver.Remote(
        "http://127.0.0.1:4723",
        options=options
    )

    yield driver

    driver.quit()