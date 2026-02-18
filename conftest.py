import pytest
import json

@pytest.fixture(scope="session")
def users():
    """Тестовые пользователи"""
    return {
        "standard_user": {"username": "standard_user", "password": "secret_sauce"},
        "locked_out_user": {"username": "locked_out_user", "password": "secret_sauce"}
    }

@pytest.fixture(scope="session")
def browser(playwright):
    """Замедленный браузер для дебага"""
    browser = playwright.chromium.launch(
        headless=False,
        slow_mo=1500  # 1.5 сек между ВСЕМИ действиями!
    )
    yield browser
    browser.close()