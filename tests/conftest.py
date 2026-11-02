
import allure
import pytest
from playwright.sync_api import Page


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Capture evidence if the test fails during execution
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")

        if page is not None:
            screenshot = page.screenshot(full_page=True)

            allure.attach(
                screenshot,
                name=f"{item.name}-failure",
                attachment_type=allure.attachment_type.PNG,
            )
