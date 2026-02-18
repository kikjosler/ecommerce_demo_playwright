import pytest
import json
import os


@pytest.fixture(scope="session")
def browser(playwright):
    """CI = headless, Локально = видимый"""
    is_ci = os.getenv('CI', 'false').lower() == 'true'

    browser = playwright.chromium.launch(
        headless=is_ci,  # ← CI=true → headless
        slow_mo=1500 if not is_ci else 0  # ← CI без замедления
    )
    yield browser
    browser.close()
