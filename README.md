# E-Commerce UI Tests (Playwright + pytest + GitHub Actions)

[![CI Tests](https://github.com/YOUR_USERNAME/ecommerce_demo_playwright/actions/workflows/test.yml/badge.svg)](https://github.com/YOUR_USERNAME/ecommerce_demo_playwright/actions)
[![Playwright](https://img.shields.io/badge/playwright-latest-brightgreen.svg)](https://playwright.dev/python/docs/intro)
[![Python](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/downloads/)

## **Что тестируем**
## **Е2Е тесты маркетплейса**

| Тест | Сценарий | Время |
|------|----------|-------|
| 🔐 `successful_login` | Корректный логин | ~8s |
| 🚫 `locked_out_user` | Блокировка юзера | ~6s |
| 🛒 `add_multiple_items` | 3 товара в корзину | ~12s |
| 💳 `full_checkout_flow` | Полный чекаут | ~20s |
| ✅ `checkout_validation` | Валидация формы | ~10s |


## **Как запустить**

### **Локально**
```bash
git clone https://github.com/YOUR_USERNAME/ecommerce_demo_playwright.git
cd ecommerce_demo_playwright

# Установка
pip install -r requirements.txt
playwright install chromium

# Запуск всех тестов
pytest tests/ -v -s
