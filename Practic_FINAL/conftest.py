import pytest
from selenium import webdriver

path_driver = '/DriverChrome/chromedriver.exe' # Путь до драйвера


@pytest.fixture(scope="session")
def testing_driver():
   """ Фикструра для запуска тестов """
   driver = webdriver.Chrome(path_driver)  # Путь до драйвера
   driver.maximize_window()

   yield driver

   driver.quit()


@pytest.fixture(scope="session")
def backdrop_testing_driver():
   """ Фикстура для запуска браузера в фоновом режиме """
   options = webdriver.ChromeOptions()
   options.add_argument('--headless')
   options.add_argument('disable-infobars')
   driver = webdriver.Chrome(path_driver, options=options)


   yield driver

   driver.quit()

