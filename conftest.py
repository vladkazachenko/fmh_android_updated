import subprocess

import allure
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options


APP_PACKAGE = "ru.edu.qamid"


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    setattr(
        item,
        f"rep_{report.when}",
        report
    )


@pytest.fixture
def driver(request):
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

    test_report = getattr(
        request.node,
        "rep_call",
        None
    )

    if (
        test_report is not None
        and test_report.failed
    ):
        try:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="Скриншот при падении теста",
                attachment_type=allure.attachment_type.PNG
            )
        except Exception:
            pass

    driver.quit()