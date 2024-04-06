from selenium.webdriver.common.by import By


class OrderButtonLocators:
    TOP_BUTTON_ORDER = By.XPATH, ".//div[@class='Header_Nav__AGCXC']/button[contains(text(),'Заказать')]"

    DOWN_BUTTON_ORDER = By.XPATH, ".//div[@class='Home_FinishButton__1_cWm']/button[contains(text(),'Заказать')]"


class OrderPageForm1Locators:
    # Заголовок нас странице заказа 1
    ORDER_HEADING_TEXT      = By.XPATH, ".//div[contains(text(),'Для кого самокат')]"
    # Поле ввода имени
    FIRST_NAME_LOCATOR      = By.CSS_SELECTOR, "input[placeholder='* Имя']"
    # Поле ввода фамилии
    SURNAME_LOCATOR         = By.CSS_SELECTOR, "input[placeholder='* Фамилия']"
    # Поле ввода адреса доставки
    ADDRESS_LOCATOR         = By.CSS_SELECTOR, "input[placeholder='* Адрес: куда привезти заказ']"
    # Выбор станции метро
    METRO_LOCATOR           = By.CSS_SELECTOR, "input[placeholder='* Станция метро']"
    # Выподающий список станций
    METRO_DROP_DOWN_LIST    = By.XPATH, "//div[contains(@class, 'select-search__select')]/ul/li"
    # Поле ввода телефона
    PHONE_LOCATOR           = By.CSS_SELECTOR, "input[placeholder='* Телефон: на него позвонит курьер']"
    # Кнопка Далее
    NEXT_BUTTON             = By.XPATH, "//div/button[contains(text(),'Далее')]"


class OrderPageForm2Locators:
    # Заголовок нас странице заказа 2
    ORDER_HEADING_TEXT      = By.XPATH, "//div[contains(text(), 'Про аренду')]"
    # Выбор даты
    FIELD_INPUT_DATE        = By.CSS_SELECTOR, "input[placeholder='* Когда привезти самокат']"
    # Выбор конкретной даты
    SELECTED_DATE           = By.XPATH, ".//div[@role='option' and (contains(text(), '{}'))]"
    # Число месяца для выбора
    DAY_NUMBER              = By.XPATH, ".//div[contains(@aria-label, '{}-е')]"
    # Период аренды
    FIELD_INPUT_PERIOD      = By.XPATH, ".//div[@class='Dropdown-placeholder' and (contains(text(), '* Срок аренды'))]"
    # Комментарий для курьера
    COMMENT_INPUT           = By.CSS_SELECTOR, "input[placeholder='Комментарий для курьера']"
    # Кнопка Заказать
    ORDER_BUTTON            = By.XPATH, (".//button[@class='Button_Button__ra12g Button_Middle__1CSJM' "
                                         "and (contains(text(), 'Заказать'))]")
    # Кнопка ДА
    ORDER_BUTTON_YES        = By.XPATH, ".//button[contains(text(), 'Да')]"
    # Заголовок "Заказ оформлен"
    FINAL_ORDER_WINDOW      = By.XPATH, ".//div[contains(text(), 'Заказ оформлен')]"

    # Локатор на цвет самоката
    COLOUR_LOCATOR            = By.ID, "{}"


