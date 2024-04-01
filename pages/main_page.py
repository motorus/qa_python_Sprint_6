import allure

from locators.main_page_locators import Locators
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys


class MainPage(BasePage):

    @allure.step("Скроллим вниз до конца страницы")
    def scroll_to_end(self):
        text_faq = self.driver.find_element(*Locators.HTML_TAG)
        text_faq.send_keys(Keys.END)

    @allure.step("Кликаем по вопросу и получаем текст ответа")
    def get_answer_text(self, question_locator, answer_locator):
        self.click_to_element(question_locator)
        return self.wait_and_find_element(answer_locator).text
