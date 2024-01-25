import allure
from locators.main_page_locators import MainPageLocators
from pages.order_page import OrderPage
from pages.main_page import MainPage
from pages.dzen_page import DzenPage


@allure.feature('Переходы на страницу "Яндекс Самокат", "Дзен" по кликам на лого')
class TestClickToLogo:
    @allure.title('Тест перехода на страницу "Яндекс Самокат"')
    @allure.description('Клик на лого "Самокат"  > переход на главную страницу "Яндекс Самокат"')
    def test_go_to_scooter_home_page_by_clicking_on_scooter_logo(self, driver, url):
        main_page = MainPage(driver)
        main_page.go_to_site(url)
        main_page.click_on_order_button(MainPageLocators.HEADER_ORDER_BUTTON)
        order_page = OrderPage(driver)
        order_page.click_on_scooter_logo()
        main_page.check_if_main_page_opened()

    @allure.title('Тест перехода на страницу "Dzen"')
    @allure.description('Клик по лого "Яндекс" > переход на страницу "Dzen"')
    def test_go_to_dzen_click_on_yandex_logo(self, driver, url):
        main_page = MainPage(driver)
        main_page.go_to_site(url)
        main_page.click_on_yandex_logo()
        main_page.go_to_dzen_page()
        dzen_page = DzenPage(driver)
        dzen_page.load_dzen_page()
        dzen_page.check_if_dzen_opened()
