import allure
from locators.main_page_locators import IconsLocators
from pages.main_page import MainPage
from data import Urls


class TestClickIcons:

    @allure.title('Проверка кнопки Самокат')
    @allure.description('Проверка клика по кнопке Самокат')
    def test_click_icon_scooter(self, driver):
        main_page = MainPage(driver)
        assert 'когда накатаетесь — заберём' in main_page.click_to_icon_scooter()

    @allure.title('Проверяем кнопку Яндекс')
    @allure.description('Проверка кнопки Яндекс')
    def test_click_icon_yandex(self, driver):
        main_page = MainPage(driver)

        main_page.click_to_icon_yandex()
        assert Urls.yandex_dzen in main_page.get_current_url()
