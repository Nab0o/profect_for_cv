from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from .locators import BasePageLocators

from global_variables import clienturl, corpforurlsearch, clientprofileurl, mytransporturl


class BasePage():

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def should_be_authorized_user(self):
        self.should_be_SbTr_icon()
        self.should_be_user_icon()    
        self.should_be_main_page_url()  

    def should_be_user_icon(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
            " probably unauthorised user"
        
    def should_be_SbTr_icon(self):
      assert self.is_element_present(*BasePageLocators.sbertransport_icon), "SberTransport icon\link is not presented"

    def should_be_main_page_url(self):
        assert clienturl in self.browser.current_url, 'Main page url is not found'
    
    def go_to_main_use_SbTr_icon(self):
      self.browser.find_element(*BasePageLocators.sbertransport_icon).click()

    def should_be_user_drop_menu(self):
      assert self.is_element_present(*BasePageLocators.personal_drop_menu_locator), "Personal menu icon\link is not presented"

    def go_to_user_drop_menu(self):
        self.browser.find_element(*BasePageLocators.personal_drop_menu_locator).click()

    def should_be_all_drop_menu_links(self):
       self.should_be_user_drop_menu_profile_link()
       self.should_be_user_drop_menu_my_transport_link()
       self.should_be_user_drop_menu_corp_office_link()
       self.should_be_user_drop_menu_exit_link()

    def should_be_user_drop_menu_profile_link(self):
      assert self.is_element_present(*BasePageLocators.personal_drop_menu_profile_locator), "Personal menu > profile link is not presented"

    def should_be_user_drop_menu_my_transport_link(self):
        assert self.is_element_present(*BasePageLocators.personal_drop_menu_my_transport_locator), "Personal menu > my transport link is not presented"

    def should_be_user_drop_menu_corp_office_link(self):
     assert self.is_element_present(*BasePageLocators.personal_drop_menu_corp_office_locator), "Personal menu > corp office link is not presented"

    def should_be_user_drop_menu_exit_link(self):
     assert self.is_element_present(*BasePageLocators.personal_drop_menu_exit_locator), "Personal menu > exit link is not presented"

    def go_to_profile_use_user_drop_menu(self):
      self.browser.find_element(*BasePageLocators.personal_drop_menu_profile_locator).click() 

    def should_be_profile_url(self):
        assert clientprofileurl in self.browser.current_url, 'Profile page url is not found'

    def go_to_my_transport_use_user_drop_menu(self):
       self.browser.find_element(*BasePageLocators.personal_drop_menu_my_transport_locator).click() 

    def should_be_my_transport_url(self):
        assert mytransporturl in self.browser.current_url, 'My transport page url is not found'

    def go_to_corp_office_page_from_user_drop_menu(self):
       self.browser.find_element(*BasePageLocators.personal_drop_menu_corp_office_locator).click()

    def should_be_my_corp_office_url(self ):	
       assert corpforurlsearch in self.browser.current_url, 'Corp office url is not found'

    def go_to_login_page_use_exit_from_user_drop_menu(self):
       self.browser.find_element(*BasePageLocators.personal_drop_menu_exit_locator).click()


#     how=method                what = selector
    def is_element_present(self, method, selector):
        try:
            self.browser.find_element(method, selector)
        except (NoSuchElementException):
            return False
        return True

    def is_not_element_present(self, method, selector, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((method, selector)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, method, selector, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((method, selector)))
        except TimeoutException:
            return False
        return True