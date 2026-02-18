def test_complete_shopping_flow(logged_user):
    """Полный шоппинг-флоу: товары → корзина → оформление"""
    # Добавляем товары
    logged_user.add_all_to_cart()
    cart_page = logged_user.go_to_cart()

    # Проверяем корзину
    assert cart_page.is_loaded()

    # Checkout (упрощенно)
    checkout_page = cart_page.proceed_to_checkout()
    assert checkout_page.is_loaded()
