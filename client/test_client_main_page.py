from client.pages.login_page import LoginPage
from client.pages.main_page import MainPage

from global_variables import clienturl, linkclientcreate, username, password

import pytest

#@pytest.mark.need_review
@pytest.mark.smoke
class TestUserGoFromMainPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, clienturl)
        page.open()
        page.should_be_login_page()
        page.login(username, password)
        page.should_be_authorized_user()
        
    def test_go_to_order_page(self, browser):
        page = MainPage(browser, linkclientcreate) 
        page.open()  
        page.go_to_order_page()
