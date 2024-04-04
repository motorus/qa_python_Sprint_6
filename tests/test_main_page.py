import pytest
import allure
from pages.main_page import MainPage
from data import QuestionsSetData


class TestMainPage:
    @pytest.mark.parametrize(QuestionsSetData.param, QuestionsSetData.value)
    @allure.title("Проверка ответа на вопрос № {question_number}")
    @allure.description("Нажимаем на вопрос и проверяем что текст равен ожидаемому")
    def test_click_to_question_and_read_answer(self, driver, question_number, expected_answer_text):

        main_page = MainPage(driver)
        assert expected_answer_text == main_page.get_answer_text(question_number)
