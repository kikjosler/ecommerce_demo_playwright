from pages.base_page import BasePage
from playwright.sync_api import Page

class CartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.checkout_btn = page.locator("#checkout")
    
    def start_checkout(self):
        self.checkout_btn.click()
        self.page.wait_for_load_state("networkidle")
        print("✅ Перешли на Checkout!")