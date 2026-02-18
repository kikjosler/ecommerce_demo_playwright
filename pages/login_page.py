from pages.base_page import BasePage
from playwright.sync_api import expect
import json


class LoginPage(BasePage):
    """Страница логина"""

    def __init__(self, page):
        super().__init__(page)
        self.username_input = page.locator("[data-test='username']")
        self.password_input = page.locator("[data-test='password']")
        self.login_button = page.locator("[data-test='login-button']")
        self.error_message = page.locator("[data-test='error']")

    def login(self, username: str, password: str):
        """Выполнить логин"""
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def successful_login(self, username: str, password: str):
        """Успешный логин → InventoryPage"""
        self.login(username, password)
        from pages.inventory_page import InventoryPage
        return InventoryPage(self.page)

    def error_login(self, username: str, password: str, expected_error: str):
        """Логин с ошибкой"""
        self.login(username, password)
        expect(self.error_message).to_have_text(expected_error)
