## Яндекс Практикум
#### Курс "Автоматизатор тестирования на Python"
#### 6 спринт
#### Финальный проект


### Файлы:
- allure_results/ - результаты запуска тестов allure
- conftest.py - фикстуры с драйвером для входа на сайт
- data.py - классы с URL и данными параметризации тестов
- locators/main_page_locators.py - локаторы главной страницы
- locators/order_page_locator.py - локаторы страницы заказа самоката
- tests/test_icon_button.py - кнопки Яндекс/Самокат на главной страницы
- tests/test_main_page.py - проверка ответов на вопросы на главной странице
- tests/test_order.py - проверка заказа самоката
- tests/test_order_button.py - проверка кнопок "Заказать"


#### Запуск тестов
`pytest tests/ --alluredir=allure_results`
#### Запуск отчетности allure
`allure serve allure_results`
