from client.pages.base_page import BasePage
from client.pages.login_page import LoginPage

from global_variables import clienturlredirectfrombaseurl, clienturl, username, password
import pytest
import time

#@pytest.mark.need_review       

@pytest.mark.smoke
def test_guest_redirects_from_url_to_url_oath(browser):
    page = LoginPage(browser, clienturlredirectfrombaseurl)
    page.open()
    time.sleep(2)                  #по требованиям редирект не должен занимать более 2х секунд
    page.should_be_login_page()

@pytest.mark.smoke
def test_guest_can_autorize(browser):
    page = LoginPage(browser, clienturl)
    page.open()
    page.should_be_login_page()
    page.login(username, password)
    page.should_be_authorized_user()

@pytest.mark.smoke
@pytest.mark.xfail    #bug, происходит переход на страницу main пустую, алерт есть
def test_guest_can_not_autorize_with_wrong_data(browser):
    page = LoginPage(browser, clienturl)
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
        page = LoginPage(browser, clienturl)
        page.open()
        page.should_be_login_page()
        page.login(username, password)    
        page.should_be_authorized_user()

    def test_user_can_see_sbtr_and_user_menu_icons(self, browser):        
        page = BasePage(browser, clienturl) 
        page.open()  
        page.should_be_SbTr_icon()
        page.should_be_user_icon()

    def test_user_can_go_and_see_user_drop_menu(self, browser): 
        page = BasePage(browser, clienturl) 
        page.open()  
        page.go_to_user_drop_menu()
        page.should_be_all_drop_menu_links()           #проверяет что отображаются все линки для перехода: профиль, мой транспорт, корпоративный кабинет,выход

    
    def test_user_can_go_and_see_profile_page_from_user_drop_menu(self, browser):  #проверка перехода в профиль из выпадающего меню
        page = BasePage(browser, clienturl) 
        page.open()  
        page.go_to_user_drop_menu()
        page.go_to_profile_use_user_drop_menu()
        page.should_be_profile_url()

    def test_user_can_go_return_to_main_page_using_sbtr_icon(self, browser):    #проверка работоспособности иконки
        page = BasePage(browser, clienturl) 
        page.open()  
        page.go_to_user_drop_menu()
        page.go_to_profile_use_user_drop_menu()
        page.go_to_main_use_SbTr_icon()
        page.should_be_main_page_url()                                   #should be main page

    def test_user_can_go_and_see_corp_office_page_from_user_drop_menu(self, browser):  #проверка перехода мой транспорт из выпадающего меню
        page = BasePage(browser, clienturl) 
        page.open()  
        page.go_to_user_drop_menu()
        page.go_to_corp_office_page_from_user_drop_menu()
        page.should_be_my_corp_office_url()
    

    def test_user_can_go_and_see_corp_office_from_user_drop_menu(self, browser):    #проверка перехода в корпоративный кабинет из выпадающего меню
        page = BasePage(browser, clienturl) 
        page.open()  
        page.go_to_user_drop_menu()
        page.go_to_corp_office_page_from_user_drop_menu()
        page.should_be_my_corp_office_url()


    def test_user_can_login_and_exit_from_user_drop_menu(self, browser):   #проверка выхода из аккаунта по нажатию на кнопку выход из выпадающего меню
        page = LoginPage(browser, clienturl) 
        page.open()  
        page.go_to_user_drop_menu()
        page.go_to_login_page_use_exit_from_user_drop_menu()
        page.should_be_login_page()