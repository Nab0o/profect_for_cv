from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from web_corp.pages.locators import BasePageLocators


from global_variables import webcorpurl, appsforurlsearch

class BasePage():

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def should_be_authorized_user(self):
        self.should_be_main_page_url()  
        self.should_be_SbTr_icon()
        self.should_be_user_icon()    


    def should_be_user_icon(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
            " probably unauthorised user"
        
    def should_be_SbTr_icon(self):
      assert self.is_element_present(*BasePageLocators.sbertransport_icon), "SberTransport icon/link is not presented"

    def should_be_main_page_url(self):
        assert webcorpurl in self.browser.current_url, 'Main page url is not found'

  
    def go_to_main_use_SbTr_icon(self):
      self.browser.find_element(*BasePageLocators.sbertransport_icon).click()


    def should_be_user_drop_menu(self):
      assert self.is_element_present(*BasePageLocators.personal_drop_menu_locator), "Personal menu icon/link is not presented"

    def go_to_user_drop_menu(self):
        self.browser.find_element(*BasePageLocators.personal_drop_menu_locator).click()

    def should_be_all_drop_menu_links(self):
       self.should_be_user_drop_menu_client_app_link()
       self.should_be_user_drop_menu_exit_link()

    def should_be_user_drop_menu_client_app_link(self):
     assert self.is_element_present(*BasePageLocators.personal_drop_menu_go_to_client_locator), "Personal menu > client app link is not presented"

    def should_be_user_drop_menu_exit_link(self):
     assert self.is_element_present(*BasePageLocators.personal_drop_menu_exit_locator), "Personal menu > exit link is not presented"

    def go_to_client_app_from_user_drop_menu(self):
       self.browser.find_element(*BasePageLocators.personal_drop_menu_go_to_client_locator).click() 

    def should_be_client_app_url(self):
        assert appsforurlsearch in self.browser.current_url, 'client app url is not found'  

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