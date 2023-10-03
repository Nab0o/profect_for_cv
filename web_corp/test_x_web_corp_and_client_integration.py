from web_corp.pages.login_page import webcorpLoginPage
from web_corp.pages.monitoring_page import MonitoringPage

from client.pages.login_page import LoginPage
from client.pages.order_passenger_page import OrderPassengerPage

from global_variables import clienturl, username, password, webcorpurl, linkclientcreate

import pytest

#@pytest.mark.need_review
@pytest.mark.smoke
class TestUserwebcorpInregrationWithClientCheckingParametres():                 
    def test_make_passenger_order_economy_taxi_and_then_go_to_details_and_get_humanreadebleid(self, browser):  
        page = LoginPage(browser, clienturl)                                                                                                          
        page.open()                                                                                            
        page.should_be_login_page()
        page.login(username, password)
        page.should_be_authorized_user()
        page = OrderPassengerPage(browser, linkclientcreate)                            #создается поездка на клиенте
        page.open()  
        page.go_to_order_page()
        page.wait_order_passenger_page_to_appear()
        page.click_adress_from_bookmarks_1()
        page.click_adress_from_bookmarks_2()
        page.go_now_button()
        page.go_taxi_section()
        page.go_next_from_transport_selection_section()
        page.go_economy_taxi_tariff()
        page.go_next_from_taxi_section()
        page.go_from_together_ride_option_to_individual()
        page.go_next_from_taxi_individual_or_together()
        page.make_a_passenger_order()
        page.go_economy_details_order()
        humanreadebleid = page.order_humanreadebleid_client_find()                                   # запоминаются данные humanreadebleid и цена поездки
        price = page.order_price_client_find()
        page = webcorpLoginPage(browser, webcorpurl)                                                # затем  происходит переход в корпаративный кабинет
        page.open()
        page.should_be_login_page()
        page.login(username, password)    
        page.should_be_authorized_user()
        page = MonitoringPage(browser, webcorpurl) 
        page.open()
        page.go_to_oto_monitoring_page()
        page.go_find_order_from_client_in_monitoring_section(humanreadebleid)                            # поиск заявки
        page.go_open_details_for_first_result_in_taxi_section()
        page.should_be_order_details_page()
        page.should_be_same_humanreadebleid_in_client_and_monitoring_order_details(humanreadebleid)         # сравниваются данные humanreadebleid и цены в детализации поездки
        page.should_be_same_price_in_client_and_monitoring_order_details(price)                      #таким образом мы проверили правильность миграции данных
