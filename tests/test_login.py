from pages.login_page import LoginPage
import pytest

@pytest.mark.smoke
def test_successful_login(page):  # ← ФУНКЦИЯ, не метод класса!
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    assert "inventory" in page.url

@pytest.mark.smoke
def test_locked_out_user(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.error_login("locked_out_user", "secret_sauce",
        "Epic sadface: Sorry, this user has been locked out.")
