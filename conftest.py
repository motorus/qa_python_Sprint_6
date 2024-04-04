import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():

    options = webdriver.FirefoxOptions()
    options.add_argument('--windows-size=1920,1080')
    driver = webdriver.Firefox(options=options)

    driver.maximize_window()

    yield driver
    driver.quit()
