from .base_page import BasePage
from .locators import LoginPageLocators

from global_variables import oauthurl

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_field()
        self.should_be_password_field()
        self.should_be_login_url()

    def should_be_login_url(self):
        assert oauthurl in self.browser.current_url, '(/oauth) Login url is not found'

    def should_be_login_field(self):
        assert self.is_element_present(*LoginPageLocators.login_field), 'Login field is not present'

    def should_be_password_field(self):
        assert self.is_element_present(*LoginPageLocators.password_field), 'password field is not present'
    
    def login(self, username, password):
        #self.browser.find_element(*BasePageLocators.LOGIN_LINK).click()
        #self.should_be_login_page
        enterlogin = self.browser.find_element(*LoginPageLocators.login_field)
        enterlogin.send_keys(username)
        enterpassword = self.browser.find_element(*LoginPageLocators.password_field)
        enterpassword.send_keys(password)
        submitbtn = self.browser.find_element(*LoginPageLocators.login_button_locator)
        submitbtn.click()

    def should_be_alert_about_wrong_data(self):
        assert self.is_element_present(*LoginPageLocators.alert_about_wrong_data_locator), 'alert about wrong login or password is not present'

    def should_be_alert_text_about_wrong_data(self):
        assert self._getattribute_(*LoginPageLocators.alert_about_wrongdata_text_locator), 'alert text present has been changed, should be "Неверно введен пароль. Попробуйте снова. Проверьте правильность написания на отсутствие пробелов до и после ввода логина."'