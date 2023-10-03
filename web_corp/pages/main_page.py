from web_corp.pages.base_page import BasePage
from web_corp.pages.locators import MainPageLocators

from global_variables import monitoringurl, reportsurl

class MainPage(BasePage):
    def go_to_oto_monitoring_page(self):
        self.browser.find_element(*MainPageLocators.oto_monitoring_section_locator).click()

    def should_be_oto_monitoring_url_link(self):
        assert monitoringurl in self.browser.current_url, 'Monitor url is not found'

    def go_to_reports_page(self):
        self.browser.find_element(*MainPageLocators.reports_section_locator).click()

    def should_be_reports_url_link(self):
        assert reportsurl in self.browser.current_url, 'Reports url is not found'