import pytest
import allure
from pages.order_page import OrderPage
from data import Urls
from locators.order_page_locator import OrderPageForm1Locators


class TestButtonOrder:

    @allure.title('Проверка кнопок \"Заказать\" на главной странице')
    @allure.description('Проверяем кнопку {button_order}')
    @pytest.mark.parametrize("order_button", ['top_button', 'down_button'])
    def test_click_order_button(self, driver, order_button):
        order_page = OrderPage(driver)
        order_page.open_page(Urls.main_page)
        order_page.click_order_button(order_button)

        order_page.wait_and_find_element(OrderPageForm1Locators.ORDER_HEADING_TEXT)
        order_page.check_heading_order_form1()
