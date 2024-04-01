import pytest
import allure
from pages.main_page import MainPage
from locators.main_page_locators import Locators
from data import QuestionsSetData, Urls


class TestMainPage:
    @pytest.mark.parametrize(QuestionsSetData.param, QuestionsSetData.value)
    @allure.title("Проверка ответа на вопрос № {question_number}")
    @allure.description("Нажимаем на вопрос и проверяем что текст равен ожидаемому")
    def test_click_to_question_and_read_answer(self, driver, question_number, expected_answer_text):

        main_page = MainPage(driver)
        main_page.open_page(Urls.main_page)
        main_page.scroll_to_end()

        formated_question_locator = main_page.format_locator(Locators.QUESTION_LOCATOR, question_number)
        formated_answer_locator = main_page.format_locator(Locators.ANSWER_LOCATOR, question_number)

        assert expected_answer_text == main_page.get_answer_text(formated_question_locator, formated_answer_locator)


