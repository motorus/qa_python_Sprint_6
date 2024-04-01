import allure
from locators.order_page_locator import OrderPageForm1Locators, OrderPageForm2Locators, OrderButtonLocators

from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class OrderPage(BasePage):

    @allure.step('Кликаем на {order_button} кнопку заказа')
    def click_order_button(self, order_button):
        if order_button == 'top_button':
            self.click_to_element(OrderButtonLocators.TOP_BUTTON_ORDER)
        elif order_button == 'down_button':
            down_order_button = self.wait_and_find_element(OrderButtonLocators.DOWN_BUTTON_ORDER)
            self.driver.execute_script("arguments[0].scrollIntoView();", down_order_button)
            self.click_to_element(OrderButtonLocators.DOWN_BUTTON_ORDER)

    @allure.step('Проверяем заголовок 1-й формы заказа')
    def check_heading_order_form1(self):
        actually_value = self.wait_and_find_element(OrderPageForm1Locators.ORDER_HEADING_TEXT).text
        expected_value = "Для кого самокат"
        assert expected_value in actually_value

    @allure.step('Заполняем поле "Станция метро"')
    def input_metro_form_order(self, metro):
        self.click_to_element(OrderPageForm1Locators.METRO_LOCATOR)
        self.wait_and_find_element(OrderPageForm1Locators.METRO_LOCATOR).send_keys(metro)
        self.click_to_element(OrderPageForm1Locators.METRO_DROP_DOWN_LIST)

    @allure.step('Заполняем форму "Даты"')
    def input_date_form_order(self, date):
        self.wait_and_find_element(OrderPageForm2Locators.FIELD_INPUT_DATE).send_keys(date)
        self.click_to_element(self.click_date(date))

    @allure.step('Заполняем форму "Срок аренды"')
    def input_period_form_order(self, time_period):
        self.click_to_element(OrderPageForm2Locators.FIELD_INPUT_PERIOD)
        self.click_to_element(self.format_locator(OrderPageForm2Locators.SELECTED_DATE, time_period))

    @allure.step('Выбираем цвет')
    def click_color_checkbox(self, colour_scooter):
        if colour_scooter == 'чёрный жемчуг':
            locator = 'black'
        else:
            locator = 'grey'
        self.click_to_element(self.format_locator(OrderPageForm2Locators.COLOUR_LOCATOR, locator))

    @allure.step('Проверяем заголовок окна успешного заказа')
    def check_windows_order_pass(self):
        actually_value = self.wait_and_find_element(OrderPageForm2Locators.FINAL_ORDER_WINDOW).text
        expected_value = "Заказ оформлен"
        assert expected_value in actually_value


    def click_date(self, date):
        date = date.split('.')[0]
        return By.XPATH, f".//div[contains(@aria-label, '{date}-е')]"
