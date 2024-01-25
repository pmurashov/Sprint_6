import pytest
import allure
from locators.order_page_locators import OrderPageLocators
from locators.main_page_locators import MainPageLocators
from pages.order_page import OrderPage
from pages.main_page import MainPage


@allure.feature('Заказ самоката')
class TestScooterOrder:

    @allure.title('Тест заказа доставки самоката')
    @allure.description('Прохождение полного позитивного сценария заказа самоката')
    @pytest.mark.parametrize('customer_data, subway_station, rental_data, duration, color_button',
                             [[("Павел", "Мурашов", "Полтавская 3", "89527552272"),
                               OrderPageLocators.SAVYOLOVSKAYA_STATION,
                               ("26.01.2024", ""), OrderPageLocators.DROPDOWN_ONE_DAY,
                               OrderPageLocators.SCOOTER_COLOR_BLACK],
                              [("Джонни", "Сомбреро", "Испания", "89875321456"),
                               OrderPageLocators.KOZHOOKHOVSKAYA_STATION,
                               ("04.02.2024", "Привезите ещё тако"), OrderPageLocators.DROPDOWN_TWO_DAYS,
                               OrderPageLocators.SCOOTER_COLOR_GREY]])
    @pytest.mark.parametrize("order_button", [MainPageLocators.HEADER_ORDER_BUTTON, MainPageLocators.ORDER_BUTTON])
    def test_order_scooter(self, driver, url, order_button, customer_data, subway_station, rental_data, duration,
                           color_button):
        main_page = MainPage(driver)
        main_page.go_to_site(url)
        main_page.click_on_order_button(order_button)
        order_page = OrderPage(driver)
        order_page.fill_out_order_form(*customer_data, subway_station)
        order_page.click_on_next_button()
        order_page.fill_out_rent_details_form(*rental_data, duration, color_button)
        order_page.click_order_button()
        order_page.wait_for_load_order_header()
        order_page.click_on_yes_button()
        order_page.check_if_success_window_visible()
