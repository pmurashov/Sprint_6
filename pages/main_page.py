import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Клик на кнопку «Заказать»')
    def click_on_order_button(self, button):
        self.scroll_to_element(button)
        self.wait_for_element_to_be_clickable(button)
        self.click_on_element(button)

    @allure.step('Клик на логотип "Яндекс"')
    def click_on_yandex_logo(self):
        self.wait_for_element_to_be_clickable(MainPageLocators.HEADER_YA_LOGO)
        self.click_on_element(MainPageLocators.HEADER_YA_LOGO)

    @allure.step('Переход на страницу "Дзен"')
    def go_to_dzen_page(self):
        self.switch_to_window()

    @allure.step('Клик на вопрос')
    def click_on_question_button(self, button):
        self.scroll_to_element(button)
        self.wait_for_element_to_be_clickable(button)
        self.click_on_element(button)

    @allure.step('Проверка открытия текста ответа на выбранный вопрос')
    def check_answer_text(self, answer, expected_text):
        self.wait_for_element_to_be_visible(answer)
        actual_text = self.get_raw_text(answer)
        assert actual_text == expected_text

    @allure.step('Проверка открытия страницы "Яндекс Самокат"')
    def check_if_main_page_opened(self):
        current_url = self.get_current_url()
        assert current_url == "https://qa-scooter.praktikum-services.ru/"
