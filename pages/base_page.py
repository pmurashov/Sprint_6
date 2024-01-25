import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть сайт")
    def go_to_site(self, url):
        self.driver.get(url)

    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    def send_keys(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)

    def wait_for_element_to_be_visible(self, locator):
        WebDriverWait(self.driver, 30).until(
            expected_conditions.visibility_of_element_located(locator))

    def wait_for_element_to_be_clickable(self, locator):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(locator))

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def get_current_url(self):
        current_url = self.driver.current_url
        return current_url

    def get_raw_text(self, locator):
        actually_text = self.driver.find_element(*locator).text
        return actually_text

    def switch_to_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
