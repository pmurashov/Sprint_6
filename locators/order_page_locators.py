from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Заголовок "Для кого самокат"
    ORDER_CAPTION = (By.CLASS_NAME, 'Order_Header__BZXOb')
    # Поле "Имя"
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, '[placeholder="* Имя"]')
    # Поле "Фамилия"
    LAST_NAME_INPUT = (By.CSS_SELECTOR, '[placeholder="* Фамилия"]')
    # Поле "Адрес: куда привезти заказ"
    ADDRESS_INPUT = (By.CSS_SELECTOR, '[placeholder="* Адрес: куда привезти заказ"]')
    # Поле "Станция метро"
    SUBWAY_STATION = (By.CSS_SELECTOR, '[placeholder="* Станция метро"]')
    # Поле "Телефон: на него позвонит курьер"
    PHONE_INPUT = (By.CSS_SELECTOR, '[placeholder="* Телефон: на него позвонит курьер"]')
    # Кнопка "Далее"
    NEXT_BUTTON = (By.XPATH, '//button[text()="Далее"]')
    # Станция метро "Черкизовская"
    SAVYOLOVSKAYA_STATION = (By.XPATH, '//div[text()="Савёловская"]')
    # Станция метро "Курская"
    KOZHOOKHOVSKAYA_STATION = (By.XPATH, '//div[text()="Кожуховская"]')

    # Заголовок "Про аренду"
    ABOUT_RENT_CAPTION = (By.CLASS_NAME, 'Order_Header__BZXOb')
    # Поле "Когда привезти самокат"
    RENT_DATE_INPUT = (By.CSS_SELECTOR, '[placeholder="* Когда привезти самокат"]')
    # Поле "Срок аренды"
    RENT_DURATION_DROPDOWN = (By.CLASS_NAME, 'Dropdown-placeholder')
    # выпадающий список срока аренды "сутки"
    DROPDOWN_ONE_DAY = (By.XPATH, '//div[text() = "сутки"]')
    # выпадающий список срока аренды "двое суток"
    DROPDOWN_TWO_DAYS = (By.XPATH, '//div[text() = "двое суток"]')
    # чекбокс цвет самоката "чёрный жемчуг"
    SCOOTER_COLOR_BLACK = (By.ID, 'black')
    # чекбокс цвет самоката "серая безысходность"
    SCOOTER_COLOR_GREY = (By.ID, 'grey')
    # Поле "Комментарий для курьера"
    COMMENT_INPUT = (By.CSS_SELECTOR, '[placeholder="Комментарий для курьера"]')
    # Кнопка "заказать"
    ORDER_BUTTON = (By.XPATH, '//div[@class = "Order_Buttons__1xGrp"]/button[text()="Заказать"]')
    # Текст "Хотите оформить заказ?" в диалоговом окне
    ORDER_CONFIRMATION_CAPTION = (By.CLASS_NAME, 'Order_ModalHeader__3FDaJ')
    # Кнопка "Да" в окне "Хотите оформить заказ?"
    ORDER_CONFIRMATION_YES_BUTTON = (By.XPATH, '//button[text()="Да"]')
    # Кнопка "Посмотреть статус" в форме "Заказ оформлен"
    POPUP_STATUS_BUTTON = (By.XPATH, '//button[text()="Посмотреть статус"]')
    # Лого Самокат
    SAMOKAT_LOGO = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR')
