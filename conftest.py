import pytest
import json
import os
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage

@pytest.fixture(scope="session")
def playwright():
    pw = sync_playwright().start()
    yield pw
    pw.stop()

@pytest.fixture(scope="session")
def browser(playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    yield browser
    browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context(viewport={"width": 1280, "height": 720})
    page = context.new_page()
    yield page
    context.close()

@pytest.fixture
def logged_user(page, data_path):
    """Залогиненный стандартный пользователь"""
    login_page = LoginPage(page)
    login_page.navigate()
    user_data = json.loads(data_path.read_text())["standard_user"]
    inventory_page = login_page.successful_login(user_data["username"], user_data["password"])
    return inventory_page

@pytest.fixture
def data_path():
    return os.path.join(os.path.dirname(__file__), "data/users.json")
