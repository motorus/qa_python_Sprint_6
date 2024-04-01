import pytest
import allure
from pages.order_page import OrderPage
from data import OrderSetData
from data import Urls
from locators.order_page_locator import OrderPageForm1Locators, OrderPageForm2Locators


class TestOrder:

    @allure.title('Полная проверка сценария "Заказать"')
    @allure.description('Полная проверка сценария "Заказать"')
    @pytest.mark.parametrize(OrderSetData.input_params, OrderSetData.data_set)
    def test_input_form1_order(self, driver, button_order, name, surname, address, metro, phone, date, period,
                               colour_scooter, comment):
        order_page = OrderPage(driver)
        order_page.open_page(Urls.main_page)
        order_page.click_order_button(button_order)
        order_page.wait_and_find_element(OrderPageForm1Locators.ORDER_HEADING_TEXT)
        order_page.wait_and_find_element(OrderPageForm1Locators.FIRST_NAME_LOCATOR).send_keys(name)
        order_page.wait_and_find_element(OrderPageForm1Locators.SURNAME_LOCATOR).send_keys(surname)
        order_page.wait_and_find_element(OrderPageForm1Locators.ADDRESS_LOCATOR).send_keys(address)
        order_page.input_metro_form_order(metro)
        order_page.wait_and_find_element(OrderPageForm1Locators.PHONE_LOCATOR).send_keys(phone)
        order_page.click_to_element(OrderPageForm1Locators.NEXT_BUTTON)
        order_page.wait_and_find_element(OrderPageForm2Locators.ORDER_HEADING_TEXT)
        order_page.input_date_form_order(date)
        order_page.input_period_form_order(period)
        order_page.click_color_checkbox(colour_scooter)
        order_page.wait_and_find_element(OrderPageForm2Locators.COMMENT_INPUT).send_keys(comment)
        order_page.click_to_element(OrderPageForm2Locators.ORDER_BUTTON)
        order_page.click_to_element(OrderPageForm2Locators.ORDER_BUTTON_YES)

        order_page.check_windows_order_pass()
