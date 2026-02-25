from playwright.sync_api import Page, expect

class CheckoutPage:
    """💳 Page Object для Checkout (оформление заказа)"""
    
    def __init__(self, page: Page):
        self.page = page
        
        # 🏷️ Локаторы формы Checkout
        self.first_name = page.locator("[data-test='firstName']")
        self.last_name = page.locator("[data-test='lastName']")
        self.zip_code = page.locator("[data-test='postalCode']")
        self.continue_btn = page.locator("[data-test='continue']")
        self.finish_btn = page.locator("[data-test='finish']")
        
        # Проверки
        self.error_msg = page.locator("text=Error")
        self.complete_header = page.locator("[data-test='complete-header']")
    
    def fill_checkout_info(self, first_name: str, last_name: str, zip_code: str):
        """Заполнить форму чекаута"""
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.zip_code.fill(zip_code)
        self.continue_btn.click()
    
    def complete_order(self):
        """Завершить заказ"""
        self.finish_btn.click()
    
    def verify_checkout_complete(self):
        """Проверить успешное завершение"""
        expect(self.complete_header).to_be_visible()
        expect(self.page.locator("text=Thank you")).to_be_visible()
    
    def verify_validation_error(self):
        """Проверить ошибку валидации"""
        expect(self.error_msg).to_be_visible()
