import allure
from selenium.webdriver import Keys
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Ожидание загрузки формы заказа')
    def wait_for_order_form_to_be_loaded(self):
        self.wait_for_element_to_be_visible(OrderPageLocators.ORDER_CAPTION)

    @allure.step('Заполнение поля "Имя"')
    def set_first_name(self, name):
        self.send_keys(OrderPageLocators.FIRST_NAME_INPUT, name)

    @allure.step('Заполнение поля "Фамилия"')
    def set_last_name(self, surname):
        self.send_keys(OrderPageLocators.LAST_NAME_INPUT, surname)

    @allure.step('Заполнение поля "Адрес"')
    def set_address(self, address):
        self.send_keys(OrderPageLocators.ADDRESS_INPUT, address)

    @allure.step('Клик на список "Станция метро"')
    def click_on_subway_dropdown(self):
        self.click_on_element(OrderPageLocators.SUBWAY_STATION)

    @allure.step('Выбор станции метро в списке')
    def select_subway(self, metro):
        self.scroll_to_element(metro)
        self.wait_for_element_to_be_clickable(metro)
        self.click_on_element(metro)

    @allure.step('Заполнение поля "Телефон"')
    def set_phone(self, phone):
        self.send_keys(OrderPageLocators.PHONE_INPUT, phone)

    @allure.step('Заполнение формы "Для кого самокат"')
    def fill_out_order_form(self, name, surname, address, phone, metro):
        self.wait_for_order_form_to_be_loaded()
        self.set_first_name(name)
        self.set_last_name(surname)
        self.set_address(address)
        self.click_on_subway_dropdown()
        self.select_subway(metro)
        self.set_phone(phone)

    @allure.step('Клик на кнопку "Далее" формы "Для кого самокат"')
    def click_on_next_button(self):
        self.click_on_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Ожидание загрузки формы "Про аренду"')
    def wait_for_rent_details_form_to_be_loaded(self):
        self.wait_for_element_to_be_visible(OrderPageLocators.ABOUT_RENT_CAPTION)

    @allure.step('Заполнение поля "Дата аренды"')
    def set_date(self, date):
        self.send_keys(OrderPageLocators.RENT_DATE_INPUT, date)
        self.send_keys(OrderPageLocators.RENT_DATE_INPUT, Keys.ENTER)

    @allure.step('Клик на поле"Срок аренды"')
    def click_period_field(self):
        self.click_on_element(OrderPageLocators.RENT_DURATION_DROPDOWN)

    @allure.step('Выбор срока аренды')
    def click_days_button(self, days_button):
        self.click_on_element(days_button)

    @allure.step('Выбор цвета самоката')
    def click_on_color_button(self, colour_button):
        self.click_on_element(colour_button)

    @allure.step('Заполнение поля "Комментарий для курьера"')
    def set_comment(self, comment):
        self.send_keys(OrderPageLocators.COMMENT_INPUT, comment)

    @allure.step('Заполнение формы "Про аренду"')
    def fill_out_rent_details_form(self, date, comment, days_button, colour_button):
        self.wait_for_rent_details_form_to_be_loaded()
        self.set_date(date)
        self.click_period_field()
        self.click_days_button(days_button)
        self.click_on_color_button(colour_button)
        self.set_comment(comment)

    @allure.step('Клик на кнопку "Заказать"')
    def click_order_button(self):
        self.click_on_element(OrderPageLocators.ORDER_BUTTON)

    @allure.step('Ожидание загрузки окна "Хотите оформить заказ?"')
    def wait_for_load_order_header(self):
        self.wait_for_element_to_be_visible(OrderPageLocators.ORDER_CONFIRMATION_CAPTION)

    @allure.step('Клик на кнопку "Да" в форме "Хотите оформить заказ?"')
    def click_on_yes_button(self):
        self.click_on_element(OrderPageLocators.ORDER_CONFIRMATION_YES_BUTTON)

    @allure.step('Проверка появления окна создания заказа с кнопкой "Посмотреть статус"')
    def check_if_success_window_visible(self):
        self.wait_for_element_to_be_visible(OrderPageLocators.POPUP_STATUS_BUTTON)
        actual_text = self.get_raw_text(OrderPageLocators.POPUP_STATUS_BUTTON)
        assert actual_text == 'Посмотреть статус', 'Окно создания заказа с кнопкой "Посмотреть статус" не появилось'

    @allure.step('Клик на логотип "Самокат"')
    def click_on_scooter_logo(self):
        self.wait_for_element_to_be_clickable(OrderPageLocators.SAMOKAT_LOGO)
        self.click_on_element(OrderPageLocators.SAMOKAT_LOGO)
