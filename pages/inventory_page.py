from pages.base_page import BasePage
from playwright.sync_api import expect


class InventoryPage(BasePage):
    """Каталог товаров"""

    def __init__(self, page):
        super().__init__(page)
        self.add_to_cart_buttons = page.locator(".btn_inventory")
        self.shopping_cart_link = page.locator("[data-test='shopping-cart-anonymous']")
        self.product_titles = page.locator(".inventory_item_name")

    def add_all_to_cart(self):
        """Добавить все товары в корзину"""
        self.add_to_cart_buttons.nth(0).click()
        self.add_to_cart_buttons.nth(1).click()

    def go_to_cart(self):
        """Перейти в корзину"""
        self.shopping_cart_link.click()
        from pages.cart_page import CartPage
        return CartPage(self.page)

    def get_product_count(self) -> int:
        """Количество товаров на странице"""
        return len(self.product_titles.all())
