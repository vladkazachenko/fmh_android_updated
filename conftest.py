import subprocess

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options


APP_PACKAGE = "ru.edu.qamid"


@pytest.fixture
def driver():
    subprocess.run(
        [
            "adb",
            "shell",
            "pm",
            "clear",
            APP_PACKAGE
        ],
        check=True,
        capture_output=True,
        text=True
    )

    options = UiAutomator2Options()

    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.udid = "emulator-5554"
    options.app_package = APP_PACKAGE
    options.app_activity = "ru.edu.qamid.ui.AppActivity"
    options.no_reset = False

    driver = webdriver.Remote(
        "http://127.0.0.1:4723",
        options=options
    )

    driver.update_settings({
        "enableMultiWindows": True
    })

    yield driver

    driver.quit()