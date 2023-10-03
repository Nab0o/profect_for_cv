from web_corp.pages.base_page import BasePage
from web_corp.pages.login_page import webcorpLoginPage

from global_variables import webcorpbaseurl, webcorpurl, webcorpdirectories, username, password

import pytest
import time

#тесты как для страницы логина так и для общего меню basepage

#@pytest.mark.need_review
#    @pytest.mark.need_review

@pytest.mark.smoke
def test_guest_redirects_from_url_to_url_oath(browser):
    page = webcorpLoginPage(browser, webcorpbaseurl)
    page.open()
    time.sleep(2)                        #по требованиям редирект не должен занимать более 2х секунд
    page.should_be_login_page()


@pytest.mark.smoke
def test_guest_can_autorize(browser):
    page = webcorpLoginPage(browser, webcorpurl)
    page.open()
    page.should_be_login_page()
    page.login(username, password)
    page.should_be_authorized_user()

@pytest.mark.smoke
#@pytest.mark.need_review
def test_guest_can_not_autorize_with_wrong_data(browser):
    page = webcorpLoginPage(browser, webcorpurl)
    page.open()
    page.should_be_login_page()
    username = "Jhasdjodui-ASD"
    password = "klaskdhiou24" 
    page.login(username, password)
    page.should_be_alert_about_wrong_data()
    page.should_be_login_page()
    

@pytest.mark.smoke
class TestUserAutorized():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = webcorpLoginPage(browser, webcorpurl)
        page.open()
        page.should_be_login_page()
        page.login(username, password)    
        page.should_be_authorized_user()

    def test_user_can_see_sbtr_and_user_menu_icons(self, browser):
        page = BasePage(browser, webcorpurl) 
        page.open()  
        page.should_be_SbTr_icon()
        page.should_be_user_icon()

    def test_user_can_go_return_to_main_page_using_sbtr_icon(self, browser):      
        page = BasePage(browser, webcorpdirectories) 
        page.open()          
        page.go_to_main_use_SbTr_icon()
        page.should_be_main_page_url()

    def test_user_can_go_and_see_user_drop_menu(self, browser): 
        page = BasePage(browser, webcorpurl) 
        page.open()  
        page.go_to_user_drop_menu()
        page.should_be_all_drop_menu_links()              #должны отображаться все линки: переход в клиент, выход
    
    def test_user_can_go_and_see_client_app_from_user_drop_menu(self, browser):  #проверка перехода в клиент из выпадающего меню
        page = BasePage(browser, webcorpurl) 
        page.open()  
        page.go_to_user_drop_menu()
        page.go_to_client_app_from_user_drop_menu()
        page.should_be_client_app_url()

    def test_user_can_login_and_exit_from_user_drop_menu(self, browser):     #проверка выхода из аккаунта при нажатии на кнопку выход из выпадающего меню
        page = webcorpLoginPage(browser, webcorpurl) 
        page.open()  
        page.go_to_user_drop_menu()
        page.go_to_login_page_use_exit_from_user_drop_menu()
        page.should_be_login_page()
