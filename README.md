# E-Commerce UI Tests (Playwright + pytest + GitHub Actions)

[![CI Tests](https://github.com/YOUR_USERNAME/ecommerce_demo_playwright/actions/workflows/test.yml/badge.svg)](https://github.com/YOUR_USERNAME/ecommerce_demo_playwright/actions)
[![Tests](https://img.shields.io/badge/tests-4/4%20PASSED-brightgreen.svg)](https://github.com/YOUR_USERNAME/ecommerce_demo_playwright/actions)
[![Playwright](https://img.shields.io/badge/playwright-latest-brightgreen.svg)](https://playwright.dev/python/docs/intro)
[![Python](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/downloads/)

## **Что тестируем**
E2E тесты интернет-магазина:

| Тест | Сценарий
|------|----------
| 🔐 `test_successful_login` | Успешный вход standard_user
| 🚫 `test_locked_out_user` | Блокировка locked_out_user
| 🛒 `test_add_multiple_items` | Добавление 3+ товаров в корзину
| 💳 `test_full_checkout_flow` | Полный чекаут с оплатой

## **Как запустить**

### **Локально (браузер)**
```bash
git clone https://github.com/YOUR_USERNAME/ecommerce_demo_playwright.git
cd ecommerce_demo_playwright

# Установка
pip install -r requirements.txt
playwright install chromium

# Запуск всех тестов (медленно + браузер)
pytest tests/ -v -s
