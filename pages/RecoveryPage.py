from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

import allure

class RecoveryPageLocators:
    BUTTON_PHONE = (By.XPATH, '//*[@data-l="t,phone"]')
    BUTTON_EMAIL = (By.XPATH, '//*[@data-l="t,email"]')
    QR_CODE = (By.XPATH, '//*[@class="qr_code"]')
    BUTTON_SUPPORT = (By.XPATH, '//*[@data-l="t,support"]')


class RecoveryPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()


    def check_page(self):
        with allure.step('Проверка загруженной страницы'):
            self.attach_screenshot()
        self.find_element(RecoveryPageLocators.BUTTON_PHONE)
        self.find_element(RecoveryPageLocators.BUTTON_EMAIL)
        self.find_element(RecoveryPageLocators.QR_CODE)
        self.find_element(RecoveryPageLocators.BUTTON_SUPPORT)