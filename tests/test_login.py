import pytest
import json
from pages.login_page import LoginPage


@pytest.mark.smoke
class TestLogin:

    @pytest.fixture(autouse=True)
    def setup(self, page):
        self.login_page = LoginPage(page)
        self.login_page.navigate()
        self.users = json.loads(open("data/users.json").read())

    def test_successful_login(self, page):
        """Успешный логин"""
        inventory = self.login_page.successful_login(
            self.users["standard_user"]["username"],
            self.users["standard_user"]["password"]
        )
        assert inventory.is_loaded()

    def test_locked_out_user(self):
        """Заблокированный пользователь"""
        self.login_page.error_login(
            self.users["locked_out_user"]["username"],
            self.users["locked_out_user"]["password"],
            "Epic sadface: Sorry, this user has been locked out."
        )

    def test_incorrect_password(self):
        """Неверный пароль"""
        self.login_page.error_login(
            "standard_user",
            "wrongpass",
            "Epic sadface: Username and password do not match"
        )
