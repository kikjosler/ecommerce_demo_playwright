import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.mark.smoke
def test_add_multiple_items(page):
    """🛒 Добавить 2+ товара в корзину"""
    # Логин
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    
    # Добавить 2 товара
    inventory = InventoryPage(page)
    inventory.add_first_item_to_cart()
    inventory.page.locator(".btn.btn_primary.btn_small.btn_inventory").nth(1).click()
    
    # Проверка бейджа = 2
    assert inventory.page.locator(".shopping_cart_badge").inner_text() == "2"
    print("✅ 2 товара в корзине!")
