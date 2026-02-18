import os
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser(playwright):
    """CI=headless, Локально=headed"""
    is_ci = os.getenv('CI', 'false').lower() == 'true'
    
    browser = playwright.chromium.launch(
        headless=is_ci,           # ← CI=true → headless=True
        slow_mo=0 if is_ci else 1500  # ← CI без задержек
    )
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
