import os
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser(playwright):
    """CI = headless=True, Локально = headless=False"""
    is_ci = os.getenv('CI', 'false').lower() == 'true'
    
    browser = playwright.chromium.launch(
        headless=is_ci,                    # CI=true → headless
        slow_mo=0 if is_ci else 1500       # CI → быстро, локально → медленно
    )
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def context(browser):
    context = browser.new_context()
    yield context
    context.close()

@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    yield page
    page.context.close()
