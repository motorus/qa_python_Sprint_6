import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Ждем и ищем элемент по локатору")
    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 5).until((expected_conditions.visibility_of_element_located(locator)))
        return self.driver.find_element(*locator)

    @allure.step("Ждем пока элемент не станет кликабельным и кликаем по нему")
    def click_to_element(self, locator):
        WebDriverWait(self.driver, 5).until((expected_conditions.element_to_be_clickable(locator)))
        self.driver.find_element(*locator).click()

    def switch_to_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def wait_for_load_window(self, link):
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(link))

    @allure.step("Открывваем страницу по URL")
    def open_page(self, url):
        self.driver.get(url)

    @staticmethod
    def format_locator(locator, param):
        search_type, search_text = locator
        return (search_type, search_text.format(param))
