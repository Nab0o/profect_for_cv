from .base_page import BasePage
from .locators import MainPageLocators
from client.pages.base_page import BasePage

from global_variables import orderpassengerurl

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



class MainPage(BasePage):
    def go_to_order_page(self):
        self.push_order_passenger_button()
        self.should_be_order_passenger_link()
        self.wait_alert_to_appear()                           
        self.push_geo_alert_on_passenger_order()


    def push_order_passenger_button(self):
        self.browser.find_element(*MainPageLocators.make_order_locator).click()

    def should_be_order_passenger_link(self):
        assert orderpassengerurl in self.browser.current_url, 'Passenger order url is not found'

    def wait_alert_to_appear(self):
        WebDriverWait(self.browser, 10).until(
            EC.alert_is_present(), 'geo alert didnt appear in 10 sec')

    def push_geo_alert_on_passenger_order(self):
        alert = self.browser.switch_to.alert
        alert.accept()