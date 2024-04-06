import pytest
import allure
from pages.order_page import OrderPage


class TestButtonOrder:

    @allure.title('Проверка кнопок \"Заказать\" на главной странице')
    @allure.description('Проверяем кнопку {button_order}')
    @pytest.mark.parametrize("order_button", ['top_button', 'down_button'])
    def test_click_order_button(self, driver, order_button):
        order_page = OrderPage(driver)

        assert "Для кого самокат" in order_page.get_heading_order_form1(order_button)
