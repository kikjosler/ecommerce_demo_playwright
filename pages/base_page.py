from playwright.sync_api import Page, expect
from typing import Optional


class BasePage:
    """Базовый класс для всех страниц"""

    BASE_URL = "https://www.saucedemo.com/"

    def __init__(self, page: Page):
        self.page = page

    def navigate(self, path: str = "/"):
        """Навигация с базовым URL"""
        self.page.goto(self.BASE_URL + path)

    def is_loaded(self) -> bool:
        """Базовая проверка загрузки"""
        return self.page.locator("body").is_visible()
