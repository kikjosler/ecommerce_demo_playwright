import os
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser(playwright):
    headless = os.getenv('CI', 'false').lower() == 'true'
    browser = playwright.chromium.launch(headless=headless)
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    page.context.close()
