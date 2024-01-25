from selenium.webdriver.common.by import By


class MainPageLocators:
    # вопрос "Сколько это стоит? и как оплатить?"
    QUESTION_PAYMENT = (By.ID, 'accordion__heading-0')
    # ответ на вопрос "Сколько это стоит? и как оплатить?"
    ANSWER_PAYMENT = (By.XPATH, '//div[@id = "accordion__panel-0"]/p')
    # вопрос "Хочу сразу несколько самокатов! Так можно?"
    QUESTION_MULTIPLE_SCOOTERS = (By.ID, 'accordion__heading-1')
    # ответ на вопрос "Хочу сразу несколько самокатов! Так можно?"
    ANSWER_MULTIPLE_SCOOTERS = (By.XPATH, '//div[@id = "accordion__panel-1"]/p')
    # вопрос "Как рассчитывается время аренды?"
    QUESTION_COUNT_RENT_TIME = (By.ID, 'accordion__heading-2')
    # ответ на вопрос "Как рассчитывается время аренды?"
    ANSWER_COUNT_RENT_TIME = (By.XPATH, '//div[@id = "accordion__panel-2"]/p')
    # вопрос "Можно ли заказать самокат прямо на сегодня?"
    QUESTION_TODAY_RENT = (By.ID, 'accordion__heading-3')
    # ответ на вопрос "Можно ли заказать самокат прямо на сегодня?"
    ANSWER_TODAY_RENT = (By.XPATH, '//div[@id = "accordion__panel-3"]/p')
    # вопрос "Можно ли продлить заказ или вернуть самокат раньше?"
    QUESTION_EXTEND_OR_RETURN = (By.ID, 'accordion__heading-4')
    # ответ на вопрос "Можно ли продлить заказ или вернуть самокат раньше?"
    ANSWER_EXTEND_OR_RETURN = (By.XPATH, '//div[@id = "accordion__panel-4"]/p')
    # вопрос "Вы привозите зарядку вместе с самокатом?"
    QUESTION_CHARGER = (By.ID, 'accordion__heading-5')
    # ответ на вопрос про зарядку
    ANSWER_CHARGER = (By.XPATH, '//div[@id = "accordion__panel-5"]/p')
    # вопрос "Можно ли отменить заказ?"
    QUESTION_CANCEL_ORDER = (By.ID, 'accordion__heading-6')
    # ответ на вопрос про отмену заказа
    ANSWER_CANCEL_ORDER = (By.XPATH, '//div[@id = "accordion__panel-6"]/p')
    # вопрос 8 "Я жизу за МКАДом, привезёте?"
    QUESTION_MKAD = (By.ID, 'accordion__heading-7')
    # ответ на вопрос про МКАД
    ANSWER_MKAD = (By.XPATH, '//div[@id = "accordion__panel-7"]/p')
    # кнопка "Заказать" в хедере сайте
    HEADER_ORDER_BUTTON = (By.CLASS_NAME, 'Button_Button__ra12g')
    # кнопка "Заказать"
    ORDER_BUTTON = (By.XPATH, '//div[@class="Home_FinishButton__1_cWm"]/button')
    # лого "Яндекс" в хедере сайта
    HEADER_YA_LOGO = (By.CLASS_NAME, 'Header_LogoYandex__3TSOI')
