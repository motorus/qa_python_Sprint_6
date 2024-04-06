import allure
import time
from locators.main_page_locators import Locators
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from data import Urls
from locators.main_page_locators import IconsLocators


class MainPage(BasePage):

    @allure.step("Скроллим вниз до конца страницы")
    def scroll_to_end(self):
        self.wait_and_find_element(Locators.HTML_TAG).send_keys(Keys.END)

    @allure.step("Кликаем по вопросу и получаем текст ответа")
    def get_answer_text(self, question_number):
        self.open_page(Urls.main_page)
        self.scroll_to_end()

        formated_question_locator = self.format_locator(Locators.QUESTION_LOCATOR, question_number)
        formated_answer_locator = self.format_locator(Locators.ANSWER_LOCATOR, question_number)

        self.click_to_element(formated_question_locator)
        return self.wait_and_find_element(formated_answer_locator).text

    def click_to_icon_scooter(self):
        self.open_page(Urls.main_page)
        self.click_to_element(IconsLocators.SCOOTER_ICON)
        return self.wait_and_find_element(IconsLocators.TEXT_IN_MAIN_PAGE).text

    def click_to_icon_yandex(self):
        self.open_page(Urls.main_page)
        self.click_to_element(IconsLocators.ALTERNATE_YANDEX_ICON)
        time.sleep(7)
        self.switch_to_window()
        self.wait_for_load_window(Urls.yandex_dzen)

    def get_current_url(self):
        return self.driver.current_url
