from web_corp.pages.base_page import BasePage
from web_corp.pages.locators import MonitoringPageLocators
from web_corp.pages.base_page import BasePage
from web_corp.pages.main_page import MainPage

from selenium.webdriver.common.keys import Keys

from global_variables import monitoringtaxiurl

class MonitoringPage(MainPage, BasePage):
    def go_find_order_from_client_in_monitoring_section(self, humanreadebleid):
        searchbar = self.browser.find_element(*MonitoringPageLocators.monitoring_taxi_search_bar_with_text_locator)
        searchbar.send_keys(humanreadebleid)
        searchbar.send_keys(Keys.RETURN)
        searchbar.send_keys(Keys.RETURN)

    def go_open_details_for_first_result_in_taxi_section(self):
        self.browser.find_element(*MonitoringPageLocators.monitoring_taxi_first_result_locator).click()

    def should_be_order_details_page(self):
        self.browser.find_element(*MonitoringPageLocators.monitoring_humanreadebleid_in_order_details_page_locator)
        assert monitoringtaxiurl in self.browser.current_url, 'Taxi in Monitoring url is not found'

    def should_be_same_humanreadebleid_in_client_and_monitoring_order_details(self, humanreadebleid):
        THEY = self.browser.find_element(*MonitoringPageLocators.monitoring_humanreadebleid_in_order_details_page_locator)
        monitoringhumanreadebleid = THEY.text                          #get_attribute("title")   
        assert humanreadebleid == monitoringhumanreadebleid, 'humanreadebleid of client order is not the same that we have opened in web corp monitoring'

    def should_be_same_price_in_client_and_monitoring_order_details(self, price):
        THEPRICE = self.browser.find_element(*MonitoringPageLocators.monitoring_price_in_order_details_page_locator)
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", THEPRICE)
        monitoringprice = THEPRICE.text                          #get_attribute("title")   
        assert price == monitoringprice, 'price of client order is not the same thats in in web corp monitoring'