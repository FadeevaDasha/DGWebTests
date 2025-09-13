from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

import allure

class LoginPageLocators:
    LOGIN_EMAIL = (By.ID, 'field_email')
    LOGIN_BUTTON = (By.XPATH, '//*[@data-l="t,sign_in"]')
    LOGIN_PASSWORD = (By.ID, 'field_password')
    LOGIN_TAB = (By.XPATH, '//*[@data-l="t,login_tab"]')
    LOGIN_QR_TAB = (By.XPATH, '//*[@data-l="t,qr_tab"]')
    LOGIN_QR_BUTTON = (By.XPATH, '//*[@data-l="t,get_qr"]')
    LOGIN_RESTORE = (By.XPATH, '//*[@data-l="t,restore"]')
    LOGIN_REGISTRATION = (By.XPATH, '//div[@class="external-oauth-login-footer"]/a[@data-l="t,register"]')
    LOGIN_VK = (By.XPATH, '//*[@data-l="t,vkc"]')
    LOGIN_MAIL = (By.XPATH, '//*[@data-l="t,mailru"]')
    LOGIN_YANDEX = (By.XPATH, '//*[@data-l="t,yandex"]')
    ERROR_TEXT = (By.XPATH, '//*[@class="input-e login_error"]')


class LoginPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()


    def check_page(self):
        self.find_element(LoginPageLocators.LOGIN_TAB)
        self.find_element(LoginPageLocators.LOGIN_QR_TAB)
        self.find_element(LoginPageLocators.LOGIN_EMAIL)
        self.find_element(LoginPageLocators.LOGIN_PASSWORD)
        self.find_element(LoginPageLocators.LOGIN_BUTTON)
        self.find_element(LoginPageLocators.LOGIN_QR_BUTTON)
        self.find_element(LoginPageLocators.LOGIN_REGISTRATION)
        self.find_element(LoginPageLocators.LOGIN_RESTORE)
        self.find_element(LoginPageLocators.LOGIN_VK)
        self.find_element(LoginPageLocators.LOGIN_MAIL)
        self.find_element(LoginPageLocators.LOGIN_YANDEX)


    @allure.step('Нажимаем кнопку "Войти"')
    def click_login(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()

    @allure.step('Получаем текст ошибки')
    def get_error_text(self):
        self.attach_screenshot()
        return self.find_element(LoginPageLocators.ERROR_TEXT).text

    @allure.step('Заполняем поле "Email"')
    def input_email_field(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_EMAIL).send_keys('test')