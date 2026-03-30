import os
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser(playwright):
    """CI=prod, DEMO=demo, default=local"""
    mode = os.getenv('DEMO_MODE', 'local').lower()
    
    if mode == 'demo':
        # видимый + медленно
        browser = playwright.chromium.launch(headless=False, slow_mo=1500)
    elif os.getenv('CI', 'false').lower() == 'true':
        # headless + быстро
        browser = playwright.chromium.launch(headless=True, slow_mo=0)
    else:
        # Локально: гибрид
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
    
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
