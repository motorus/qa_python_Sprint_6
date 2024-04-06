from selenium.webdriver.common.by import By


class Locators:
    QUESTION_LOCATOR = [By.ID, "accordion__heading-{}"]
    ANSWER_LOCATOR = [By.ID, "accordion__panel-{}"]
    HTML_TAG = [By.TAG_NAME, "html"]


class IconsLocators:
    SCOOTER_ICON = By.XPATH, "//img[@alt='Scooter']"
    YANDEX_ICON = By.XPATH, "//a[@href='//yandex.ru']"
    ALTERNATE_YANDEX_ICON = By.XPATH, '//img[@alt="Yandex"]'
    TEXT_IN_MAIN_PAGE = By.XPATH, "//div[contains(text(), 'Привезём его прямо к вашей двери')]"
