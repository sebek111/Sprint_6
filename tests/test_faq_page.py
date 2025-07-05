import allure
import pytest
from data import faq_answers_text
from pages.home_page import HomePage


class TestFAQBlock:

    @allure.title('FAQ: отображение ответов на вопросы')
    @allure.description('Проверяем, что при клике на каждый вопрос в блоке FAQ появляется корректный ответ')
    @pytest.mark.parametrize('num', range(8))
    def test_click_question_shows_correct_answer(self, driver_main_page, num):
        page = HomePage(driver_main_page)

        page.wait_for_homepage_loaded()
        page.scroll_to_down()
        page.click_to_question(num)

        actual_text = page.get_answer_text(num)
        expected_text = faq_answers_text[num]

        assert actual_text == expected_text, f'Ожидали: «{expected_text}», получили: «{actual_text}»'
