from pages.base_page import BasePage
from playwright.sync_api import Page, expect

class InventoryPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
    
    def add_first_item_to_cart(self):
        """Добавить первый товар"""
        self.page.locator(".btn.btn_primary.btn_small.btn_inventory").first.click()
        self.page.locator(".shopping_cart_badge").wait_for(state="visible")
        print("Первый товар в корзине!")
    
    def go_to_cart(self):
        """Перейти в корзину"""
        self.page.locator(".shopping_cart_link").click()
        self.page.wait_for_load_state("networkidle")
        from pages.cart_page import CartPage
        return CartPage(self.page)
