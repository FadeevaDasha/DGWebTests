import allure

from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.LoginPage import LoginPageHelper
from pages.RegistrationPage import RegistrationPageHelperHelper

BASE_URL = 'https://ok.ru/'

@allure.suite('Проверка формы регистрации')
@allure.title('Проверка рандомного выбора страны и соответствующего кода в поле телефон')
def test_registration_random_country(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.click_registration()
    RegistrationPage = RegistrationPageHelperHelper(browser)
    Selected_country_code = RegistrationPage.select_random_country()
    Actual_country_code = RegistrationPage.get_phone_field_value()
    assert Selected_country_code == Actual_country_code