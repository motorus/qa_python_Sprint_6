import allure
from locators.order_page_locator import OrderPageForm1Locators, OrderPageForm2Locators, OrderButtonLocators
from data import Urls
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class OrderPage(BasePage):

    @allure.step('Кликаем на {order_button} кнопку заказа')
    def click_order_button(self, order_button):
        if order_button == 'top_button':
            self.click_to_element(OrderButtonLocators.TOP_BUTTON_ORDER)
        elif order_button == 'down_button':
            down_order_button = self.wait_and_find_element(OrderButtonLocators.DOWN_BUTTON_ORDER)
            self.execute_script("arguments[0].scrollIntoView();", down_order_button)
            self.click_to_element(OrderButtonLocators.DOWN_BUTTON_ORDER)

    @allure.step('Проверяем заголовок 1-й формы заказа')
    def get_heading_order_form1(self, order_button):
        self.open_page(Urls.main_page)
        self.click_order_button(order_button)

        self.wait_and_find_element(OrderPageForm1Locators.ORDER_HEADING_TEXT)
        return self.wait_and_find_element(OrderPageForm1Locators.ORDER_HEADING_TEXT).text

    @allure.step('Заполняем поле "Станция метро"')
    def input_metro_form_order(self, metro):
        self.click_to_element(OrderPageForm1Locators.METRO_LOCATOR)
        self.wait_and_find_element(OrderPageForm1Locators.METRO_LOCATOR).send_keys(metro)
        self.click_to_element(OrderPageForm1Locators.METRO_DROP_DOWN_LIST)

    @allure.step('Заполняем форму "Даты"')
    def input_date_form_order(self, date):
        self.wait_and_find_element(OrderPageForm2Locators.FIELD_INPUT_DATE).send_keys(date)

        formated_date = self.format_locator(OrderPageForm2Locators.DAY_NUMBER, date)
        self.click_to_element(formated_date)

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
    def get_windows_order_pass_text(self):
        return self.wait_and_find_element(OrderPageForm2Locators.FINAL_ORDER_WINDOW).text

    def click_date(self, date):
        date = date.split('.')[0]
        return By.XPATH, f".//div[contains(@aria-label, '{date}-е')]"

    def create_order(self, button_order, name, surname, address, metro, phone, date, period, colour_scooter, comment):

        self.open_page(Urls.main_page)
        self.click_order_button(button_order)
        self.wait_and_find_element(OrderPageForm1Locators.ORDER_HEADING_TEXT)
        self.wait_and_find_element(OrderPageForm1Locators.FIRST_NAME_LOCATOR).send_keys(name)
        self.wait_and_find_element(OrderPageForm1Locators.SURNAME_LOCATOR).send_keys(surname)
        self.wait_and_find_element(OrderPageForm1Locators.ADDRESS_LOCATOR).send_keys(address)
        self.input_metro_form_order(metro)
        self.wait_and_find_element(OrderPageForm1Locators.PHONE_LOCATOR).send_keys(phone)
        self.click_to_element(OrderPageForm1Locators.NEXT_BUTTON)
        self.wait_and_find_element(OrderPageForm2Locators.ORDER_HEADING_TEXT)
        self.input_date_form_order(date)
        self.input_period_form_order(period)
        self.click_color_checkbox(colour_scooter)
        self.wait_and_find_element(OrderPageForm2Locators.COMMENT_INPUT).send_keys(comment)
        self.click_to_element(OrderPageForm2Locators.ORDER_BUTTON)
        self.click_to_element(OrderPageForm2Locators.ORDER_BUTTON_YES)



