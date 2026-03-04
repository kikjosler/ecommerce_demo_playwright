import pytest


@pytest.mark.smoke
def test_full_checkout_flow(page):
    """Полный чекаут: логин → товар → корзина → оплата → успех"""

    # 1. Логин
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    # 2. Добавить товар
    page.click("[data-test='add-to-cart-sauce-labs-backpack']")

    # 3. Корзина
    page.click(".shopping_cart_link")
    print("Корзина: 1 товар")

    # 4. Checkout
    page.click("[data-test='checkout']")

    # 5. Заполнить форму
    page.fill("[data-test='firstName']", "John")
    page.fill("[data-test='lastName']", "Doe")
    page.fill("[data-test='postalCode']", "12345")
    page.click("[data-test='continue']")

    # 6. Завершить
    page.click("[data-test='finish']")

    # 7. Проверка успеха
    assert page.locator("[data-test='complete-header']").is_visible()
    print("Чекаут завершен!")
