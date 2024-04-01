import allure
from locators.main_page_locators import IconsLocators
from pages.main_page import MainPage
from data import Urls


class TestClickIcons:

    @allure.title('Проверка кнопки Самокат')
    @allure.description('Проверка клика по кнопке Самокат')
    def test_click_icon_scooter(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.order_page)
        main_page.click_to_element(IconsLocators.SCOOTER_ICON)
        text_from_main_page = main_page.wait_and_find_element(IconsLocators.TEXT_IN_MAIN_PAGE).text
        assert 'когда накатаетесь — заберём' in text_from_main_page


"""
    @allure.title('Проверяем кнопку Яндекс')
    @allure.description('Проверка кнопки Яндекс')
    def test_click_icon_yandex(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.main_page)

        main_page.click_to_element(IconsLocators.YANDEX_ICON)
        main_page.switch_to_window()
        main_page.wait_for_load_window(Urls.yandex_dzen)
        # !!!!!!!!!!!
        # Здравствуйте. С этим тестом я не справился.
        # При програмном клике на логотип яндекса открывается не dzen.ru, а вот такой url:
        # https://sso.passport.yandex.ru/push?uuid=85070411-eb0b-4e58-b2f9-3dcb62c10608&retpath=https%3A%2F%2Fdzen.ru%2F%3Fyredirect%3Dtrue
        # висит на нем с полминуты. Потом по таймауту выдает ошибку что не смог зайти на login.vk.com.
        # Пробовал через локатор ALTERNATE_YANDEX_ICON. Результат тот же.
        # При этом если перед програмным кликом поставить time.sleep и самому нажать мышкой на логотип то прекрасно
        # открывается dzen.ru.
        # Пробовал:
         # 1. Залогиниться в яндексе.
         # 2. Соглашаться с куками.
         # 3. Через другое соединение(расшарил с телефона WiFi)
         # 4. Пробовал через другую версию geckodriver
        # Прошу понять и простить! Спасибо!

        assert Urls.yandex_dzen in driver.current_url
"""