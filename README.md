# ecommerce_demo_playwright

Автоматизированные тесты интернет-магазина на Playwright + Python + POM

## Запуск
```bash
pip install -r requirements.txt
playwright install
pytest tests/ -v --html=reports/report.html
