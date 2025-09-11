from pyexpat.errors import messages
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_element_located(locator), message=f'Не удалось найти элемент {locator}')

    def get_url(self, url):
        return self.driver.get(url)