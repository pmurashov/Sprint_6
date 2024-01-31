import pytest
import allure
from locators.main_page_locators import MainPageLocators
from data.answers_faq import AnswersFAQ
from pages.main_page import MainPage


@allure.feature('FAQ на главной странице "Яндекс Самокат"')
class TestFaqHomePage:

    @allure.title('Тест открытия ответов в FAQ')
    @allure.description('Клик по вопросам FAQ по очереди > открываются ответы на вопросы по очереди')
    @pytest.mark.parametrize(
        'button, answer, expected_text',
        [
            [MainPageLocators.QUESTION_PAYMENT, MainPageLocators.ANSWER_PAYMENT,
             AnswersFAQ.cost_answer],
            [MainPageLocators.QUESTION_MULTIPLE_SCOOTERS, MainPageLocators.ANSWER_MULTIPLE_SCOOTERS,
             AnswersFAQ.share_answer],
            [MainPageLocators.QUESTION_COUNT_RENT_TIME, MainPageLocators.ANSWER_COUNT_RENT_TIME,
             AnswersFAQ.rent_time_answer],
            [MainPageLocators.QUESTION_TODAY_RENT, MainPageLocators.ANSWER_TODAY_RENT,
             AnswersFAQ.today_rent_answer],
            [MainPageLocators.QUESTION_EXTEND_OR_RETURN, MainPageLocators.ANSWER_EXTEND_OR_RETURN,
             AnswersFAQ.extend_return_answer],
            [MainPageLocators.QUESTION_CHARGER, MainPageLocators.ANSWER_CHARGER,
             AnswersFAQ.charge_answer],
            [MainPageLocators.QUESTION_CANCEL_ORDER, MainPageLocators.ANSWER_CANCEL_ORDER,
             AnswersFAQ.cancel_order_answer],
            [MainPageLocators.QUESTION_MKAD, MainPageLocators.ANSWER_MKAD,
             AnswersFAQ.mkad_answer]
        ]
    )
    def test_faq_list_click_on_questions_check_answer_(self, driver, button, answer, expected_text):
        main_page = MainPage(driver)
        main_page.click_on_question_button(button)
        main_page.check_answer_text(answer, expected_text)
