from .base_page import BasePage
from .locators import OrderPassengerLocators
from client.pages.main_page import MainPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os


class OrderPassengerPage(MainPage, BasePage):

    def wait_order_passenger_page_to_appear(self):        
       self.wait_adress_1_field_to_appear()
       self.wait_adress_1_field_to_be_clickable()    
       
    def wait_adress_1_field_to_appear(self):
       assert self.is_element_present(*OrderPassengerLocators.adress_1_locator), "Adress field 1 is not present"

    def wait_adress_1_field_to_be_clickable(self):
        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(OrderPassengerLocators.adress_1_locator))

    def make_order_2_points(self):                      #маршрут не строится через ввод адрес+enter  баг есть
        self.input_adress_1()
        self.input_adress_2()

    def input_adress_1(self, adress_1):
        point_1 = self.browser.find_element(*OrderPassengerLocators.adress_1_locator)
        point_1.send_keys(adress_1)
        point_1.send_keys(Keys.RETURN)
        # point_1.click()

    def input_adress_2(self, adress_2):
        point_2 = self.browser.find_element(*OrderPassengerLocators.adress_2_locator)
        point_2.send_keys(adress_2)
        point_2.send_keys(Keys.RETURN)
        # point_2.click()


    def click_adress_from_bookmarks_1(self): #подготовленный заранее тут хардкод адресов выбор из тех что уже добавлены  т.к через адрес enter маршрут не строится баг есть
        self.browser.implicitly_wait(5)  #неявно ожидаем прогрузки страницы, без этого иногда падает с ошибкой
        self.browser.find_element(*OrderPassengerLocators.adress_1_locator).click()
        adressbookmark1 = self.browser.find_element(*OrderPassengerLocators.adress_moscow_kutuzovski_prosp_57)
        adressbookmark1.click()
     

    def click_adress_from_bookmarks_2(self): 
        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(OrderPassengerLocators.adress_2_locator))
        self.browser.find_element(*OrderPassengerLocators.adress_2_locator).click()
        adressbookmark2 = self.browser.find_element(*OrderPassengerLocators.adress_moscow_big_dmitrovka_street_5_6)
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", adressbookmark2)
        adressbookmark2.click()   

    
    def wait_for_route_to_be_done(self):
        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(OrderPassengerLocators.go_now_button_locator))


    def go_now_button(self):
        gonow = self.browser.find_element(*OrderPassengerLocators.go_now_button_locator)
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", gonow)
        gonow.click()   

    def go_taxi_section(self):
        self.browser.find_element(*OrderPassengerLocators.taxi_section_locator).click()
      
    def go_next_from_transport_selection_section(self):
        self.browser.find_element(*OrderPassengerLocators.go_next_from_transport_selection_section_locator).click()

    def go_economy_taxi_tariff(self):
        economytaxi = self.browser.find_element(*OrderPassengerLocators.taxi_econom_locator)
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", economytaxi)
        economytaxi.click()   
        #self.browser.find_element(*OrderPassengerLocators.taxi_econom_locator).click()

    def go_comfort_taxi_tariff(self):
        comforttaxi = self.browser.find_element(*OrderPassengerLocators.taxi_comfort_locator)
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", comforttaxi)
        comforttaxi.click()
        
    def go_comfort_plus_taxi_tariff(self):
        comfortplustaxi = self.browser.find_element(*OrderPassengerLocators.taxi_comfort_plus_locator)
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", comfortplustaxi)        
        comfortplustaxi.click()

    def go_business_taxi_tariff(self):
        businesstaxi = self.browser.find_element(*OrderPassengerLocators.taxi_business_locator)
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", businesstaxi)    
        businesstaxi.click()

    def go_next_from_taxi_section(self):
        self.browser.find_element(*OrderPassengerLocators.go_next_from_taxi_section_locator).click()  

    def go_from_together_ride_option_to_individual(self):
        self.browser.find_element(*OrderPassengerLocators.go_from_together_ride_option_to_individual_locator).click()

    def go_next_from_taxi_individual_or_together(self):
        self.browser.find_element(*OrderPassengerLocators.go_next_from_taxi_individual_or_together_locator).click()

    def make_a_passenger_order(self):
        makeapassengerorder = self.browser.find_element(*OrderPassengerLocators.make_passenger_order_locator)
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", makeapassengerorder)
        makeapassengerorder.click()


    def go_economy_details_order(self):
        self.browser.find_element(*OrderPassengerLocators.taxi_economy_go_to_order_details).click()

    def order_price_client_find(self):
        order_price_client = self.browser.find_element(*OrderPassengerLocators.taxi_economy_order_details_price_locator)
        #print(order_price_client.text)
        return order_price_client.text
        

    def order_humanreadebleid_client_find(self):
        THEX = self.browser.find_element(*OrderPassengerLocators.taxi_economy_order_details_humanreadebleid_locator)
        humanreadebleid = THEX.get_attribute("title")    
        return humanreadebleid
    
    def show_client_humanreadebleid_in_terminal(self, humanreadebleid):
        print(humanreadebleid)


    def go_OT_order_screen(self):
        OT = self.browser.find_element(*OrderPassengerLocators.OT_section_locator)
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", OT)    
        OT.click()

    def go_to_OT_drop_menu_to_choose_type_of_transport(self):
        self.go_click_OT_drop_menu_to_choose_type_of_transport()
        self.go_wait_to_appear_OT_drop_menu_to_choose_type_of_transport()

    def go_click_OT_drop_menu_to_choose_type_of_transport(self):
        self.browser.find_element(*OrderPassengerLocators.OT_type_drop_menu_locator).click()

    def go_wait_to_appear_OT_drop_menu_to_choose_type_of_transport(self):
        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(OrderPassengerLocators.OT_type_metro_from_drop_menu_locator))

    def go_to_in_city_compensation_section(self):
        self.browser.find_element(*OrderPassengerLocators.OT_compensation_type_travel_in_city_name_locator).click()

    def go_choose_autobus_type_from_drop_menu(self):
        self.browser.find_element(*OrderPassengerLocators.OT_type_autobus_from_drop_menu_locator).click()
    
    def go_choose_trolleybus_type_from_drop_menu(self):
        self.browser.find_element(*OrderPassengerLocators.OT_type_trolleybus_from_drop_menu_locator).click()

    def go_choose_trum_type_from_drop_menu(self):
        self.browser.find_element(*OrderPassengerLocators.OT_type_trum_from_drop_menu_locator).click()

    def go_choose_metro_type_from_drop_menu(self):
        self.browser.find_element(*OrderPassengerLocators.OT_type_metro_from_drop_menu_locator).click()

    def make_an_OT_order(self):
        makeOTorder = self.browser.find_element(*OrderPassengerLocators.OT_make_an_order_button_locator)
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", makeOTorder)   
        makeOTorder.click() 

    def increase_ticket_number(self):
        self.browser.find_element(*OrderPassengerLocators.OT_amount_of_tickets_increase_locator).click()

    def go_to_city_to_city_compensation_section(self):
        self.browser.find_element(*OrderPassengerLocators.OT_type_travel_city_to_city_locator).click()

    def go_city_to_city_drop_menu_to_choose_type_of_transport(self):
        self.browser.find_element(*OrderPassengerLocators.OT_city_to_city_drop_menu_locator).click()
    
    def go_city_to_city_choose_autobus_type_from_drop_menu(self):
        self.browser.find_element(*OrderPassengerLocators.OT_type_city_to_city_autobus_choose_from_drop_menu_locator).click()

    def input_type_travel_city_to_city_COST_field(self, costOT):
        travelCOSTOT = self.browser.find_element(*OrderPassengerLocators.OT_type_travel_city_to_city_COST_field_locator)
        travelCOSTOT.send_keys(costOT)
        travelCOSTOT.send_keys(Keys.RETURN) #тут снова баг, ввод не работает, для применения нужно сместить фокус на другой элемент
        self.browser.find_element(*OrderPassengerLocators.OT_type_travel_city_to_city_locator).click()
        

    def input_type_travel_city_to_city_ADD_FILE_for_Ticket(self):
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, 'OT_ticket.jpg')
        inputfile = self.browser.find_element(*OrderPassengerLocators.OT_type_travel_city_to_city_ADD_FILE_ticket_locator)
        inputfile.send_keys(file_path)

    def should_be_order_done_text(self):
        assert self.is_element_present(*OrderPassengerLocators.order_done_locator), "Order Done text is not Present 'Всё получилось'"
