import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DzenPage(BasePage):
    HEADER_DZEN_LOGO = (By.CLASS_NAME, 'desktop-base-header__logo-tA')

    @allure.step('Ожидание загрузки главной страницы Дзен')
    def load_dzen_page(self):
        self.wait_for_element_to_be_visible(self.HEADER_DZEN_LOGO)

    @allure.step('Проверка открытия страницы Дзен')
    def check_if_dzen_opened(self):
        current_url = self.get_current_url()
        assert current_url == "https://dzen.ru/?yredirect=true", 'Страница Дзена не открылась'