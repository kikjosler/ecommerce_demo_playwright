import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

@pytest.mark.smoke
def test_full_checkout_flow(page):
    # Логин
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    # Добавить ПЕРВЫЙ товар
    inventory = InventoryPage(page)
    inventory.add_first_item_to_cart()

    # Перейти в корзину
    cart_page = inventory.go_to_cart()
    print("✅ До корзины дошли!")

