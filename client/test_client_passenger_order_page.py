from client.pages.login_page import LoginPage
from client.pages.order_passenger_page import OrderPassengerPage

from global_variables import clienturl, linkclientcreate, username, password

import pytest


@pytest.mark.smoke
class TestUserMakePassengerOrder():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, clienturl)
        page.open()
        page.should_be_login_page()
        page.login(username, password)
        page.should_be_authorized_user()
        page = OrderPassengerPage(browser, linkclientcreate) 
        page.open()  
        page.go_to_order_page()

    
    def test_make_passenger_order_route_done(self, browser):
        page = OrderPassengerPage(browser, linkclientcreate) 
        page.wait_order_passenger_page_to_appear()
        page.click_adress_from_bookmarks_1()
        page.click_adress_from_bookmarks_2()
        page.wait_for_route_to_be_done()

    #@pytest.mark.need_review
    def test_make_passenger_order_economy_taxi(self, browser):
        page = OrderPassengerPage(browser, linkclientcreate) 
        page.wait_order_passenger_page_to_appear()
        page.click_adress_from_bookmarks_1()
        page.click_adress_from_bookmarks_2()
        page.go_now_button()
        page.go_taxi_section()
        page.go_next_from_transport_selection_section()
        page.go_economy_taxi_tariff()        
        page.go_next_from_taxi_section()
        page.go_next_from_taxi_individual_or_together()
        page.make_a_passenger_order()
        page.should_be_order_done_text()

    
    #@pytest.mark.need_review
    def test_make_passenger_order_comfort_taxi(self, browser):
        page = OrderPassengerPage(browser, linkclientcreate) 
        page.wait_order_passenger_page_to_appear()
        page.click_adress_from_bookmarks_1()
        page.click_adress_from_bookmarks_2()
        page.go_now_button()
        page.go_taxi_section()
        page.go_next_from_transport_selection_section()
        page.go_comfort_taxi_tariff()
        page.go_next_from_taxi_section()
        page.go_next_from_taxi_individual_or_together()
        page.make_a_passenger_order()
        page.should_be_order_done_text()

    
    #@pytest.mark.need_review
    def test_make_passenger_order_comfort_plus_taxi(self, browser):
        page = OrderPassengerPage(browser, linkclientcreate) 
        page.wait_order_passenger_page_to_appear()
        page.click_adress_from_bookmarks_1()
        page.click_adress_from_bookmarks_2()
        page.go_now_button()
        page.go_taxi_section()
        page.go_next_from_transport_selection_section()
        page.go_comfort_plus_taxi_tariff()
        page.go_next_from_taxi_section()
        page.go_next_from_taxi_individual_or_together()
        page.make_a_passenger_order()
        page.should_be_order_done_text()

    #@pytest.mark.need_review
    def test_make_passenger_order_business_taxi(self, browser):
        page = OrderPassengerPage(browser, linkclientcreate) 
        page.wait_order_passenger_page_to_appear()
        page.click_adress_from_bookmarks_1()
        page.click_adress_from_bookmarks_2()
        page.go_now_button()
        page.go_taxi_section()
        page.go_next_from_transport_selection_section()
        page.go_business_taxi_tariff()
        page.go_next_from_taxi_section()
        page.go_next_from_taxi_individual_or_together()
        page.make_a_passenger_order()
        page.should_be_order_done_text()

    #@pytest.mark.need_review
    def test_make_OT_order_autobus(self, browser):
        page = OrderPassengerPage(browser, linkclientcreate) 
        page.wait_order_passenger_page_to_appear()
        page.click_adress_from_bookmarks_1()
        page.click_adress_from_bookmarks_2()
        page.go_now_button()
        page.go_OT_order_screen()
        page.go_to_in_city_compensation_section()
        page.go_to_OT_drop_menu_to_choose_type_of_transport()
        page.go_choose_autobus_type_from_drop_menu()
        page.make_an_OT_order()
        page.should_be_order_done_text()
    
    #@pytest.mark.need_review
    def test_make_OT_order_trolleybus(self, browser):
        page = OrderPassengerPage(browser, linkclientcreate) 
        page.wait_order_passenger_page_to_appear()
        page.click_adress_from_bookmarks_1()
        page.click_adress_from_bookmarks_2()
        page.go_now_button()
        page.go_OT_order_screen()
        page.go_to_in_city_compensation_section()
        page.go_to_OT_drop_menu_to_choose_type_of_transport()
        page.go_choose_trolleybus_type_from_drop_menu()
        page.make_an_OT_order()
        page.should_be_order_done_text()

    #@pytest.mark.need_review
    def test_make_OT_order_trum(self, browser):
        page = OrderPassengerPage(browser, linkclientcreate) 
        page.wait_order_passenger_page_to_appear()
        page.click_adress_from_bookmarks_1()
        page.click_adress_from_bookmarks_2()
        page.go_now_button()
        page.go_OT_order_screen()
        page.go_to_in_city_compensation_section()
        page.go_to_OT_drop_menu_to_choose_type_of_transport()
        page.go_choose_trum_type_from_drop_menu()
        page.make_an_OT_order()
        page.should_be_order_done_text()

    #@pytest.mark.need_review
    def test_make_OT_order_metro(self, browser):
        page = OrderPassengerPage(browser, linkclientcreate) 
        page.wait_order_passenger_page_to_appear()
        page.click_adress_from_bookmarks_1()
        page.click_adress_from_bookmarks_2()
        page.go_now_button()
        page.go_OT_order_screen()
        page.go_to_in_city_compensation_section()
        page.go_to_OT_drop_menu_to_choose_type_of_transport()
        page.go_choose_metro_type_from_drop_menu()
        page.make_an_OT_order()
        page.should_be_order_done_text()


    #@pytest.mark.need_review
    @pytest.mark.parametrize("costOT", ['1', '1500', '5000'])                         #заказ с разными ценами
    def test_make_OT_order_city_to_city_with_document(self, browser, costOT):
        page = OrderPassengerPage(browser, linkclientcreate) 
        page.wait_order_passenger_page_to_appear()
        page.click_adress_from_bookmarks_1()
        page.click_adress_from_bookmarks_2()
        page.go_now_button()
        page.go_OT_order_screen()
        page.go_to_city_to_city_compensation_section()
        page.go_city_to_city_drop_menu_to_choose_type_of_transport()
        page.go_city_to_city_choose_autobus_type_from_drop_menu()
        page.input_type_travel_city_to_city_COST_field(costOT)
        page.input_type_travel_city_to_city_ADD_FILE_for_Ticket()
        page.make_an_OT_order()
        page.should_be_order_done_text()