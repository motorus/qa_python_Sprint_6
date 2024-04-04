import pytest
import allure
from pages.order_page import OrderPage
from data import OrderSetData


class TestOrder:

    @allure.title('Полная проверка сценария "Заказать"')
    @allure.description('Полная проверка сценария "Заказать"')
    @pytest.mark.parametrize(OrderSetData.input_params, OrderSetData.data_set)
    def test_input_form1_order(self, driver, button_order, name, surname, address, metro, phone, date, period,
                               colour_scooter, comment):
        order_page = OrderPage(driver)
        order_page.create_order(button_order, name, surname, address, metro, phone, date, period,
                                colour_scooter, comment)
        assert "Заказ оформлен" in order_page.get_windows_order_pass_text()
